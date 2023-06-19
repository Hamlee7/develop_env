image_name=image.sourcefind.cn:5000/dcu/admin/base/dtk
version=22.10.1-centos7.6-py39

container_name=tit_dtk_server_centos
host=/data1/testGD2023

docker run --device=/dev/kfd --device=/dev/dri -it --net=host --name=${container_name} -v ${host}:/engine ${image_name}:${version} /bin/bash


# watch -n 1 hy-smi
# watch -n 1 rocm-smi
