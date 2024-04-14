ARG base=amd64/ubuntu:22.04
FROM ${base}
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update  \
    && apt-get -y install  \
        build-essential \
        binutils \
        curl   \
        iproute2  \
        iputils-ping \
        nano   \
        net-tools \
        unzip \
        sudo \
        arping \
        conntrack \
        curl   \
        dnsutils  \
        iptables \
        mtr-tiny  \
        netcat \
        openbsd-inetd  \
        procps \
        tcpdump   \
        telnet \
        telnetd \
        git \
        curl \
        bash \
        wget \
        python3 \
        python3-pip \
     && rm -rf /var/lib/apt/lists/*

COPY get-pip3.py /tmp

RUN git clone --progress --recurse-submodules https://github.com/NripeshN/panthon --depth 1 /app/panthon

WORKDIR /app/panthon

RUN  python3 /tmp/get-pip3.py \
     && pip3 install scapy \
     && pip install -e . \
     && rm /tmp/get-pip3.py 

RUN  useradd -m -s /bin/bash seed \
     && echo "root:dees" | chpasswd \
     && echo "seed:dees" | chpasswd

COPY bashrc /home/seed/.bashrc
COPY bashrc /root/.bashrc

CMD /bin/bash
