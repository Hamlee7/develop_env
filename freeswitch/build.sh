#!/bin/bash

image_name="freeswitch"
iversion="3.0"
dockerfile="Dockerfile"

docker build -t ${image_name}:${iversion} -f ${dockerfile} . \
&& docker save -o freeswitch_${iversion}.tar ${image_name}:${iversion}
