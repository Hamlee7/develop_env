#!/bin/bash

image_name=centos8_dev
iversion=1.1

container_name=lit_dev_env
new_container_name=lit_${image_name}_${iversion}

#author=lit
#commit='add cmake protoc grpc and so on for dev_env_demo'

#docker commit -m "${commit}" ${container_name} ${image_name}:${iversion}
#echo "finished commit image"
#docker save -o ${image_name}_${iversion}.tar ${image_name}:${iversion}
#echo "finished saving image"
#docker load -i ${image_name}_${iversion}.tar
#echo "finished loading image"


#docker export ${container_name} -o ${image_name}_${iversion}.tar
#echo "finished export image"
docker import ${image_name}_${iversion}.tar ${new_container_name}
echo "finished import image"


#docker run --rm -it -v /home/work/thinkit/gd/TitSpeechEngineServer:/demo/ --name ${new_container_name} ${image_name}:${iversion} bash
#docker run --privileged --rm -it -v /home/work/thinkit/docker_images/demo:/opt/deps/demo --name ${new_container_name} ${image_name}:${iversion} bash
