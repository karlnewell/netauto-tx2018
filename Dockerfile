FROM ubuntu:18.04

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
 bash-completion \
 command-not-found \
 curl \
 git \
 inetutils-ping \
 locales \
 nano \
 netcat-openbsd \
 python \
 python-virtualenv \
 python-pip \
 python3 \
 python3-pip \
 python3-venv \
 sudo \
 vim \
 wget
# && rm -rf /var/lib/apt/lists/*

RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

RUN adduser --disabled-password --gecos "" techex18
RUN adduser techex18 sudo
RUN echo "techex18 ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

WORKDIR /home/techex18/
COPY . .
RUN chown -Rh techex18:techex18 .
RUN pip install -r requirements.txt

USER techex18
 
#ENTRYPOINT ["/bin/bash"]
