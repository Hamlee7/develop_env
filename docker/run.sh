#!/bin/bash

image_name=centos8_dev
iversion=1.1

host_path=/home/work/thinkit/service_engine/TitAudioProcessingEngines
container_path=/thinkit/TitAudioProcessingEngines

container_expose_port=8901

container_hostname='thinkit00 '


docker run --rm -it -p ${container_expose_port}:8900 -v /home/haorp/docker/vcpkg:/engine/docker/vcpkg -v ${host_path}:${container_path} --name lit_${image_name}_${iversion} ${image_name}:${iversion} bash

#docker run --rm -it -p ${container_expose_port} -h ${container_hostname} -v /home/haorp/docker/vcpkg:/engine/docker/vcpkg -v ${host_path}:${container_path} --name lit_${image_name}_${iversion} ${image_name}:${iversion} bash

#docker run --rm -it -v /home/work/thinkit/gd/TitSpeechEngineServer:/demo/ --name ${image_name}_${iversion} ${image_name}:${iversion} bash

#docker run --rm --privileged -it -h thinkit00 -v ${host_path}:${container_path} --name lit_${image_name}_${iversion} ${image_name}:${iversion} bash
