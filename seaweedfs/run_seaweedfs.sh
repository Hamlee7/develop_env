#!/bin/bash

# seaweedfs version >= 2.77
hostpath="/home/work/thinkit/docker_images/develop_env/seaweedfs"

# master 
# ip need real ip
# peers need all ip:port
docker run --rm -d --net=host --name weed-master chrislusf/seaweedfs master -ip=10.20.5.21 -peers=10.20.5.21:9333
#docker run --rm -d --net=host --name weed-master chrislusf/seaweedfs master -ip=10.20.5.21 -peers=10.20.5.21:9333,10.20.5.100:9333

# volume
# mserver just need one master ip
docker run -d --net=host --name weed-volume -v ${hostpath}/volume:/data chrislusf/seaweedfs volume -mserver=10.20.5.21:9333 -port=8080  -metricsPort=9325
#docker run --rm -d --net=host --name weed-volume -v ${hostpath}/volume:/data chrislusf/seaweedfs volume -mserver=10.20.5.21:9333 -port=8080  -metricsPort=9325

# filer
# mserver just need one master ip
# automatic find ohter filer
docker run --rm -d --net=host --name weed-filer -v ${hostpath}/filer:/data chrislusf/seaweedfs filer -master=10.20.5.21:9333 -metricsPort=9326

# mount
./weed mount -filer=10.20.5.21:8888 -dir=${hostpath}/mnt -filer.path=/
