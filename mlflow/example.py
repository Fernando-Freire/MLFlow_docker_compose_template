# This is an example feature definition file

from datetime import timedelta

from feast import Entity, FeatureService, FeatureView, Field, FileSource
from feast.types import Float32, Int64

# Read data from parquet files. Parquet is convenient for local development mode. For
# production, you can use your favorite DWH, such as BigQuery. See Feast documentation
# for more info.
sample_products = FileSource(
    path="/feature_repo/data/sample_products.parquet",
    timestamp_field="event_timestamp",
    created_timestamp_column="created",
)

test_products = FileSource(
    path="/feature_repo/data/test_products.parquet",
    timestamp_field="event_timestamp",
    created_timestamp_column="created",
)

