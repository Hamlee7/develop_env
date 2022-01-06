#!/bin/bash

#base version: devtoolset-7-toolchain-centos7:latest
#base_name=devtoolset-7-toolchain-centos7

#latest version
image_name=centos8_dev
iversion=1.1

docker build -t ${image_name}:${iversion} .

#docker load -i ${base_name}.tar \
#&& docker build -t ${image_name}:${iversion} . \
#&& docker save -o ${image_name}_${iversion}.tar ${image_name}:${iversion} \
#&& docker run --rm -it -v /home/work/thinkit/gd/TitSpeechEngineServer:/demo/ --name ${image_name}_${iversion} ${image_name}:${iversion} bash
