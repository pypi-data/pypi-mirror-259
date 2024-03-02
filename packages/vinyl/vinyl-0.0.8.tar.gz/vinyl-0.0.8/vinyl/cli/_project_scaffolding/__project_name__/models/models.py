from vinyl import model, metric, MetricStore

from __project_name__.sources.local_filesystem.stores import Stores
from __project_name__.sources.local_filesystem.store_num_transactions import (
    StoreNumTransactions,
)


@model(deps=[Stores, StoreNumTransactions])
def top_stores(stores, txns):
    table = stores.join(txns, ["store_nbr"])
    table.aggregate(
        cols={"num_transactions": table.transactions.sum()},
        by=[table.store_nbr, table.city, table.state],
    )
    return table.sort(by=[table.num_transactions.desc()])


@model(deps=[StoreNumTransactions, Stores])
def store_txns(txns, stores):
    table = txns.join(
        stores,
        [
            stores.store_nbr == txns.store_nbr,
        ],
    )
    return table


@metric(deps=[store_txns, MetricStore])
def sales_metrics(table, metric_store):
    metric_store.metric(
        tbl=table,
        by=[table.store_nbr, table.city, table.state],
        ts=table.date.cast("timestamp"),
        cols={
            "total_txns": table.transactions.sum(),
            "average_txns": table.transactions.mean(),
        },
    )
    return metric_store
