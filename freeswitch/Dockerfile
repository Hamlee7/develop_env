FROM centos:7

# 设置时区
ENV TZ=Asia/Shanghai
#RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Base deps
RUN yum -y --setopt=install_weak_deps=false --setopt=tsflags=nodocs --setopt=override_install_langs=en_US.utf8 install \
    epel-release gcc gcc-c++ swig lua-devel \
    python-devel python-pip \
    https://files.freeswitch.org/repo/yum/centos-release/freeswitch-release-repo-0-1.noarch.rpm \
    && yum install -y luarocks freeswitch-config-vanilla \
#&& yum install -y freeswitch-config-vanilla freeswitch-lang-en* freeswitch-sounds-en* \
    && yum clean all && rm -fR /var/cache/yum \
    && pip install python-ESL requests\
    && luarocks install luasocket lua-cjson\
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# COPY source dest better than ADD source dest
COPY sounds scripts /usr/share/freeswitch/ \
    && COPY entrypoint.sh /

# WORKDIR /src

# EXPOSE 8080

# USER daemon

#HEALTHCHECK --interval=15s --timeout=5s CMD  /healthcheck.sh

# 使用exec格式的 ENTRYPOINT指令 设置固定的默认命令和参数
# ENTRYPOINT ["/bin/bash", "-c", "tail", "-f", "/dev/null"]
ENTRYPOINT ["/entrypoint.sh"]
#ENTRYPOINT ["freeswitch", "-c", "-nc", "nonat"]

# 使用 CMD指令 设置可变的参数
# CMD [ "executable" ]
