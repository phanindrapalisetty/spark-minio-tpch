FROM bitnami/spark:3.4.0

USER root

# Install required packages
RUN apt-get update && apt-get install -y curl wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Add AWS S3 support for Spark
RUN wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.2/hadoop-aws-3.3.2.jar -P /opt/bitnami/spark/jars/ && \
    wget https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar -P /opt/bitnami/spark/jars/

# Add Iceberg dependencies
RUN wget https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-spark-runtime-3.4_2.12/1.3.1/iceberg-spark-runtime-3.4_2.12-1.3.1.jar -P /opt/bitnami/spark/jars/ && \
    wget https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-core/1.3.1/iceberg-core-1.3.1.jar -P /opt/bitnami/spark/jars/ && \
    wget https://repo1.maven.org/maven2/software/amazon/awssdk/bundle/2.20.18/bundle-2.20.18.jar -P /opt/bitnami/spark/jars/ && \
    wget https://repo1.maven.org/maven2/software/amazon/awssdk/url-connection-client/2.20.18/url-connection-client-2.20.18.jar -P /opt/bitnami/spark/jars/

# Create log directory with appropriate permissions
RUN mkdir -p /opt/bitnami/spark/logs && \
    chmod -R 777 /opt/bitnami/spark/logs

# Set environment variables for AWS credentials to ensure they're available in the container
ENV AWS_ACCESS_KEY_ID=minio
ENV AWS_SECRET_ACCESS_KEY=minio123

USER 1001

WORKDIR /opt/bitnami/spark