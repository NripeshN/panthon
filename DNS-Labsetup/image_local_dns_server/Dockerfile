FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update  \
    && apt-get -y install  \
        binutils \
        curl   \
        iproute2  \
        iputils-ping \
        nano   \
        net-tools \
        dnsutils  \
        tcpdump   \
        bind9  \
        bind9utils \
     && rm -rf /var/lib/apt/lists/*

# Copy the configuration file for the local DNS server
COPY named.conf           /etc/bind/
COPY named.conf.options   /etc/bind/

CMD service named start && tail -f /dev/null 
