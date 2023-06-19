FROM image.sourcefind.cn:5000/dcu/admin/base/dtk:22.10.1-centos7.6-py39

#ADD  CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo

RUN yum -y install wget \
 && yum -y install net-tools nc telnet \
 && yum -y install tmux \
 && yum -y install dos2unix \
 && yum -y install vim
VOLUME /engine/
#对外暴露的端口
EXPOSE 2777
#拷贝业务程序到相应的目录,需要根据实际情况修改
#COPY ./engine/ /engine/
#容器启动时默认执行的程序,需要根据实际情况修改
#COPY run_asr_chn.sh /run_asr_chn.sh
WORKDIR /engine
CMD sh run.sh
