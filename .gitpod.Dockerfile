FROM gitpod/workspace-full

USER root

RUN apt-get update \
    && apt-get install -y python3 python3-dev python3-pip \
    && apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*

RUN  update-alternatives --install /usr/bin/python python /usr/bin/python3 1
    #ln -s /usr/bin/python3 /usr/bin/python && \
    #ln -s /usr/bin/pip3 /usr/bin/pip

RUN pip3 install \
    python-language-server \
    flake8 \
    autopep8 \
    futures \
    configparser \
    rope \
    pydocstyle \
    yapf
