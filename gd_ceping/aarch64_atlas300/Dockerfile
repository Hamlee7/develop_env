FROM test:1.1
MAINTAINER Liting <liting@thinkit.cn>

LABEL \
    base.name="centos7-engine-devel" \
    base.version="1.0" \
    base.expose-port="2777"

#设置默认工作目录，如不存在则自动创建
WORKDIR  /engine

#对外开放TCP 2777端口
EXPOSE 2777

CMD ["/bin/bash","run.sh"]
