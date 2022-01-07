#!/bin/bash

#image_name=centos8_dev
#iversion=1.1
image_name=engine_bamp_release
iversion=1.0

#dockfilename=Dockerfile.devel
dockerfile=Dockerfile.release


docker build -t ${image_name}:${iversion} -f ${dockerfile} . \
&& docker save -o ${image_name}_${iversion}.tar ${image_name}:${iversion}
