from pyspark.sql import SparkSession

# Initialize Spark Session with Iceberg support
spark = SparkSession.builder \
    .appName("TPC-H Iceberg Query Example") \
    .getOrCreate()

print("Iceberg Catalog Tables:")
spark.sql("SHOW TABLES IN s3.tpch").show()

# Query customer data
print("Sample customer data:")
spark.sql("SELECT * FROM s3.tpch.customer LIMIT 5").show()

# Query orders data
print("Sample orders data:")
spark.sql("SELECT * FROM s3.tpch.orders LIMIT 5").show()

# Example of a join query
print("Join query example:")
spark.sql("""
    SELECT c.c_name, o.o_orderkey, o.o_totalprice
    FROM s3.tpch.customer c
    JOIN s3.tpch.orders o ON c.c_custkey = o.o_custkey
    LIMIT 5
""").show()

# Example of a more complex query (similar to TPC-H Q3)
print("Complex query example (similar to TPC-H Q3):")
spark.sql("""
    SELECT
        o.o_orderkey,
        SUM(l.l_extendedprice * (1 - l.l_discount)) as revenue,
        o.o_orderdate,
        o.o_shippriority
    FROM
        s3.tpch.customer c,
        s3.tpch.orders o,
        s3.tpch.lineitem l
    WHERE
        c.c_custkey = o.o_custkey
        AND l.l_orderkey = o.o_orderkey
        AND c.c_mktsegment = 'BUILDING'
    GROUP BY
        o.o_orderkey,
        o.o_orderdate,
        o.o_shippriority
    ORDER BY
        revenue DESC,
        o.o_orderdate
    LIMIT 10
""").show()

# Check some Iceberg-specific metadata
print("Iceberg snapshot information:")
spark.sql("SELECT * FROM s3.tpch.customer.snapshots").show()

spark.stop()