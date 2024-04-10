ARG base=amd64/ubuntu:20.04
FROM ${base}
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update  \
    && apt-get -y install  \
        binutils \
        curl   \
        iproute2  \
        iputils-ping \
        nano   \
        net-tools \
        unzip \
        arping \
        conntrack \
        dnsutils  \
        iptables \
        mtr-tiny  \
        netcat \
        openbsd-inetd  \
        procps \
        tcpdump   \
        telnet \
        telnetd \
        libexpat1-dev \
        python3.8-dev \
        python3.8-distutils \
        git \ 
     && rm -rf /var/lib/apt/lists/*

# Clone the panthon repository from GitHub
RUN git clone --progress --recurse-submodules https://github.com/NripeshN/panthon --depth 1 /app/panthon

WORKDIR /app/panthon

# Install pip and set up a virtual environment
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
     && python3.8 get-pip.py \
     && python3.8 -m pip install virtualenv \
     && python3.8 -m virtualenv venv \
     && . venv/bin/activate \
     && pip install -e .

# Copy the configuration and zone files
COPY named.conf  zone_attacker32.com  zone_example.com  /etc/bind/

CMD service named start && tail -f /dev/null
