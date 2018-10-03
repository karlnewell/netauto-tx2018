FROM ubuntu:18.04

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
 bash-completion \
 command-not-found \
 curl \
 git \
 locales \
 python \
 python-virtualenv \
 python-pip \
 python3 \
 python3-pip \
 python3-venv \
 wget
# && rm -rf /var/lib/apt/lists/*

RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

WORKDIR /opt/netauto-tx2018/
COPY . .
RUN pip install -r requirements.txt
 
ENTRYPOINT ["/bin/bash"]