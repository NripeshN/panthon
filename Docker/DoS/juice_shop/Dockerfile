FROM node:20-buster as installer

# Install necessary packages
RUN apt-get update && apt-get install -y \
    binutils curl iproute2 iputils-ping nano net-tools unzip \
    arping conntrack dnsutils iptables mtr-tiny netcat openbsd-inetd \
    procps tcpdump telnet telnetd git bash wget build-essential python3 \
 && rm -rf /var/lib/apt/lists/*

# Clone and set up the Juice Shop application
RUN git clone --progress --recurse-submodules https://github.com/juice-shop/juice-shop.git --depth 1 /juice-shop
COPY . /juice-shop
WORKDIR /juice-shop
RUN npm install -g typescript ts-node \
 && npm install --omit=dev --unsafe-perm \
 && npm dedupe \
 && rm -rf frontend/node_modules frontend/.angular frontend/src/assets \
 && mkdir logs && chown -R 65532 logs && chgrp -R 0 ftp/ frontend/dist/ logs/ data/ i18n/ \
 && chmod -R g=u ftp/ frontend/dist/ logs/ data/ i18n/ \
 && rm -f data/chatbot/botDefaultTrainingData.json ftp/legal.md i18n/*.json \
 && npm install -g @cyclonedx/cyclonedx-npm@latest \
 && npm run sbom

# Build libxmljs2 without errors
RUN rm -rf node_modules/libxmljs2/build \
 && cd node_modules/libxmljs2 \
 && npm run build

# User setup
RUN useradd -m -s /bin/bash seed \
 && echo "root:dees" | chpasswd \
 && echo "seed:dees" | chpasswd

COPY bashrc /home/seed/.bashrc
COPY bashrc /root/.bashrc

# Use distroless image for runtime
FROM gcr.io/distroless/nodejs20-debian11
COPY --from=installer --chown=65532:0 /juice-shop .
COPY --chown=65532:0 --from=installer /juice-shop/node_modules/libxmljs2 ./node_modules/libxmljs2
USER 65532
EXPOSE 3000
CMD ["/juice-shop/build/app.js"]
