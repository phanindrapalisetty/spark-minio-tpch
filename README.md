## Setting up Apache Spark with MinIO for TPC-H Data
This guide will walk you through setting up Apache Spark with MinIO as the object storage for loading and processing TPC-H benchmark data.

## Prerequisites
Docker and Docker Compose
Java 8 or higher
Scala (compatible with your Spark version)
Python 3.x (for PySpark, if needed)


## Schema Reference for TPC-H Tables
Here are the column definitions for the main TPC-H tables:

  - customer: c_custkey, c_name, c_address, c_nationkey, c_phone, c_acctbal, c_mktsegment, c_comment
  - lineitem: l_orderkey, l_partkey, l_suppkey, l_linenumber, l_quantity, l_extendedprice, l_discount, l_tax, l_returnflag, l_linestatus, l_shipdate, l_commitdate, l_receiptdate, l_shipinstruct, l_shipmode, l_comment
  - nation: n_nationkey, n_name, n_regionkey, n_comment
  - orders: o_orderkey, o_custkey, o_orderstatus, o_totalprice, o_orderdate, o_orderpriority, o_clerk, o_shippriority, o_comment
  - part: p_partkey, p_name, p_mfgr, p_brand, p_type, p_size, p_container, p_retailprice, p_comment
  - partsupp: ps_partkey, ps_suppkey, ps_availqty, ps_supplycost, ps_comment
  - region: r_regionkey, r_name, r_comment
  - supplier: s_suppkey, s_name, s_address, s_nationkey, s_phone, s_acctbal, s_comment


## Troubleshooting

  - MinIO Connection Issues: Make sure your MinIO service is running and accessible
  - Class Not Found Errors: Ensure all required dependencies are included in your build or with the --packages option
  - Access Denied: Verify your MinIO credentials and bucket permissions
  - Path Issues: Confirm that the S3 path is correct and the data is properly uploaded
