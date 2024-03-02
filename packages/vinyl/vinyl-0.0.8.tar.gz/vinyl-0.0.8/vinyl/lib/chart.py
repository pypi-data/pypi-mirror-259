from enum import Enum
from typing import Any, Callable, Literal

from lets_plot import (
    LetsPlot,
    aes,
    coord_flip,
    facet_grid,
    facet_wrap,
    flavor_darcula,
    ggplot,
    scale_x_datetime,
    scale_y_datetime,
)
from lets_plot.plot.core import LayerSpec

from vinyl.lib.column_methods import (
    ColumnBuilder,
    ColumnListBuilder,
    base_column_type,
    column_type_without_dict,
)
from vinyl.lib.settings import PyProjectSettings


class geom(Enum):
    from lets_plot import (
        geom_area,
        geom_area_ridges,
        geom_bar,
        geom_bin2d,
        geom_boxplot,
        geom_density,
        geom_histogram,
        geom_line,
        geom_point,
        geom_smooth,
        geom_violin,
        position_dodge,
        ylab,
    )

    scatter: Callable[..., LayerSpec] = geom_point()
    line: Callable[..., LayerSpec] = geom_line()
    bar: Callable[..., LayerSpec] = geom_bar(stat="identity", position=position_dodge())
    area: Callable[..., LayerSpec] = geom_area()
    stacked_bar: Callable[..., LayerSpec] = geom_bar(stat="identity")
    percent_bar: Callable[..., LayerSpec] = (
        geom_bar() + aes(y="..prop..") + ylab("Percent of total")
    )
    histogram: Callable[..., LayerSpec] = geom_histogram()
    histogram_2d: Callable[..., LayerSpec] = geom_bin2d()
    violin: Callable[..., LayerSpec] = geom_violin()
    boxplot: Callable[..., LayerSpec] = geom_boxplot()
    density: Callable[..., LayerSpec] = geom_density()
    ridge: Callable[..., LayerSpec] = geom_area_ridges()
    trendline_lm: Callable[..., LayerSpec] = geom_smooth()
    trendline_loess: Callable[..., LayerSpec] = geom_smooth(method="loess")


class BaseChart:
    _mode: Literal["light", "dark"] = "dark"
    _geoms: geom | list[geom]
    _source: Any  # will be VinylTable, but use Any to avoid recursion
    _x: base_column_type
    _y: base_column_type | None
    _color: base_column_type | None
    _fill: base_column_type | None
    _size: base_column_type | None
    _alpha: base_column_type | None
    _facet: column_type_without_dict | None
    _coord_flip: bool = False

    from lets_plot import (
        LetsPlot,
        aes,
        coord_flip,
        facet_grid,
        facet_wrap,
        flavor_darcula,
        ggplot,
        scale_x_datetime,
        scale_y_datetime,
    )

    def __init__(
        self,
        geoms: geom | list[geom],
        source: Any,  # will be VinylTable, but use Any to avoid recursion
        x: base_column_type,
        y: base_column_type | None = None,
        color: base_column_type | None = None,
        fill: base_column_type | None = None,
        size: base_column_type | None = None,
        alpha: base_column_type | None = None,
        facet: column_type_without_dict | None = None,
        coord_flip: bool = False,
    ):
        self._geoms = geoms
        self._source = source
        self._x = x
        self._y = y
        self._color = color
        self._fill = fill
        self._size = size
        self._alpha = alpha
        self._facet = facet
        self.coord_flip = coord_flip

    def _show(self):
        LetsPlot.setup_html()
        adj_facet = self._facet if isinstance(self._facet, list) else [self._facet]
        all_cols = [
            x
            for x in [self._x]
            + [self._y]
            + [self._color]
            + [self._fill]
            + [self._size]
            + [self._alpha]
            + adj_facet
            if x is not None
        ]

        adj_data = self._source.mutate(all_cols).execute("pandas")

        ## make sure all cols are in there,
        vinyl_x = ColumnBuilder(self._source.tbl, self._x)
        type_x = vinyl_x._type
        if self._y is not None:
            vinyl_y = ColumnBuilder(self._source.tbl, self._y)
            type_y = vinyl_y._type
        aes_dict = {}
        for var in ["x", "y", "color", "fill", "size"]:
            attr = getattr(self, var)
            if attr is not None:
                aes_dict[var] = ColumnBuilder(self._source.tbl, attr)._name

        plot = ggplot(adj_data, aes(**aes_dict))
        if isinstance(self._geoms, list):
            for g in self._geoms:
                plot += g.value
        elif self._geoms is not None:
            plot += self._geoms.value
        if self._facet is not None:
            facet_names = ColumnListBuilder(self._source.tbl, adj_facet)._names
            if len(adj_facet) > 1:
                plot += facet_grid(
                    facet_names[0],
                    facet_names[1],
                )
            else:
                plot += facet_wrap(facet_names[0])
        if type_x.is_timestamp():
            plot += scale_x_datetime()
        if self._y is not None and type_y.is_timestamp():
            plot += scale_y_datetime()
        if self.coord_flip:
            plot += coord_flip()

        if PyProjectSettings()._get_setting("dark-mode") is True:
            plot += flavor_darcula()

        return plot
