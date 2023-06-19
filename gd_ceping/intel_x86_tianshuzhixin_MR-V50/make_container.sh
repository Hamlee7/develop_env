image_name=sxs_x86_tianshumr_env_baseline
version=1.0
#image_name=sxs_x86_t4_env_baseline
#version=v2.0
#image_name=sxs_x86_dcu_env_baseline_sid_lid:v1.0
#image_name=image.sourcefind.cn:5000/dcu/admin/base/dtk
#version=22.10.1-centos7.6-py39
#version=22.10.1-ubuntu22.04-py37-latest

#container_name=tit_dtk_server_centos
#container_name=tit_dtk_server_ubuntu
container_name=tit_tianshumr_server
host=/data3/testGD2023

docker run -it --net=host -v /lib/modules:/lib/modules --privileged --cap-add=ALL --pid=host --shm-size 32G --name=${container_name} -v ${host}:/engine ${image_name}:${version} /bin/bash
#docker run --device=/dev/kfd --device=/dev/dri -it --net=host --name=${container_name} -v ${host}:/engine ${image_name}:${version} /bin/bash

#watch -n 2 ixsmi
