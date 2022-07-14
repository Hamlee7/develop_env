#!/bin/bash

image_name="freeswitch"
iversion="1.0"

docker run --rm -d --net=host --name freeswitch \
        ${image_name}:${iversion}
docker exec -it freeswitch bash

#docker run -d --net=host --name freeswitch \
#        -e SOUND_RATES=8000:16000 \
 #       -e SOUND_TYPES=music:en-us-callie \
  #      -v freeswitch-sounds:/usr/share/freeswitch/sounds \
   #     -v /etc/freeswitch/:/etc/freeswitch \
    #    safarov/freeswitch
#docker run --rm -dit -p ${container_expose_port}:8900 --name lit_${image_name}_${iversion} ${image_name}:${iversion} bash
#docker run --rm -it -p ${container_expose_port}:8900 -v /home/haorp/docker/vcpkg:/engine/docker/vcpkg -v ${host_path}:${container_path} --name lit_${image_name}_${iversion} ${image_name}:${iversion} bash
