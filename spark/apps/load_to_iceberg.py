from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Convert TPCH to Iceberg") \
    .config("spark.sql.catalog.iceberg", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.iceberg.catalog-impl", "org.apache.iceberg.hadoop.HadoopCatalog") \
    .config("spark.sql.catalog.iceberg.warehouse", "s3a://iceberg/") \
    .config("spark.sql.catalog.iceberg.io-impl", "org.apache.iceberg.hadoop.HadoopFileIO") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000") \
    .config("spark.hadoop.fs.s3a.access.key", "minio") \
    .config("spark.hadoop.fs.s3a.secret.key", "minio123") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .getOrCreate()

# Read from .tbl file
df = spark.read.option("delimiter", "|").option("inferSchema", True).csv("s3a://tpch/customer.tbl")

# Drop the last empty column (because of trailing '|')
df = df.drop("_c8")  # customer.tbl has 8 columns, but ends with a pipe

# Rename columns appropriately
df = df.toDF("c_custkey", "c_name", "c_address", "c_nationkey", "c_phone", "c_acctbal", "c_mktsegment", "c_comment")

# Create Iceberg table (overwrite if exists)
df.writeTo("iceberg.tpch.customer").using("iceberg").createOrReplace()

print("Customer table written to Iceberg in Parquet format on Minio")
