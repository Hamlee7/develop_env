FROM centos:latest

ARG LITDEV_VERSION=3.0

# 切换root权限
#USER 0

# 设置时区
ENV TZ=Asia/Shanghai

# Base deps
RUN yum -y --setopt=install_weak_deps=false --setopt=tsflags=nodocs --setopt=override_install_langs=en_US.utf8 install \
    autoconf \
    automake \
    gcc \
    gcc-c++ \
    gdb \
    git \
    make \
    libssh \
    libtool \
    openssl \
    openssl-libs \
    openssh \
    openssh-clients \
    python3 \
    python3-pip \
    vim \
    wget \
    zlib \
    && ln -s /usr/lib64/libz.so.1.2.11 /usr/lib64/libz.so \
    && yum clean all && rm -fR /var/cache/yum \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Source install tools
RUN mkdir -p /opt/deps/ && cd /opt/deps/ \
    # cmake
    # RUN mkdir -p ./cmake/ && pushd ./cmake/ && wget https://gitlab.kitware.com/cmake/cmake/-/archive/v3.20.6/cmake-v3.20.6.tar.gz && tar zvxf cmake-v3.20.6.tar.gz && cd cmake-v3.20.6/ && ./bootstrap && make && sudo make install && popd && rm -rf ./cmake
    && mkdir -p ./cmake && pushd ./cmake && wget -q -O cmake-linux.sh https://github.com/Kitware/CMake/releases/download/v3.19.6/cmake-3.19.6-Linux-x86_64.sh && sh cmake-linux.sh -- --skip-license --prefix=/usr/local && rm cmake-linux.sh && popd && rm -rf ./cmake
    #&& scl enable devtoolset-7 bash
    # protoc
    #&& mkdir -p ./protoc && pushd ./protoc && wget https://github.com/protocolbuffers/protobuf/releases/download/v3.11.2/protobuf-all-3.11.2.tar.gz && tar zvxf protobuf-all-3.11.2.tar.gz && cd protobuf-3.11.2/ && ./autogen.sh && ./configure -prefix=/usr/local/ && make -j 8 && make install && popd && rm -rf ./protoc \
    # grpc
    #&& mkdir -p ./grpc && pushd ./grpc && git clone --recurse-submodules -b v1.41.0 https://github.com/grpc/grpc ; cd grpc && mkdir -p cmake/build && pushd cmake/build && cmake -DgRPC_INSTALL=ON \
    #  -DgRPC_BUILD_TESTS=OFF \
    #  -DCMAKE_INSTALL_PREFIX=/usr/local \
    #  ../.. && make -j 8 && make install && popd \
    #  && popd && rm -rf ./grpc


# CentOS
# ENV TZ=Asia/Shanghai
# RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# COPY source dest better than ADD source dest

# WORKDIR /src

# EXPOSE 8080

# USER daemon

# 使用exec格式的 ENTRYPOINT指令 设置固定的默认命令和参数
# ENTRYPOINT ["/bin/bash", "-c", "tail", "-f", "/dev/null"]
# 使用 CMD指令 设置可变的参数
# CMD [ "executable" ]
