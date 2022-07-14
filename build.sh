#!/bin/bash

#image_name=centos8_dev
#iversion=1.1
image_name=engine_uniform_dev
iversion=1.1

#dockfilename=Dockerfile.devel
#dockerfile=Dockerfile.release
dockerfile=Dockerfile.uniform


docker build -t ${image_name}:${iversion} -f ${dockerfile} . \
&& docker save -o ${image_name}_${iversion}.tar ${image_name}:${iversion}
