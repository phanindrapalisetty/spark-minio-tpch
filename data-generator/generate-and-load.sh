#!/bin/bash
set -e

cd /tpch-dbgen

# Generate TPC-H data (scale factor 1 = 1GB)
./dbgen -s 1

echo "TPC-H data generation completed!"

# Configure MinIO client and create bucket if not exists
mc alias set myminio http://minio:9000 minio minio123

# Upload data to MinIO
echo "Uploading TPC-H data to MinIO..."
mc cp *.tbl myminio/tpch/

echo "Data upload completed!"

# Keep the container running for debugging if needed
tail -f /dev/null