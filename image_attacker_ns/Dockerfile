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

# Copy the configuration and zone files
COPY named.conf  zone_attacker32.com  zone_example.com  /etc/bind/

CMD service named start && tail -f /dev/null
