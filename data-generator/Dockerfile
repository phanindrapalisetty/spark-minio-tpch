FROM ubuntu:20.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install MinIO client
RUN curl https://dl.min.io/client/mc/release/linux-amd64/mc --output /usr/local/bin/mc && \
    chmod +x /usr/local/bin/mc

# Clone and build TPC-H dbgen
RUN git clone https://github.com/electrum/tpch-dbgen.git /tpch-dbgen && \
    cd /tpch-dbgen && \
    sed -i 's/^CC\s*=.*/CC = gcc/' makefile.suite && \
    sed -i 's/^DATABASE\s*=.*/DATABASE = ORACLE/' makefile.suite && \
    sed -i 's/^MACHINE\s*=.*/MACHINE = LINUX/' makefile.suite && \
    sed -i 's/^WORKLOAD\s*=.*/WORKLOAD = TPCH/' makefile.suite && \
    cp makefile.suite Makefile && \
    make

# Copy the script to generate and load data
COPY generate-and-load.sh /generate-and-load.sh
RUN chmod +x /generate-and-load.sh

ENTRYPOINT ["/generate-and-load.sh"]