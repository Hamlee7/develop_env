#!/bin/bash

docker run --rm -it -p 2776:2777 -v /data/gz_GA_server/engine:/engine --name=lit portus.teligen.com:5000/sxs-cp/xc-arm-devel:1.1 /bin/bash

#docker run --rm -it -p 2777:2777 --cap-add LINUX_IMMUTABLE --device=/dev/davinci0 --device=/dev/davinci1 --device=/dev/davinci2 --device=/dev/davinci3 --device=/dev/davinci_manager --device=/dev/devmm_svm --device=/dev/hisi_hdc -v /data/guoyutong/engine:/engine --name=lit portus.teligen.com:5000/sxs-cp/xc-arm-devel:1.1 /bin/bash

#docker run --rm -it -p 2778:2777 --cap-add LINUX_IMMUTABLE -e ASCEND_VISIBLE_DEVICES=0,1,2,4 --device=/dev/davinci_manager --device=/dev/devmm_svm --device=/dev/hisi_hdc -v /data/guoyutong/engine:/engine --name=lit portus.teligen.com:5000/sxs-cp/xc-arm-devel:1.1 /bin/bash

#docker run --rm -it -p 2778:2777 --cap-add LINUX_IMMUTABLE -e ASCEND_VISIBLE_DEVICES=0,1,2,4 -v /data/guoyutong/engine:/engine --name=lit portus.teligen.com:5000/sxs-cp/xc-arm-devel:1.1 /bin/bash

#docker run --rm -it -p 2778:2777 --cap-add LINUX_IMMUTABLE --device=/dev/davinci0 --device=/dev/davinci1 --device=/dev/davinci2 --device=/dev/davinci3 --device=/dev/davinci_manager --device=/dev/devmm_svm --device=/dev/hisi_hdc -v /data/guoyutong/engine:/engine --name=lit portus.teligen.com:5000/sxs-cp/xc-arm-devel:1.1 /bin/bash

#docker run --rm -it -p 2778:2777 --cap-add LINUX_IMMUTABLE --device=/dev/davinci0 --device=/dev/davinci1 --device=/dev/davinci2 --device=/dev/davinci3 --device=/dev/davinci_manager --device=/dev/devmm_svm --device=/dev/hisi_hdc -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi -v /usr/local/Ascend/:/usr/local/Ascend/ -v /data/guoyutong/engine:/engine --name=lit portus.teligen.com:5000/sxs-cp/xc-arm-devel:1.0 /bin/bash

#docker run --rm -it -p 2777:2777 --cap-add LINUX_IMMUTABLE --device=/dev/davinci0 --device=/dev/davinci1 --device=/dev/davinci2 --device=/dev/davinci3 --device=/dev/davinci_manager --device=/dev/devmm_svm --device=/dev/hisi_hdc -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi -v /usr/local/Ascend/:/usr/local/Ascend/ -v /data/guoyutong/engine:/engine --name=litTest test:1.2 /bin/bash

#docker run --rm -it -p 2777:2777 --cap-add LINUX_IMMUTABLE --device=/dev/davinci2 --device=/dev/davinci3 --device=/dev/davinci_manager --device=/dev/devmm_svm --device=/dev/hisi_hdc -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi -v /usr/local/Ascend/:/usr/local/Ascend/ -v /data/guoyutong/engine:/engine --name=lit centos7-engine-devel:1.0 /bin/bash

#docker run --rm -d -p 2777:2777 --cap-add LINUX_IMMUTABLE --device=/dev/davinci2 --device=/dev/davinci3 --device=/dev/davinci_manager --device=/dev/devmm_svm --device=/dev/hisi_hdc -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi -v /usr/local/Ascend/:/usr/local/Ascend/ -v /data/guoyutong/engine:/engine --name=lit centos7-engine-devel:1.0 /bin/bash

#docker run -it --cap-add LINUX_IMMUTABLE --device=/dev/davinci2 --device=/dev/davinci3 --device=/dev/davinci_manager --device=/dev/devmm_svm --device=/dev/hisi_hdc -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi -v /usr/local/Ascend/:/usr/local/Ascend/ -v /data/guoyutong/engine:/engine --name lit centos7-engine-devel:1.0 /bin/bash
#docker run -it -p 2777:2777 --cap-add LINUX_IMMUTABLE --device=/dev/davinci1 --device=/dev/davinci0 --device=/dev/davinci_manager --device=/dev/devmm_svm --device=/dev/hisi_hdc -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi -v /usr/local/Ascend/:/usr/local/Ascend/ -v /data/guoyutong/engine:/engine --name lit test:1.1 /bin/bash

#docker run -it --cap-add LINUX_IMMUTABLE --device=/dev/davinci2 --device=/dev/davinci3 --device=/dev/davinci_manager --device=/dev/devmm_svm --device=/dev/hisi_hdc -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi -v /usr/local/Ascend/:/usr/local/Ascend/ -v /data/guoyutong/engine:/engine  test:1.1 ./run.sh

#docker run -it --cap-add LINUX_IMMUTABLE --device=/dev/davinci2 --device=/dev/davinci3 --device=/dev/davinci_manager --device=/dev/devmm_svm --device=/dev/hisi_hdc -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi -v /usr/local/Ascend/:/usr/local/Ascend/ -v /data/guoyutong/engine:/engine  test:1.1 /engine/run.sh
