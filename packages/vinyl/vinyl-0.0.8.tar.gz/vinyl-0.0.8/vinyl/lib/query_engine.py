from vinyl.lib.project import Project
from vinyl.lib.table import VinylTable


class QueryEngineResult:
    def __init__(self, table: VinylTable):
        self.table = table

    def to_pandas(self):
        return self.table.execute("pandas")

    def to_records(self):
        df = self.to_pandas()
        for col, dtype in df.dtypes.items():
            if dtype.kind == "M":  # Check for datetime64 types
                df[col] = df[col].dt.strftime("%Y-%m-%dT%H:%M:%S")

        return df.to_dict("records")

    def columns(self):
        return self.table.columns

    def numpy_rows(self):
        df = self.to_pandas()
        return [tuple(row) for row in df.to_numpy()]


class QueryEngine:
    def __init__(self, project: Project):
        self.project = project

    def _model(self, name: str, limit: str):
        table = self.project._get_model(name)
        return QueryEngineResult(table.limit(limit))

    def _metric(self, name: str, grain: str, limit: int):
        if "=" not in grain:
            raise ValueError("Invalid bucket format. Ex: 'days=1'")

        bucket_grain, bucket_value = grain.split("=")
        metrics = self.project._get_metric_store(name)

        cols = [getattr(metrics, name) for name in metrics._metrics_dict.keys()]

        table = metrics.select(
            [
                metrics.ts.dt.floor(**{bucket_grain: bucket_value}),
                *cols,
            ]
        )

        return QueryEngineResult(table.limit(limit))
