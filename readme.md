# My research and development
禅道录入4/5个任务列表记工时（2小时/个）:

ToDoList:
kt-lib:master分支代码剥离打包
kdm-意图识别(诺谛大模型)
kdm-语音识别asr
kdm-语音合成tts
kdm-敏感词识别(诺谛大模型)
kdm-文本分词向量化模型
消息订阅/回调机制(grpc,ws,dbus,mqtt)
扩展能力sysfunc(网络WIFI、应用商店)

// 设计原则：
//   安全质量
//   好用灵活
//   折中


9月13日前计划:
完成语音ASR/TTS功能开发并沉淀为KDM		需完成模块设计以及功能开发落地	50%	输出完整KDM并上线使用	9月13日	AIPC端服务概要设计
完成端上意图识别改造并沉淀为KDM			完成KDM改造并沉淀为通用依赖	20%	输出完整KDM并上线使用	9月13日	AIPC端服务概要设计
完成端上敏感词识别KDM改造并沉淀为KDM		完成KDM改造并沉淀为通用依赖	20%	输出完整KDM并上线使用	9月13日	AIPC端服务概要设计
完成两个第三方库的KDM落地					完成KDM改造并沉淀为通用依赖	10%	输出完整KDM并上线使用	9月13日	AIPC端服务概要设计

联想开天负责人徐江萍(辉煌国际A座701)
无线WIFI:Lenovokt

1、调研MQTT
2、第三方如何使用kt-lib的grpc服务能力（intent、senword、llm、doc parse、pkg）


vcpkg bin url:
https://github.com/microsoft/vcpkg-tool/releases/download/2024-01-11/vcpkg-glibc
https://github.com/microsoft/vcpkg-tool/releases/download/2024-08-01/vcpkg-glibc



排查logger模块创建日志目录失败
寻求讯飞技术支持，定位授权签名不合法问题
编写KDM ASR工程README.md
编写KDM ASR API功能说明
编写KDM ASR设计说明






kd-asr-proxy
rtp端口号范围太小时，服务启动log提示端口配置不合理并自动退出
(max-min)/4 < 1



线上测试kd-asr-proxy镜像5.0版本，定位http超时问题
修改sysfunc中intent调用流程与逻辑，因抽槽模块更新，sysfunc解析槽位信息无法兼容

mrcp和freeswitch



设计修改sysfunc/intent2
并发应用安装存在"其他任务正在更新升级中，请稍后再试。"问题





设计sysfunc语义路由模块semantic_router
开发数据库db_keeper模块








<!-- ---
技术方案调研及评估
- Speech Denoise
  - [ClearerVoice-Studio](https://stable-learn.com/zh/clearvoice-studio-tutorial)

  - VoiceBank + DEMAND (Noisy speech database for training speech enhancement algorithms and TTS models):https://paperswithcode.com/dataset/demand

  - DNS Challenge (Deep Noise Suppression Challenge):https://paperswithcode.com/dataset/deep-noise-suppression-2020

关于实时降噪功能，目前讯飞开放平台的实时语音转写产品不支持降噪功能。如果您需要降噪相关的解决方案，建议您考虑使用双麦克风阵列开发套件或模块，它们基于科大讯飞双麦阵列算法设计，提供降噪功能，适用于智能硬件设备。您可以访问以下链接了解更多信息：
[双麦克风阵列开发套件与模块介绍](https://www.xfyun.cn/services/rtasr)


speech enhance
enhancement
speech denoise

- 实时降噪
 - based on real time or stream speech denoise，有哪些开源技术算法

在实时或流式语音降噪领域，有许多开源技术和算法可供使用。这些技术通常利用信号处理和机器学习方法来减少背景噪音，提高语音信号的清晰度。以下是一些常见的开源技术和算法：
RNNoise：
由Xiph.org基金会开发，结合了经典信号处理和深度学习技术。RNNoise是一个轻量级的实时语音降噪库，适用于低延迟应用。
Speex DSP：
Speex项目的一部分，提供了多种音频处理功能，包括回声消除、噪声抑制和自动增益控制。适用于实时音频处理。
DeepFilterNet：
基于深度学习的语音降噪模型，专注于实时应用。它利用神经网络来预测和抑制噪音。
Noisereduce：
一个基于Python的库，使用频谱减法和其他信号处理技术来实现降噪。虽然主要用于离线处理，但可以调整用于实时应用。
Wavesplit：
使用深度学习技术进行语音分离和降噪，适用于实时和离线应用。
OpenSMILE：
虽然主要用于音频特征提取，但也包含一些基本的信号处理功能，可以用于降噪。
Pyroomacoustics：
提供了一些用于房间声学仿真和信号处理的工具，包括噪声抑制算法。
这些开源技术和算法各有优缺点，选择时可以根据具体的应用场景、实时性要求和计算资源来决定。通常，结合多种技术可以获得更好的降噪效果。

 - based on real time or stream speech enhance，有哪些开源技术算法

在实时或流式语音增强领域，有许多开源技术和算法可供使用。这些技术通常结合信号处理和深度学习方法，以提高语音信号的质量和可懂度。以下是一些常见的开源技术和算法：
RNNoise：
由Xiph.org基金会开发，结合经典信号处理和深度学习技术。RNNoise不仅用于降噪，也能在一定程度上增强语音信号。
DeepFilterNet：
基于深度学习的语音增强模型，专注于实时应用。它利用神经网络来增强语音信号的质量。
Speex DSP：
Speex项目的一部分，提供了多种音频处理功能，包括回声消除、噪声抑制和自动增益控制，适用于实时音频增强。
VoiceFixer：
一个基于深度学习的工具，用于修复和增强语音信号，适用于实时和离线应用。
AUDIO-DK：
提供了一些用于音频信号处理的工具和算法，包括语音增强功能。
Pyroomacoustics：
提供了一些用于房间声学仿真和信号处理的工具，可以用于语音增强。
SEGAN (Speech Enhancement Generative Adversarial Network)：
使用生成对抗网络（GAN）进行语音增强，适用于实时和离线应用。
Wave-U-Net：
基于U-Net架构的语音增强模型，适用于实时应用。
这些开源技术和算法各有优缺点，选择时可以根据具体的应用场景、实时性要求和计算资源来决定。通常，结合多种技术可以获得更好的语音增强效果。



- do vad_lenovo with enable_noise
- do de with stream/real time
--- -->

1、讯飞API不支持实时降噪功能
2、声学所实时降噪，需提供典型应用场景样本语音，用于分析评估效果


- 20250314
编写DE&VAD技术方案调研及评估结果
调研开源实时降噪算法
沟通声学所实时降噪技术方案
调研讯飞流式实时TTS API



<!--
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
taming-transformers-rom1504 0.0.6 requires pytorch-lightning>=1.0.8, which is not installed.
xtuner 0.1.23 requires bitsandbytes>=0.40.0.post4, which is not installed.
xtuner 0.1.23 requires lagent>=0.1.2, which is not installed.
xtuner 0.1.23 requires mmengine>=0.10.3, which is not installed.
easyrobust 0.2.4 requires timm==0.5.4, but you have timm 1.0.12 which is incompatible.
fairseq 0.12.2 requires hydra-core<1.1,>=1.0.7, but you have hydra-core 1.3.2 which is incompatible.
fairseq 0.12.2 requires omegaconf<2.1, but you have omegaconf 2.3.0 which is incompatible.
funcodec 0.2.0 requires typeguard==2.13.3, but you have typeguard 4.3.0 which is incompatible.
pai-easycv 0.11.6 requires timm==0.5.4, but you have timm 1.0.12 which is incompatible. -->





## DE&VAD技术方案调研及评估

|  技术分类  |  技术方案  |  评估效果  |  测试详情  |  语音case详情  |  非实时DE处理  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|  vad  |  vad_rtc  |  2/6  |  2句人声(丢首字) + 4句噪音  |  2句有效人声  |  否  |
|  vad  |  vad_lenovo  |  2/22  |  3句人声 + 19句噪音  |  2句有效人声  |  否  |
|  vad  |  vad_ali  |  2/30  |  3句人声(弱降噪) + 27句噪音  |  2句有效人声  |  否  |
|  de&vad  |  de_vad_rtc  |  2/3  |  3句人声(丢首字)  |  2句有效人声  |  是  |
|  de&vad  |  de_vad_lenovo  |  2/4  |  3句人声 + 1句噪音  |  2句有效人声  |  是  |
|  de&vad  |  de_vad_ali  |  2/3  |  3句人声  |  2句有效人声  |  是  |




- 20250313
调研讯飞API降噪和开源语音降噪算法
测试并评估降噪+vad_rtc方案效果
测试并评估降噪+vad_lenovo方案效果
测试并评估降噪+vad_fsmn方案效果


<!--
计算机四级网络工程师
华为HCIA-AI V3.0
-->

- 20250312
调试asr-proxy测试程序，排查解决vad分段结果信息异常丢失问题
修改asr-proxy测试程序，落地vad分段结果语音
修改fsmn-vad测试程序，落地vad分段结果语音
参加语音机器人问题分类会议


- 20250311
分析asr-proxy模块vad接口libmfe_JNI
分析asr-proxy模块lenovoVadInst
分析asr-proxy模块recoProxy_vad、recoProxy
修改测试程序，添加vad分段结果信息

void recoProxy::processVadRes(unsigned char * pData, int iLen, vadVars* pVars)


LOG (mfeInit():vad_04/libmfe_JNI.cc:136) MFE_Init with SampleRate=16000
VLOG[1] (MFE_Init():feat/front-end.cc:71) dither=0, subband_type=0, debug=0
VLOG[1] (MFE_Init():feat/front-end.cc:100) Using linear PCM, encode frame size = 160, decoder frame size = 160


ret is
3050

ret is 0
248

ret is 1
2657

ret is 2
143

ret is 3
2



- slicence
Get Data 0xa2b830, Len:640
Create Data 0xa2b560 iLen=640
ret is 0
T: 2 -> mfeDetect return: 0
var->_iIsEnd = 0
Free data 0xa2b830
Feed Data 0xa28920, Len:640


- speech but without begin and end
Get Data 0xa2a270, Len:640
Create Data 0xa29fa0 iLen=640
ret is 1
T: 1 -> mfeDetect return: 1
var->_iIsEnd = 0
start to output data
start to output data
Free data 0xa2a270
Feed Data 0xa28650, Len:640



- noise audio
Get Data 0xa28bb0, Len:640
Create Data 0xa28610 iLen=640
ret is 2
T: 2 -> mfeDetect return: 2
var->_iIsEnd = 0
Free data 0xa28bb0
Feed Data 0xa28e80, Len:640







- begin of speech:6(mfeDetect:0->1, 2->1)
Get Data 0xa2adb0, Len:640
Create Data 0xa2aae0 iLen=640
ret is 0
T: 1 -> mfeDetect return: 0
var->_iIsEnd = 0
Free data 0xa2adb0
Feed Data 0xa29730, Len:640
Get Data 0xa29730, Len:640
Create Data 0xa2adb0 iLen=640
ret is 1
T: 1 -> mfeDetect return: 1
T: 1 -> detected begin of speech. ret: 1
var->_iIsEnd = 0
start to output data
start to output data
start to output data
Free data 0xa29730
Feed Data 0xa2b080, Len:640
Get Data 0xa2b080, Len:640
Create Data 0xa29730 iLen=640
ret is 1
T: 1 -> mfeDetect return: 1
var->_iIsEnd = 0
start to output data
start to output data
Free data 0xa2b080
Feed Data 0xa2b350, Len:640

Get Data 0xa28920, Len:640
Create Data 0xa2b830 iLen=640
ret is 2
T: 2 -> mfeDetect return: 2
var->_iIsEnd = 0
Free data 0xa28920
Feed Data 0xa29730, Len:640
Get Data 0xa29730, Len:640
Create Data 0xa28920 iLen=640
ret is 1
T: 2 -> mfeDetect return: 1
T: 2 -> detected begin of speech. ret: 1
var->_iIsEnd = 0
start to output data
start to output data
start to output data
Free data 0xa29730
Feed Data 0xa29190, Len:640
Get Data 0xa29190, Len:640
Create Data 0xa29730 iLen=640
ret is 1
T: 2 -> mfeDetect return: 1
var->_iIsEnd = 0
start to output data
start to output data
Free data 0xa29190
Feed Data 0xa29460, Len:640



- end of speech:6(mfeDetect:1->2, 1->3)
Get Data 0x19e7f10, Len:640
ret is 1
T: 0 -> mfeDetect return: 1
var->_iIsEnd = 0
start to output data,len = 640
start to output data,len = 0
Free data 0x19e7f10
Feed Data 0x19e81e0, Len:640
Get Data 0x19e81e0, Len:640
ret is 3
T: 0 -> mfeDetect return: 3
T: 1 -> detected end of speech. ret: 3
var->_iIsEnd = 1
Free data 0x19e81e0
Feed Data 0x19e84b0, Len:640
Get Data 0x19e84b0, Len:640
ret is 0
T: 1 -> mfeDetect return: 0
var->_iIsEnd = 0
Free data 0x19e84b0
Feed Data 0x19e8780, Len:640

Get Data 0xa2acf0, Len:640
Create Data 0xa2aa40 iLen=640
ret is 1
T: 2 -> mfeDetect return: 1
var->_iIsEnd = 0
start to output data
start to output data
Free data 0xa2acf0
Feed Data 0xa2afc0, Len:640
Get Data 0xa2afc0, Len:640
Create Data 0xa2acf0 iLen=640
ret is 2
T: 2 -> mfeDetect return: 2
T: 2 -> detected end of speech. ret: 2
var->_iIsEnd = 1
Free data 0xa2afc0
Feed Data 0xa2b290, Len:640
Get Data 0xa2b290, Len:640
Create Data 0xa2afc0 iLen=640
ret is 2
T: 2 -> mfeDetect return: 2
var->_iIsEnd = 0
Free data 0xa2b290
Feed Data 0xa2b560, Len:640





Get Data 0xa2b350, Len:640
Create Data 0xa2b080 iLen=640
ret is 0
T: 0 -> mfeDetect return: 0
var->_iIsEnd = 0
Free data 0xa2b350
Feed Data 0xa2b620, Len:640
Get Data 0xa2b620, Len:640
Create Data 0xa2b350 iLen=640
ret is 3
T: 0 -> mfeDetect return: 3
var->_iIsEnd = 0
Free data 0xa2b620
Feed Data 0xa27b10, Len:640
Get Data 0xa27b10, Len:640
ret is 0
T: 1 -> mfeDetect return: 0
var->_iIsEnd = 0
Free data 0xa27b10
Feed Data 0xa27de0, Len:640





LOG (mfeInit():vad_04/libmfe_JNI.cc:136) MFE_Init with SampleRate=8000
VLOG[1] (MFE_Init():feat/front-end.cc:71) dither=0, subband_type=0, debug=0
VLOG[1] (MFE_Init():feat/front-end.cc:100) Using linear PCM, encode frame size = 80, decoder frame size = 80
Buffer initialized 0x19e2320
vadInst buffer is 0x19e2050
wav file length = 81218 Byte
buf is , iLen=1
Create Data 0x19e7f10 iLen=640
Create Data 0x19e81e0 iLen=640






[root@centos7 bin]# sh run.sh
==========1
Main Pointer 0x7ffff97a250c
[kd-mrcp-asr] recoProxy::recoProxy >>>>>> in
[kd-mrcp-asr] rreporter create pUuid = noise_87f37c.pcm
[kd-mrcp-asr] createVadCbUtil
[kd-mrcp-asr] recoProxyCreateVad >>>>>> RECO_VAD_LENOVO
[kd-mrcp-asr] recoProxy::recoProxy >>>>>> RECO_ASR_LENOVO
[kd-mrcp-asr] recoProxyInitVad
[kd-mrcp-asr] lenovoVadInst::init vad iVadEnergyStart = 70
[kd-mrcp-asr] lenovoVadInst::init iVadEnergeStop = 40
[kd-mrcp-asr] lenovoVadInst::init iVoicePoint = 100
[kd-mrcp-asr] lenovoVadInst::init iLRelax = 25
[kd-mrcp-asr] lenovoVadInst::init iRRelax = 30
[kd-mrcp-asr] lenovoVadInst::init iMinSpDuration = 15
[kd-mrcp-asr] lenovoVadInst::init iMaxSpDuration = 100000
[kd-mrcp-asr] lenovoVadInst::init iSleepTimeout = 6000
[kd-mrcp-asr] lenovoVadInst::init iMaxSpPause = 500 ms, iLRelax = 250 ms
LOG (mfeInit():vad/libmfe_JNI.cc:225) MFE_Init with SampleRate=8000
VLOG[1] (MFE_Init():feat/front-end.cc:71) dither=0, subband_type=0, debug=0
VLOG[1] (MFE_Init():feat/front-end.cc:100) Using linear PCM, encode frame size = 80, decoder frame size = 80
[kd-spdlog][reco] init success m_logger_ = 0x7f567620a980
[kd-mrcp-asr] recoProxy::recoProxy >>>>>> out
==========2
[kd-mrcp-asr] recoProxySetVadIntParam type = 0, value = 1
[kd-mrcp-asr] recoProxySetVadIntParam type = 1, value = 300
wav file length = 1483200 Byte
Catch noinput at 5120 ms, elapsed 320 ms
[kd-mrcp-asr] lenovoAsrInst::sendFirstMsg
CreateMsg Index = 0, point = 0x7f5668000b30
[kd-mrcp-asr] rreporter::createSocketCon socketConnection url = 10.110.147.191:7070
[kd-mrcp-asr] recoProxyCloseVad
asr connect error:Connection timed out
asr connect error:Connection timed out
[kd-mrcp-asr] recoProxy::openDbgFile filename: /tmp/vad//noise_87f37c.pcm_0000.wav
[kd-mrcp-asr] recoProxy::processVadRes VAD END
[kd-mrcp-asr] rreporter::sendMsg 3 FRAME_LAST
[kd-mrcp-asr] socketConnection::sendMsg 2 VAD END, sessionId = noise_87f37c.pcm, traceId = 1d3fb216-cd84-4609-8cf7-809e0e25cda2, time = 2025-03-12 03:13:00:950875
[kd-mrcp-asr] lenovoAsrInst::sendFirstMsg
CreateMsg Index = 1, point = 0x7f56680010a0
[kd-mrcp-asr] rreporter::createSocketCon socketConnection url = 10.110.147.191:7070

[root@centos7 bin]# sh run.sh
==========1
Main Pointer 0x7fff0fda1b7c
[kd-mrcp-asr] recoProxy::recoProxy >>>>>> in
[kd-mrcp-asr] rreporter create pUuid = test222
[kd-mrcp-asr] createVadCbUtil
[kd-mrcp-asr] recoProxyCreateVad >>>>>> RECO_VAD_LENOVO
[kd-mrcp-asr] recoProxy::recoProxy >>>>>> RECO_ASR_LENOVO
[kd-mrcp-asr] recoProxyInitVad
[kd-mrcp-asr] lenovoVadInst::init vad iVadEnergyStart = 70
[kd-mrcp-asr] lenovoVadInst::init iVadEnergeStop = 40
[kd-mrcp-asr] lenovoVadInst::init iVoicePoint = 100
[kd-mrcp-asr] lenovoVadInst::init iLRelax = 25
[kd-mrcp-asr] lenovoVadInst::init iRRelax = 30
[kd-mrcp-asr] lenovoVadInst::init iMinSpDuration = 15
[kd-mrcp-asr] lenovoVadInst::init iMaxSpDuration = 100000
[kd-mrcp-asr] lenovoVadInst::init iSleepTimeout = 6000
[kd-mrcp-asr] lenovoVadInst::init iMaxSpPause = 500 ms, iLRelax = 250 ms
LOG (mfeInit():vad/libmfe_JNI.cc:225) MFE_Init with SampleRate=8000
VLOG[1] (MFE_Init():feat/front-end.cc:71) dither=0, subband_type=0, debug=0
VLOG[1] (MFE_Init():feat/front-end.cc:100) Using linear PCM, encode frame size = 80, decoder frame size = 80
[kd-spdlog][reco] init success m_logger_ = 0x7f0d1e5d1960
[kd-mrcp-asr] recoProxy::recoProxy >>>>>> out
==========2
[kd-mrcp-asr] recoProxySetVadIntParam type = 0, value = 1
[kd-mrcp-asr] recoProxySetVadIntParam type = 1, value = 300
wav file length = 156672 Byte
Catch noinput at 5120 ms, elapsed 320 ms
[kd-mrcp-asr] lenovoAsrInst::sendFirstMsg
CreateMsg Index = 0, point = 0x7f0d10000b30
[kd-mrcp-asr] rreporter::createSocketCon socketConnection url = 10.110.147.191:7070
[kd-mrcp-asr] recoProxyCloseVad
asr connect error:Connection timed out
asr connect error:Connection timed out
[kd-mrcp-asr] recoProxy::openDbgFile filename: /tmp/vad//test222_0000.wav
[kd-mrcp-asr] rreporter::sendMsg 3 FRAME_LAST
[kd-mrcp-asr] socketConnection::sendMsg 2 VAD END, sessionId = test222, traceId = 6959dd58-48bc-4bf4-98da-b86d6589c262, time = 2025-03-11 11:09:50:540683


run.sh: line 1: 27077 Segmentation fault      (core dumped) ./test_kdm_asr_proxy 1 testoutput_polly0.pcm zh



- 20250310
服务器搭建fsmn-vad测试环境
安装语音处理工具，转换测试语音格式
修改测试程序，调测fsmn-vad功能
分析vad分段结果，依旧存在无法过滤噪音问题


- 20250307
调研fsmn-vad算法
对比分析fsmn-vad和silero-vad算法实现原理及优劣
编写fsmn-vad算法模型测试程序
搭建fsmn-vad测试环境



/mnt/workspace/.cache/modelscope/hub



root@centos7:/test_asr_proxy/modelscope/speech_fsmn_vad_zh-cn-8k-common# sh run.sh
2025-03-10 18:05:49,350 - modelscope - WARNING - Model revision not specified, use revision: v2.0.4
Downloading [configuration.json]: 100%|████████████████████████████████████████████████████████████████████████████████████| 356/356 [00:00<00:00, 1.91kB/s]
Downloading Model to directory: /mnt/workspace/.cache/modelscope/damo/speech_fsmn_vad_zh-cn-8k-common
2025-03-10 18:05:50,275 - modelscope - WARNING - Model revision not specified, use revision: v2.0.4
2025-03-10 18:05:50,651 - modelscope - INFO - Got 6 files, start to download ...
Downloading [README.md]: 100%|█████████████████████████████████████████████████████████████████████████████████████████| 10.5k/10.5k [00:00<00:00, 46.7kB/s]
Downloading [am.mvn]: 100%|████████████████████████████████████████████████████████████████████████████████████████████| 7.88k/7.88k [00:00<00:00, 31.6kB/s]
Downloading [config.yaml]: 100%|███████████████████████████████████████████████████████████████████████████████████████| 1.18k/1.18k [00:00<00:00, 4.30kB/s]
Downloading [fig/struct.png]: 100%|████████████████████████████████████████████████████████████████████████████████████| 27.3k/27.3k [00:00<00:00, 88.3kB/s]
Downloading [example/vad_example.wav]: 100%|███████████████████████████████████████████████████████████████████████████| 1.76M/1.76M [00:00<00:00, 3.03MB/s]
Downloading [model.pt]: 100%|██████████████████████████████████████████████████████████████████████████████████████████| 1.64M/1.64M [00:00<00:00, 1.81MB/s]
Processing 6 items: 100%|████████████████████████████████████████████████████████████████████████████████████████████████| 6.00/6.00 [00:00<00:00, 6.26it/s]
2025-03-10 18:05:51,613 - modelscope - INFO - Download model 'damo/speech_fsmn_vad_zh-cn-8k-common' successfully.██████| 27.3k/27.3k [00:00<00:00, 88.7kB/s]
2025-03-10 18:05:51,618 - modelscope - INFO - initiate model from /mnt/workspace/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-8k-common
2025-03-10 18:05:51,618 - modelscope - INFO - initiate model from location /mnt/workspace/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-8k-common.
2025-03-10 18:05:51,621 - modelscope - INFO - initialize model from /mnt/workspace/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-8k-common0:00, 3.32MB/s]
funasr version: 1.2.2.
Check update of funasr, and it would cost few times. You may disable it by set `disable_update=True` in AutoModel
New version is available: 1.2.5.
Please use the command "pip install -U funasr" to upgrade.
Warning, miss key in ckpt: encoder.in_linear1.linear.weight, /mnt/workspace/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-8k-common/model.pt
Warning, miss key in ckpt: encoder.in_linear1.linear.bias, /mnt/workspace/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-8k-common/model.pt
Warning, miss key in ckpt: encoder.in_linear2.linear.weight, /mnt/workspace/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-8k-common/model.pt
Warning, miss key in ckpt: encoder.in_linear2.linear.bias, /mnt/workspace/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-8k-common/model.pt
Warning, miss key in ckpt: encoder.fsmn.0.linear.linear.weight, /mnt/workspace/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-8k-common/model.pt
Warning, miss key in ckpt: encoder.fsmn.0.fsmn_block.conv_left.weight, /mnt/workspace/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-8k-common/model.pt
Warning, miss key in ckpt: encoder.fsmn.0.affine.linear.weight, /mnt/workspace/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-8k-common/model.pt
Warning, miss key in ckpt: encoder.fsmn.0.affine.linear.bias, /mnt/workspace/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-8k-common/model.pt
Warning, miss key in ckpt: encoder.fsmn.1.linear.linear.weight, /mnt/workspace/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-8k-common/model.pt
Warning, miss key in ckpt: encoder.fsmn.1.fsmn_block.conv_left.weight, /mnt/workspace/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-8k-common/model.pt
Warning, miss key in ckpt: encoder.fsmn.1.affine.linear.weight, /mnt/workspace/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-8k-common/model.pt
Warning, miss key in ckpt: encoder.fsmn.1.affine.linear.bias, /mnt/workspace/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-8k-common/model.pt
Warning, miss key in ckpt: encoder.fsmn.2.linear.linear.weight, /mnt/workspace/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-8k-common/model.pt
Warning, miss key in ckpt: encoder.fsmn.2.fsmn_block.conv_left.weight, /mnt/workspace/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-8k-common/model.pt
Warning, miss key in ckpt: encoder.fsmn.2.affine.linear.weight, /mnt/workspace/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-8k-common/model.pt
Warning, miss key in ckpt: encoder.fsmn.2.affine.linear.bias, /mnt/workspace/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-8k-common/model.pt
Warning, miss key in ckpt: encoder.fsmn.3.linear.linear.weight, /mnt/workspace/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-8k-common/model.pt
Warning, miss key in ckpt: encoder.fsmn.3.fsmn_block.conv_left.weight, /mnt/workspace/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-8k-common/model.pt
Warning, miss key in ckpt: encoder.fsmn.3.affine.linear.weight, /mnt/workspace/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-8k-common/model.pt
Warning, miss key in ckpt: encoder.fsmn.3.affine.linear.bias, /mnt/workspace/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-8k-common/model.pt
Warning, miss key in ckpt: encoder.out_linear1.linear.weight, /mnt/workspace/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-8k-common/model.pt
Warning, miss key in ckpt: encoder.out_linear1.linear.bias, /mnt/workspace/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-8k-common/model.pt
Warning, miss key in ckpt: encoder.out_linear2.linear.weight, /mnt/workspace/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-8k-common/model.pt
Warning, miss key in ckpt: encoder.out_linear2.linear.bias, /mnt/workspace/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-8k-common/model.pt
2025-03-10 18:05:55,756 - modelscope - WARNING - No preprocessor field found in cfg.
2025-03-10 18:05:55,756 - modelscope - WARNING - No val key and type key found in preprocessor domain of configuration.json file.
2025-03-10 18:05:55,756 - modelscope - WARNING - Cannot find available config to build preprocessor at mode inference, current config: {'model_dir': '/mnt/workspace/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-8k-common'}. trying to build by task and model information.
2025-03-10 18:05:55,757 - modelscope - WARNING - No preprocessor key ('funasr', 'voice-activity-detection') found in PREPROCESSOR_MAP, skip building preprocessor.
2025-03-10 18:05:55,758 - modelscope - INFO - cuda is not available, using cpu instead.
Traceback (most recent call last):
  File "/test_asr_proxy/modelscope/speech_fsmn_vad_zh-cn-8k-common/ms_vad_test.py", line 84, in <module>
    test_8k(wav_file)
  File "/test_asr_proxy/modelscope/speech_fsmn_vad_zh-cn-8k-common/ms_vad_test.py", line 43, in test_8k
    rec_result = inference_pipeline(
  File "/usr/local/lib/python3.10/site-packages/modelscope/pipelines/audio/funasr_pipeline.py", line 73, in __call__
    output = self.model(*args, **kwargs)
  File "/usr/local/lib/python3.10/site-packages/modelscope/models/base/base_model.py", line 35, in __call__
    return self.postprocess(self.forward(*args, **kwargs))
  File "/usr/local/lib/python3.10/site-packages/modelscope/models/audio/funasr/model.py", line 61, in forward
    output = self.model.generate(*args, **kwargs)
TypeError: AutoModel.generate() missing 1 required positional argument: 'input'



root@centos7:/test_asr_proxy/modelscope/speech_fsmn_vad_zh-cn-8k-common# sh run.sh

funasr version: 1.2.2.
Check update of funasr, and it would cost few times. You may disable it by set `disable_update=True` in AutoModel
New version is available: 1.2.5.
Please use the command "pip install -U funasr" to upgrade.
Downloading Model to directory: /mnt/workspace/.cache/modelscope/iic/speech_fsmn_vad_zh-cn-16k-common-pytorch
2025-03-10 15:34:54,901 - modelscope - INFO - Use user-specified model revision: v2.0.4
2025-03-10 15:34:55,157 - modelscope - INFO - Got 7 files, start to download ...
Downloading [README.md]: 100%|█████████████████████████████████████████████████████████████████████████████████████████| 8.45k/8.45k [00:00<00:00, 37.8kB/s]
Downloading [am.mvn]: 100%|████████████████████████████████████████████████████████████████████████████████████████████| 7.85k/7.85k [00:00<00:00, 20.4kB/s]
Downloading [configuration.json]: 100%|██████████████████████████████████████████████████████████████████████████████████████| 365/365 [00:00<00:00, 950B/s]
Downloading [fig/struct.png]: 100%|████████████████████████████████████████████████████████████████████████████████████| 27.3k/27.3k [00:00<00:00, 70.2kB/s]
Downloading [config.yaml]: 100%|███████████████████████████████████████████████████████████████████████████████████████| 1.19k/1.19k [00:00<00:00, 2.99kB/s]
Downloading [example/vad_example.wav]: 100%|███████████████████████████████████████████████████████████████████████████| 2.16M/2.16M [00:01<00:00, 2.24MB/s]
Downloading [model.pt]: 100%|██████████████████████████████████████████████████████████████████████████████████████████| 1.64M/1.64M [00:01<00:00, 1.60MB/s]
Processing 7 items: 100%|████████████████████████████████████████████████████████████████████████████████████████████████| 7.00/7.00 [00:01<00:00, 6.45it/s]
2025-03-10 15:34:56,245 - modelscope - INFO - Download model 'iic/speech_fsmn_vad_zh-cn-16k-common-pytorch' successfully.27.3k/27.3k [00:00<00:00, 70.9kB/s]
rtf_avg: 0.120: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 49.48it/s]
rtf_avg: 0.067: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 70.22it/s]
rtf_avg: 0.042: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 108.76it/s]
[{'key': 'rand_key_WgNZq6ITZM5jt', 'value': [[70, -1]]}]
rtf_avg: 0.039: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 117.33it/s]
rtf_avg: 0.039: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 117.19it/s]
rtf_avg: 0.040: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 114.27it/s]
rtf_avg: 0.039: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 118.02it/s]
rtf_avg: 0.039: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 116.31it/s]
rtf_avg: 0.043: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 106.49it/s]
rtf_avg: 0.040: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 114.17it/s]
rtf_avg: 0.039: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 116.64it/s]
rtf_avg: 0.039: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 116.45it/s]
rtf_avg: 0.044: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 104.19it/s]
rtf_avg: 0.039: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 116.37it/s]
rtf_avg: 0.044: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 98.69it/s]
[{'key': 'rand_key_PS6YwfuNhFLOv', 'value': [[-1, 2340]]}]
rtf_avg: 0.099: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 47.74it/s]
[{'key': 'rand_key_2mpbUrhToxYkv', 'value': [[2620, -1]]}]





# The Research of VAD

## VAD List

## signal processing

- lenovo
- webrtc
- kaldi
- epd

## neural network(ML/DL)

- DeepSpeech
- silero-vad
- funasr/fsmn-vad

### requirements

- python>=3.8
- torch>=1.13
- torchaudio

### env install

```bash
conda create -n modelscope_py3.10 python=3.10
conda activate modelscope_py3.10
pip3 install -U funasr
pip3 install modelscope
# modelscope download --model iic/speech_fsmn_vad_zh-cn-8k-common

# pip3 install torchaudio
# pip3 install torch -i https://pypi.tuna.tsinghua.edu.cn/simple
# pip3 install -U modelscope huggingface_hub
```

- wenet
- espnet
- k2/sherpa-onnx

https://github.com/modelscope/FunASR

⭐ represents the ModelScope model zoo
🤗 represents the Huggingface model zoo
🍀 represents the OpenAI model zoo


alibaba(16k的是Unet结构，没有使用Transformer)

End-to-End Integration of Speech Emotion Recognition with Voice Activity Detection using Self-Supervised Learning Features

全文摘要
这篇论文介绍了一种基于自我监督学习特征的语音情感识别（SER）和语音活动检测（VAD）端到端集成方法。传统的SER方法通常使用VAD模型检测出的语音片段进行操作，但VAD模型可能会在嘈杂环境中输出错误的语音片段，导致后续的SER模型性能下降。为了解决这个问题，作者提出了一个端到端方法，将VAD和SER模块整合在一起，并使用自我监督学习特征作为输入。实验结果表明，该方法可以提高SER的性能。此外，为了探究该方法对VAD和SSL模块的影响，作者还进行了VAD输出和SSL编码器各层权重的分析。

- SSL-VAD
- MarbleNet VAD
- reference: https://www.modelscope.cn/papers/64188




对比分析fsmn-vad与silero-vad:
https://blog.csdn.net/weixin_45684442/article/details/140712513


iic/speech_fsmn_vad_zh-cn-16k-common-pytorch
iic/speech_fsmn_vad_zh-cn-8k-common-onnx
iic/speech_fsmn_vad_zh-cn-8k-common
https://www.modelscope.cn/models/iic/speech_fsmn_vad_zh-cn-8k-common/summary


onnx-community/silero-vad
dsh54054/silero-vad
manyeyes/silero-vad-onnx
https://github.com/snakers4/silero-vad.git
https://www.modelscope.cn/models/dsh54054/silero-vad/files



20250306
搭建录音数据的技术分析环境
技术分析VAD断句问题的录音数据详情，均由asr引擎误识别噪音导致
调研VAD算法实现DeepSpeech
调研VAD算法实现silero-vad




可考虑增加3A模块缓解；





电话语音机器人专项突破启动会20250305

TODO:
最新vad研究开源算法调研
rewrite改写or纠错语言模型工程化


elk、flink

项目背景：
颐和园、市监局、智联、
热力、徐工


优化体验不好问题:(3.24那周给出优化的技术和解决方案)

3A问题:
(降噪、回声消除、自动增益)


vad问题:
断句、打断反应慢(语义或意图打断)

最新vad研究开源算法调研

webrtc signal，效果一般
nn模型速度慢，效果一般


drimo3.0机器人
智能客服


asr问题:
转译，asr识别结果不准确

rewrite改写or纠错语言模型工程化


NLU/NLP问题:
反应迟钝、延迟时间长


tts问题:
语音合成or播报不完整(前半句丢失)




20250305
调测kd-asr-proxy新增SessionContext功能模块
分析梳理ManagerSingleton会化管理OnSessionCreate流程
优化AsrReporter、AsrParam、VadParam等模块，解决SessionContext部分参数值丢失问题
参加电话语音机器人专项突破启动会




20250304
开发SessionContext会话管理模块
优化Call、SessionCreateReq、RecoProxyProcess等模块对应接口
优化utils::json_value支持int64类型数值
构建并部署kd-asr-proxy新版本docker镜像，进行联调


搭建并调测软电话测试环境
联调新增透传字段无效问题


推送asr结果至kafka失败问题
增加默认配置，定位


router.POST("/asr/session", [](const HttpContextPtr& ctx) {

	http::api::SessionCreateReq sc_req;
	ManagerSingleton::OnSessionCreate(const http::api::SessionCreateReq& req) {

		// Call::CreateRecieverSession(EndPointType ep, int port, const std::string& asrEngine, int engMin, int engMax, int bos, int eos, std::string &sid) {
		Call::CreateRecieverSession(const http::api::SessionCreateReq& req, int port) {

			RecieverPtr pRecv; SetSid, Init, Start,
			// pProcessor RecoProxyProcess; UpdateSid, Create {
			// RecoProxyProcess::RecoProxyProcess(const std::string& appID, const std::string& callID, const std::string& sid, const std::string& epTp) {
			RecoProxyProcess::RecoProxyProcess(const http::api::SessionCreateReq& req) {

				m_pObj pCreateRecoProxy;

			}

		} // Call::CreateRecieverSession

	} // ManagerSingleton::OnSessionCreate

} // router.POST


	{"timestamp":"2025-02-06T16:37:26.861","msg":"call processor destory sid 2edb7d13-6790-40be-bc0d-bb31e9d36799_30098"}
	{"timestamp":"2025-02-06T16:37:26.862","msg":"sesssion 2edb7d13-6790-40be-bc0d-bb31e9d36799_30098 processor destory"}
	{"timestamp":"2025-02-06T16:37:26.885","msg":"call processor destory sid 2edb7d13-6790-40be-bc0d-bb31e9d36799_30100"}
	{"timestamp":"2025-02-06T16:37:26.888","msg":"sesssion 2edb7d13-6790-40be-bc0d-bb31e9d36799_30100 processor destory"}
	{"timestamp":"2025-02-06T16:55:42.021","msg":"call processor destory sid 2b63b151-7b2f-49c2-91e9-68736d1049c0_30000"}
	{"timestamp":"2025-02-06T16:55:42.025","msg":"sesssion 2b63b151-7b2f-49c2-91e9-68736d1049c0_30000 processor destory"}
	{"timestamp":"2025-02-06T16:55:42.061","msg":"call processor destory sid 2b63b151-7b2f-49c2-91e9-68736d1049c0_30002"}
	{"timestamp":"2025-02-06T16:55:42.061","msg":"sesssion 2b63b151-7b2f-49c2-91e9-68736d1049c0_30002 processor destory"}





20250303
优化kd-asr-proxy配置解析模块，联调解决kafka topic解析异常coredump问题
排查解决kd-asr-proxy服务无asr识别结果推送问题
修改kd-asr-proxy推送kafka回传毫秒时间戳
设计kd-asr-proxy新增两个透传字段(agentId、serviceId)


{"project":"kds","module":"kd-asr-proxy","timestamp":"2025-02-28T14:20:16.275","level":"info","host":"centos7","hostIp":"172.70.10.210","event":{"appId":"servicePool_test_appId","asrResult":"差不多就是","callId":"b5e009c7-9287-44c2-9d1d-5fb72e7d257f","channelId":"b5e009c7-9287-44c2-9d1d-5fb72e7d257f_30004","channelType":"agent","sessionId":"b5e009c7-9287-44c2-9d1d-5fb72e7d257f_30004"},"eventId":"4ae1026b-0280-4266-987a-a8903fc57e95","eventName":"ASR_RESULT_CB"}
{"project":"kds","module":"kd-asr-proxy","timestamp":"2024-12-17T15:41:51.843","level":"info","host":"centos7","hostIp":"172.70.10.210","event":{"appId":"servicePool_test_appId","asrResult":"喂你好喂你好喂你好能听到我说话吗","callId":"254425cb-ebde-433c-932d-9538bf48cd2a","channelId":"254425cb-ebde-433c-932d-9538bf48cd2a_30004","channelType":"agent","sessionId":"254425cb-ebde-433c-932d-9538bf48cd2a_30004"},"eventId":"edc97f19-f69d-44f2-aecd-ffb798c5dad5","eventName":"ASR_RESULT_CB"}




{"project":"kds","module":"kd-asr-proxy","timestamp":"2025-02-28T14:19:57.862","level":"info","host":"centos7","hostIp":"172.70.10.210","msg":"createSession response 200 {"code":200,"data":{"rtpPort":30004,"sessionID":"b5e009c7-9287-44c2-9d1d-5fb72e7d257f_30004"},"msg":"OK"}"}
{"project":"kds","module":"kd-asr-proxy","timestamp":"2025-02-28T14:20:16.275","level":"debug","host":"centos7","hostIp":"172.70.10.210","msg":"sid b5e009c7-9287-44c2-9d1d-5fb72e7d257f_30004 recieve command = 0"}
{"project":"kds","module":"kd-asr-proxy","timestamp":"2025-02-28T14:20:16.275","level":"debug","host":"centos7","hostIp":"172.70.10.210","msg":"recieve result sid , file /var/asr_record/6294be67-be57-41b1-b8af-abffee8ee51c_0002.wav, result 差不多就是, index 2, pos 0, beginTime 16400, endTime 18480"}
{"project":"kds","module":"kd-asr-proxy","timestamp":"2025-02-28T14:20:16.706","level":"info","host":"centos7","hostIp":"172.70.10.210","msg":"Starting ... "}
{"project":"kds","module":"kd-asr-proxy","timestamp":"2025-02-28T14:20:16.711","level":"info","host":"centos7","hostIp":"172.70.10.210","msg":"kd-asr-proxy bind host 172.70.10.210 port 30208"}



{"project":"kds","module":"kd-asr-proxy","timestamp":"2025-02-24T15:52:10.283","level":"info","host":"centos7","hostIp":"172.70.10.210","msg":"kafka msg sended, topic asr_result_notify partition 0 msg {"app_id":"servicePool_test_appId","begin_time":"2025-02-24 15:52:08","call_id":"30c117b0-189f-42a6-a2b3-049dd1ef31ec","index":0,"msg_type":"asr_result","result":"喂喂喂喂喂喂","side":"agent","time_stamp":"2025-02-24 15:52:08,000"}"}
{"project":"kds","module":"kd-asr-proxy","timestamp":"2025-02-24T15:52:14.865","level":"debug","host":"centos7","hostIp":"172.70.10.210","msg":"sid 30c117b0-189f-42a6-a2b3-049dd1ef31ec_30088 recieve command = 0"}

{"project":"kds","module":"kd-asr-proxy","timestamp":"2025-02-24T15:52:14.865","level":"debug","host":"centos7","hostIp":"172.70.10.210","msg":"recieve result sid , file /var/asr_record/e8984bb5-d7d3-437c-a8c3-3c033b2ffba0_0001.wav, result 可以说话吗能听到吗, index 1, pos 0, beginTime 4650, endTime 6820"}
{"project":"kds","module":"kd-asr-proxy","timestamp":"2025-02-24T15:52:14.867","level":"info","host":"centos7","hostIp":"172.70.10.210","msg":"kafka msg sended, topic asr_result_notify partition 0 msg {"app_id":"servicePool_test_appId","begin_time":"2025-02-24 15:52:09","call_id":"30c117b0-189f-42a6-a2b3-049dd1ef31ec","index":1,"msg_type":"asr_result","result":"可以说话吗能听到吗","side":"agent","time_stamp":"2025-02-24 15:52:09,000"}"}

{"project":"kds","module":"kd-asr-proxy","timestamp":"2025-02-24T15:52:24.630","level":"info","host":"centos7","hostIp":"172.70.10.210","msg":"recieve request method DELETE, body sessionid 30c117b0-189f-42a6-a2b3-049dd1ef31ec_30086"}
{"project":"kds","module":"kd-asr-proxy","timestamp":"2025-02-24T15:52:24.829","level":"info","host":"centos7","hostIp":"172.70.10.210","msg":"pcm reciever thread exit ... fd 46"}




20250228
联调kd-asr-proxy推送kafka asr结果功能和kafka topic配置功能
同步kt-lib分支dev代码到分支dev_intent2，合并解决代码冲突
调研sqlite数据库三方开发框架(sqlite_orm、sqlite3pp、sqlitecpp、easysqlite、sqlSQLite++、sqlite3cc)
搭建并测试数据库开发框架sqlite_orm环境



vcpkg install sqlite-orm

sqlite-orm provides CMake targets:
  # this is heuristically generated, and may not be correct
  find_package(SqliteOrm CONFIG REQUIRED)
  target_link_libraries(main PRIVATE sqlite_orm::sqlite_orm)




sqlite3pp: modern design inspired by boost, MIT License
sqlitecpp: qeury with string and bind
easySQLite: manages table as structured objects, complex
sqlite_modern_cpp: modern C++11, all in one file, MIT license
sqlite_orm: modern C++14, header only all in one file, no raw string queries, BSD-3 license


sqlite3cc: uses boost, modern design, LPGPL
SQLite++: uses boost build system, Boost License 1.0
CppSQLite: famous Code Project but old design, BSD License
sqdbcpp: RAII design, simple, no dependencies, UTF-8/UTF-16, new BSD license




1、kafka消息格式修改
2、topic改成变量可配的启动参数(环境变量ASRPROXY_KAFKA_TOPIC, )，目前topic是写死的


{"project":"kds","module":"kd-asr-proxy","timestamp":"2025-03-05T14:19:33.082","level":"debug","host":"centos7","hostIp":"172.70.10.210","msg":"获取rtp端口 30004"}
{"project":"kds","module":"kd-asr-proxy","timestamp":"2025-03-05T14:19:33.082","level":"debug","host":"centos7","hostIp":"172.70.10.210","msg":"ASR OPTIONS: AsrRenderId 3 1"}
{"project":"kds","module":"kd-asr-proxy","timestamp":"2025-03-05T14:19:33.083","level":"debug","host":"centos7","hostIp":"172.70.10.210","msg":"recpProxy.so pCreateRecoProxy success"}
{"project":"kds","module":"kd-asr-proxy","timestamp":"2025-03-05T14:19:33.083","level":"debug","host":"centos7","hostIp":"172.70.10.210","msg":"PCMReciever listen 172.70.10.210:30004"}
{"project":"kds","module":"kd-asr-proxy","timestamp":"2025-03-05T14:19:33.083","level":"info","host":"centos7","hostIp":"172.70.10.210","msg":"binding PCM reciever port success, fs 33 ipaddr 172.70.10.210 port 30004"}
{"project":"kds","module":"kd-asr-proxy","timestamp":"2025-03-05T14:19:33.083","level":"debug","host":"centos7","hostIp":"172.70.10.210","msg":"insert processor for sid ad592d37-74f7-4670-a5b5-e0f7b07f72ca_30004"}

{"project":"kds","module":"kd-asr-proxy","timestamp":"2025-03-05T14:19:33.083","level":"info","host":"centos7","hostIp":"172.70.10.210","msg":"call session create success, sid ad592d37-74f7-4670-a5b5-e0f7b07f72ca_30004"}
{"project":"kds","module":"kd-asr-proxy","timestamp":"2025-03-05T14:19:33.083","level":"info","host":"centos7","hostIp":"172.70.10.210","msg":"createSession response 200 {"code":200,"data":{"rtpPort":30004,"sessionID":"ad592d37-74f7-4670-a5b5-e0f7b07f72ca_30004"},"msg":"OK"}"}
{"project":"kds","module":"kd-asr-proxy","timestamp":"2025-03-05T14:19:33.083","level":"info","host":"centos7","hostIp":"172.70.10.210","msg":"pcm reciever thread start ... fd 33"}

{"project":"kds","module":"kd-asr-proxy","timestamp":"2025-03-05T14:19:37.015","level":"debug","host":"centos7","hostIp":"172.70.10.210","msg":"sid 0b8764ea-3334-4134-9299-9afca8314556_30002 receive command = 0"}
{"project":"kds","module":"kd-asr-proxy","timestamp":"2025-03-05T14:19:37.015","level":"debug","host":"centos7","hostIp":"172.70.10.210","msg":"recieve result sid , file /var/asr_record/0b8764ea-3334-4134-9299-9afca8314556_0000.wav, result 喂喂喂喂喂喂, index 0, pos 0, beginTime 1550, endTime 3960"}





{
	"agentId":1896135529281617922,
	"appID":"servicePool_test_appId",
	"asrEngine":"Lenovo_HTTP",
	"callID":"0b8764ea-3334-4134-9299-9afca8314556",
	"channelID":"0b8764ea-3334-4134-9299-9afca8314556",
	"channelType":"agent",
	"serviceId":1897170063405424640,
	"vadParams":{
		"maxSpeechPause":750,
		"minSpeechDuration":120,
		"minVoicePoint":2000,
		"voicePoint":4000
	}
}


app_id servicePool_test_appId,
call_id 0b8764ea-3334-4134-9299-9afca8314556,
channel_id 0b8764ea-3334-4134-9299-9afca8314556,
service_id agent,
agent_id 2 ,
channel_type 1897170063405424640,
asr_engine 1896135529281617922 ,
voice_point 4000,
min_voice_point 2000,
spd 120,
spp 120


{

	"appID": "servicePool_test_appId",
	"asrEngine": "Lenovo_HTTP",
	"callID": "0d5c80ac-5d19-4f3b-ab67-b779348c5b60",
	"channelID": "0d5c80ac-5d19-4f3b-ab67-b779348c5b60",
	"channelType": "user",
	"serviceId": 1896485082995732480,
	"agentId": 1895020113934639106,
	"vadParams": {
		"maxSpeechPause": 750,
		"minSpeechDuration": 120,
		"minVoicePoint": 2000,
		"voicePoint": 4000
	}
}

{
"type": "asrResult",
"data": {
	"serviceId": 1896485082995732480,												//透传，来自create
	"agentId": 1895020113934639106,													//透传，来自create
	"sessionId": "0f0d6196-217a-4b19-a306-34f10950f279",							//原callId
	"time": 1652525365123, 															//当前时间
	"side": "user", 																//user或agent
	"msgBody": "你好",
	"msgType": "text"
 }
}




20250227
修改kd-asr-proxy推送kafka asr结果格式
添加kd-asr-proxy推送kafka topic通过环境变量方式可配功能
调试解决kd-asr-proxy编译报错问题
构建kd-asr-proxy docker镜像最新版本



20250226
跟进规避kylin软件安装dbus接口管控方式(后续通知kylin技术更新白名单即可)
支持维章联调sysfunc.key.shortcuts功能接口
编写意图体系Excel表格必要数据解析的工具程序
构建系统调用所用意图资源sqlite数据库




sysfunc.app.get 获取本地已安装应用接口
sysfunc.app.install 安装应用到本地接口
sysfunc.app.installable 查询可安装应用接口

#sysfunc.app.open 打开已安装应用接口

#sysfunc.os.set 系统设置接口
#sysfunc.os.get 系统状态接口


sysfunc.key.shortcuts 键盘唤起快捷输入框接口




系统调用接口
intent 调用方式：打开应用

应用状态变更事件
INSTALL_STATUS_CHANGE: 应用安装状态变更事件
RUNNING_STATUS_CHANGE: 应用运行状态变更事件

用户行为事件
USER_SELECTED_CONTENT_CHANGE: 用户选择的内容变更事件
USER_MOUSE_EVENT: 用户鼠标事件




20250225
设计sysfunc.exec打开应用功能模块
开发sysfunc.exec打开应用功能
调测sysfunc.exec打开应用功能
排查解决打开应用shell命令调用失败问题


the design of sysfunc exec:

打开应用:
	get_app_by_key: 			func，9个，		前端调grpc api(app_info) --> shell
	get_login_user: 	    	func，6个，		后台调system api(username) --> shell
	desktop: 	    			gio， 18个，		后台调ukuisearch(app_info) --> shell

系统设置:
	gsettings:					shell，59个，	后台调shell
	ukui-control-center:		shell，108个，	后台调shell
	gdbus call --session:		shell，10个，	后台调shell
	ukui-screensaver-command:	shell，1个，		后台调shell


	"type": "dbus",				dbus，2个，		后台调shell
		"data": {
			"destination": "org.ukui.media",
			"path": "/org/ukui/media",
			"interface": "org.ukui.media",
			"method": "getDefaultOutputVolume",
			"paramfmt": ""
		}


	"type": "int",				int，3个			后台调shell
		"delta": 10,
		"max": 100,
		"min": 0
	"type": "float",			float，3个		后台调shell
		"delta": 0.2,
		"max": 1.0,
		"min": 0.0
	"type": "enum",				enum，2个，		后台调shell
		"enums": ["10", "12", "13.5", "15"]
	"type": "map",				map，10个，		后台调shell
		"maps": {
			"1分钟": "1",
			"5分钟": "5",
			"10分钟": "10",
			"15分钟": "15",
			"30分钟": "30",
			"1小时": "60",
			"从不": "-1"
		}


20250224
更新51.215机器测试环境最新版本(kt-lib/dev,kt-app/phase2)
调测应用中心安装接口底层dbus服务调用报错问题(upgrade-2403.tar.gz补丁包安装、管控取消)
排查解决并发调用sysfunc.app.get接口服务崩溃问题
添加sysfunc.exec功能接口，尝试解决模块选择错误(sysfunc中意图槽位匹配失败)



I20250224 17:07:59.542178 21573 sysfunc.cc:749] handleGrpcMsgAsync request: {"cmd":"sysfunc.app.get","data":{"package":"","name":"微信"},"private":"调用者自定义字符串"}
I20250224 17:07:59.542275 21573 app_manager.cc:143] app manager searching 微信
I20250224 17:07:59.544663 21573 app_manager.cc:188] app manager search [{"exec":"/usr/bin/wechat ","icon":"/usr/share/icons/hicolor/256x256/apps/wechat.png","identity":"/usr/share/applications/wechat.desktop","name":"微信","package":"wechat","status":4,"version":""}]
I20250224 17:07:59.545109 21573 sysfunc.cc:821] handleGrpcMsgAsync rep: {"cmd":"sysfunc.app.get","data":[{"exec":"/usr/bin/wechat ","icon":"/usr/share/icons/hicolor/256x256/apps/wechat.png","identity":"/usr/share/applications/wechat.desktop","name":"微信","package":"wechat","status":4,"version":""}],"eot":true,"private":"调用者自定义字符串","sessionId":null,"state":{"code":0,"extend":"","info":"success"}}
I20250224 17:07:59.553581 21573 sysfunc.cc:749] handleGrpcMsgAsync request: {"cmd":"sysfunc.exec","data":{"type":"intent","data":{"intent":"打开应用","slots":["微信"]}},"private":"自定义标识"}
I20250224 17:07:59.553642 21573 sysfunc.cc:679] syscall_cmd() cmdMsg: {"data":{"intent":"打开应用","slots":["微信"]},"type":"intent"}
I20250224 17:07:59.553663 21573 sysfunc.cc:339] KModuleSysfunc::syscall_intent in
I20250224 17:07:59.553680 21573 sysfunc.cc:345] KModuleSysfunc::syscall_intent intent = 打开应用
I20250224 17:07:59.553700 21573 sysfunc.cc:363] KModuleSysfunc::syscall_intent mainSlot: 微信, subSlot:
I20250224 17:07:59.553732 21573 sysfunc.cc:371] >>>>>> cmdCfg is null.
I20250224 17:07:59.553750 21573 sysfunc.cc:574] KModuleSysfunc::syscall_intent ot
I20250224 17:07:59.553774 21573 sysfunc.cc:821] handleGrpcMsgAsync rep: {"cmd":"sysfunc.exec","data":{"result":"槽值不存在"},"eot":true,"private":"自定义标识","sessionId":null,"state":{"code":400,"extend":"","info":"success"}}




20250221
调试sysfunc中模拟键盘输入功能接口
编写sysfunc中模拟键盘输入接口文档
调测sysfunc应用商店搜索功能接口
排查解决dbus应用搜索方法调用参数解析错误问题


20250220
调研C++实现模拟键盘输入功能(X11、QT、Wayland、uinput、evdev)
编写C++测试用例验证模拟键盘输入功能(基于X11实现该功能可用)
设计模拟键盘执行器key_actuator模块
开发sysfunc中模拟键盘输入接口，实现唤起小天快捷输入框功能



/home/lit/project/kaitian/kt-lib/bin/resource/intent/intent_resource.zip

unzOpen


intent_controller、intent_recognizer、slot_filler


./modelutil bin

(data_vector.json --> hnsw.bin)



20250219
构建并更新意图hnsw向量库，更新意图sort模型，测试修复bad case:"泰山多高"
合并固定槽位和可变槽位到同一个意图槽位关联配置文件
汇总意图资源文件的构造工具及其原始素材，编写其使用说明文档
修改sysfunc中intent调用流程与逻辑，因抽槽模块更新，sysfunc解析槽位信息暂无法兼容，需对应更新sysfunc中配置文件kd_sysf_cfg.enc



20250218
修改code关联信息预置表构造逻辑，调试解决code关联信息预置表解析失败问题
调测解决意图code匹配失败问题
调测槽名和槽值的code匹配出错问题
梳理sysfunc中intent调用流程与逻辑


1、intent_name(intent api json)

2、intent_value(all slots value) = kd_sysf_cfg.enc[intent_name](kd_sysf_cfg.enc file)

3、main_slot, sub_slot = intent_name(intent api json)

4、shell cmd = kd_sysf_cfg.enc[intent_name][main_slot](kd_sysf_cfg.enc file)
  / shell cmd = kd_sysf_cfg.enc[intent_name][sub_slot](kd_sysf_cfg.enc file)





20250217
调测意图识别bad case: "输入泰山有多高"
探讨并修改意图接口api(code关联信息)
开发code关联信息预置表构造和解析逻辑
开发意图识别和抽槽模块接口code关联信息


intent_code
slot_code
slot_value_name





开天意图体系 二期:
https://docs.qq.com/sheet/DQlJ6QWhCb0xVaFpD?tab=000001&no_promotion=1&nlc=1&_t=1739763548876


I20250217 09:54:31.154943 112461 hnsw_searcher.cc:71] kdm hnsw searcher search result idx: 35008, relation = 0.240524, label = 设置字体大小的状态, text = 查
询一下字体大小状态, score = 0.759476
I20250217 09:54:31.154956 112461 hnsw_searcher.cc:71] kdm hnsw searcher search result idx: 31540, relation = 0.242184, label = 设置字体大小, text = 帮我把字
体放到最大, score = 0.757816
I20250217 09:54:31.154966 112461 intent_model_bert.cc:86] intent model bert recognize 输入泰山有多高 intent OTHER, score 0.804328, match text 你有多高
I20250217 09:54:31.162602 112461 intent_model_bert.cc:94] intent model bert recognize 输入泰山有多高 intent OTHER, rescore 0.402271, match text 你有多高
I20250217 09:54:31.162700 112461 intent_model_bert.cc:86] intent model bert recognize 输入泰山有多高 intent 文本创作, score 0.799022, match text 山有多高歌>词生成：
I20250217 09:54:31.179783 112461 intent_model_bert.cc:94] intent model bert recognize 输入泰山有多高 intent 文本创作, rescore 0.399583, match text 山有多高>歌词生成：
I20250217 09:54:31.179852 112461 intent_model_bert.cc:86] intent model bert recognize 输入泰山有多高 intent OTHER, score 0.797757, match text 身高？
I20250217 09:54:31.186669 112461 intent_model_bert.cc:94] intent model bert recognize 输入泰山有多高 intent OTHER, rescore 0.404728, match text 身高？
I20250217 09:54:31.186736 112461 intent_model_bert.cc:86] intent model bert recognize 输入泰山有多高 intent OTHER, score 0.794401, match text 你多高
I20250217 09:54:31.193466 112461 intent_model_bert.cc:94] intent model bert recognize 输入泰山有多高 intent OTHER, rescore 0.397221, match text 你多高
I20250217 09:54:31.193537 112461 intent_model_bert.cc:86] intent model bert recognize 输入泰山有多高 intent 打开天气, score 0.772818, match text 下周一泰山>的天气适合爬山吗
I20250217 09:54:31.202370 112461 intent_model_bert.cc:94] intent model bert recognize 输入泰山有多高 intent 打开天气, rescore 0.886391, match text 下周一泰>山的天气适合爬山吗
I20250217 09:54:31.202436 112461 intent_model_bert.cc:86] intent model bert recognize 输入泰山有多高 intent 设置字体大小的状态, score 0.771357, match text >目前的字体大小是什么
I20250217 09:54:31.210414 112461 intent_model_bert.cc:94] intent model bert recognize 输入泰山有多高 intent 设置字体大小的状态, rescore 0.385684, match text 目前的字体大小是什么
I20250217 09:54:31.210485 112461 intent_model_bert.cc:86] intent model bert recognize 输入泰山有多高 intent 设置字体大小的状态, score 0.764991, match text >现在是什么字体大小
I20250217 09:54:31.218429 112461 intent_model_bert.cc:94] intent model bert recognize 输入泰山有多高 intent 设置字体大小的状态, rescore 0.3825, match text >现在是什么字体大小
I20250217 09:54:31.218495 112461 intent_model_bert.cc:86] intent model bert recognize 输入泰山有多高 intent 设置字体大小的状态, score 0.763636, match text >现在字体是多大
I20250217 09:54:31.226540 112461 intent_model_bert.cc:94] intent model bert recognize 输入泰山有多高 intent 设置字体大小的状态, rescore 0.381823, match text 现在字体是多大
I20250217 09:54:31.226608 112461 intent_model_bert.cc:86] intent model bert recognize 输入泰山有多高 intent 打开天气, score 0.763447, match text 查询近期双>鸭山湿度是否属于挺高
I20250217 09:54:31.235882 112461 intent_model_bert.cc:94] intent model bert recognize 输入泰山有多高 intent 打开天气, rescore 0.881704, match text 查询近期>双鸭山湿度是否属于挺高
I20250217 09:54:31.235947 112461 intent_model_bert.cc:86] intent model bert recognize 输入泰山有多高 intent 设置字体大小, score 0.757816, match text 帮我把>字体放到最大
I20250217 09:54:31.244045 112461 intent_model_bert.cc:94] intent model bert recognize 输入泰山有多高 intent 设置字体大小, rescore 0.378913, match text 帮我>把字体放到最大
I20250217 09:54:31.244112 112461 intent_model_bert.cc:111] intent model bert recognize intent 打开天气 score 0.886391, match text 下周一泰山的天气适合爬山吗


20250214
调测kt-lib arm64平台编译问题，定位解决sqlite3依赖缺失问题
熟悉ktservice测试环境使用和打包
测试arm64平台下意图模块加载、识别、卸载、升级功能
支持维璋调测应用查询、安装等接口，解决kylin系统提示其他任务进行中



20250213
调测intent2.0识别功能接口，排查解决pipeline流程中断问题
调测并修改intent2.0更新升级功能接口
排查解决测试意图模型更新时崩溃问题
修改意图各个模块命名规范(intent_controller、intent_recognizer、slot_filler)


20250212
编写intent2.0接口测试用例
调测intent2.0模型加载，卸载接口，定位解决接口协议解析失败问题
验证麒麟应用商店搜索session dbus接口调用
参加转正述职报告会议


20250211
排查颐和园项目线上freeswitch调用mrcp建立tts通道失败问题
跟进调测麒麟应用商店搜索接口调用不通问题
开发intent2.0外部交互api intent.recog功能接口
调试解决intent2.0集成层编译报错问题


20250210
优化intent2.0资源重载与升级模块
开发intent2.0外部交互api model.load功能接口
开发intent2.0外部交互api model.unload功能接口
开发intent2.0外部交互api model.update功能接口


20250208
开发KModuleIntent接口模块
开发ner和intent流程pipeline
梳理原intent资源重载与升级模块
设计新版intent资源重载与升级模块


E20250208 11:56:40.229475 258173 app_manager.cc:92] app manager center proxy_new_for_bus_sync error: Error calling StartServiceByName for com.kylin.softwarecenter.getsearchresults: Cannot do system-bus activation with no user
(process:258173): GLib-GIO-CRITICAL **: 11:56:40.229: g_dbus_proxy_call_sync_internal: assertion 'G_IS_DBUS_PROXY (proxy)' failed


20250207
修改text_embedding为独立kdm工程
修改kdm_intent为独立kdm工程
修改kdm_ner为独立kdm工程
梳理kt-lib中依赖于原intent的其他模块(modelutil)


20250206
开发text_embedding文本向量化模块
调测text_embedding依赖缺失问题
集成text_embedding到kt-lib
调测解决kt-lib/text_embedding编译问题


20250205
编写intent意图识别功能测试用例
调试规则匹配意图无结果问题
调试解决模型识别意图coredump问题
优化规则匹配、模型识别两者的意图结果融合逻辑


Hyper-V虚拟机配置文件夹和存储地址:
C:\ProgramData\Microsoft\Windows\Hyper-V
D:\hyper-v\kylin2403




20250123
intent集成hnsw search模块
intent集成sort模型模块
调试intent模型识别、规则匹配等模块编译问题
修改转正述职报告



20250122
开发intent/sort模型预处理逻辑
开发intent/sort模型推理逻辑
开发intent/sort模型后处理功能
撰写转正述职报告




20250121
优化image_embedding外层错误码逻辑
开发intent/HnswSearcher模块规则解析等初始化功能接口
开发intent/HnswSearcher模块搜索功能接口
编写转正述职报告


image_embedding图像resize后数据不一致



20250120
研究graphicmagick配置选项，修改其图像量化深度
编译更新graphicmagick库
修改image_embedding的图像处理流程
调测图像原始RGB像素量化范围、尺寸缩放后像素量化范围、矩阵转换后归一化值等



需求、产品、开发、测试流程环节不规范标准，不可预测性较大


开天项目外部关联性较大，因外部可控因素导致不可预测性较大
开天项目产品面向To C客户群，与To B产品场景不同，用户体验要求较高
AIPC端产品在技术开发层面直接面向硬件或系统层开发，难点较多，有效评估不易；


应用本身自成体系
需要熟悉、学习等预研方向
不可预测性太高
修改矩阵空间转换过程


(base) root@docker-desktop:~/vcpkg/packages/graphicsmagick_x64-linux# egrep -Rn "QuantumDepth" .
./include/wand/magick_wand.h:81:  *MagickGetQuantumDepth(unsigned long *),
./include/wand/wand_symbols.h:239:#define MagickGetQuantumDepth GmMagickGetQuantumDepth


./include/magick/colorspace.h:19:#if (QuantumDepth == 8) || (QuantumDepth == 16)
./include/magick/colorspace.h:31:#elif (QuantumDepth == 32)
./include/magick/magick_config_api.h:7:#define QuantumDepth 16
./include/magick/alpha_composite.h:45:#if QuantumDepth > 16
./include/magick/magick_config.h:599:#define QuantumDepth 16
./include/magick/version.h:60:#if (QuantumDepth == 8)
./include/magick/version.h:61:#define MagickQuantumDepth  "Q8"
./include/magick/version.h:62:#elif (QuantumDepth == 16)
./include/magick/version.h:63:#define MagickQuantumDepth  "Q16"
./include/magick/version.h:64:#elif (QuantumDepth == 32)
./include/magick/version.h:65:#define MagickQuantumDepth  "Q32"
./include/magick/version.h:71:  MagickReleaseDate " " MagickQuantumDepth " " MagickWebSite
./include/magick/image.h:30:#if !defined(QuantumDepth)
./include/magick/image.h:31:#  define QuantumDepth  16
./include/magick/image.h:34:#if (QuantumDepth == 8)
./include/magick/image.h:57:#elif (QuantumDepth == 16)
./include/magick/image.h:80:#elif (QuantumDepth == 32)
./include/magick/image.h:122:#  error "Specified value of QuantumDepth is not supported"
./include/Magick++/Image.h:886:    // 65536 entries depending on the value of QuantumDepth when


Binary file ./debug/lib/libgraphicsmagick.a matches
Binary file ./lib/libgraphicsmagick.a matches


QuantumDepth

I20250117 17:44:09.010612 48272 log_stream.cc:21] color Pixel at (0, 0) - R: 102, G: 101, B: 101
I20250117 17:44:09.010617 48272 log_stream.cc:21] color Pixel at (1, 0) - R: 98, G: 97, B: 97
I20250117 17:44:09.010619 48272 log_stream.cc:21] color Pixel at (2, 0) - R: 95, G: 94, B: 94
I20250117 17:44:09.010622 48272 log_stream.cc:21] color Pixel at (0, 1) - R: 105, G: 104, B: 104
I20250117 17:44:09.010624 48272 log_stream.cc:21] color Pixel at (1, 1) - R: 101, G: 100, B: 100
I20250117 17:44:09.010627 48272 log_stream.cc:21] color Pixel at (2, 1) - R: 98, G: 97, B: 97
I20250117 17:44:09.010629 48272 log_stream.cc:21] color Pixel at (0, 2) - R: 110, G: 109, B: 109
I20250117 17:44:09.010632 48272 log_stream.cc:21] color Pixel at (1, 2) - R: 105, G: 104, B: 104
I20250117 17:44:09.010635 48272 log_stream.cc:21] color Pixel at (2, 2) - R: 101, G: 100, B: 100
I20250117 17:44:09.010685 48272 log_stream.cc:21] rgb Pixel at (0, 0) - R: 99, G: 101, B: 100
I20250117 17:44:09.010689 48272 log_stream.cc:21] rgb Pixel at (1, 0) - R: 0, G: 0, B: 0
I20250117 17:44:09.010691 48272 log_stream.cc:21] rgb Pixel at (2, 0) - R: 0, G: 0, B: 0


quality()
quantizeColors()
quantizeTreeDepth()
scene()
depth()

pixelColor(x, y)
pixelColor



  // Magick::PixelPacket *pixels = image.getPixels(0, 0, image_size_, image_size_);
  // Magick::Color color = pixels[y * width + x];
  std::vector<unsigned char> rgbBuffer(image_size_ * image_size_ * image_channels_);
  // image.writePixels(Magick::RGBQuantum, rgbBuffer.data());




IPC: ws, grpc, dbus
sense：sendword, intent, ner,
decision:
action:search(text content, image content, file name, app name), app manage, system manage, IO device manage(screen, mouse, keyboard), file format convertion,



20250117
研究graphicmagick封装层Image实现
分析graphicmagick封装层Color模块
分析graphicmagick封装层Pixels模块
修改magick_config，调测Image像素点量化范围


编译时配置
研究graphicmagick底层量化过程
调测图像处理像素点分布范围
调测python脚本图像像素点分布范围
调试image_embedding预处理时像素点量化不一致问题


20250116
探讨Freeswitch集群部署方案
调试image_embedding预处理时像素点量化不一致问题
修改sysfunc.get_app_by_key兼容性
添加sysfunc应用管理的搜索已安装接口




20250115
调测sysfunc.app.install接口，定位GDBus.Error:org.freedesktop.DBus.Error.NotSupported: dbus limit control,not supported
修改app_manager中安装接口为同步调用，解决异步并发调用dbus接口时二次调用阻塞问题；
开发sysfunc.app.installable接口
调试麒麟应用商店搜索dbus接口

测sysfunc.app.installable接口流程，



[

  {'appname': 'wechat-devtools',
  'discription': '为了帮助开发者简单和高效地开发和调试微信小程序，我们在原有的公众号网页调试工具的基础上，推出了全新的微信开发者工具，集成了公众号网页调试和小程序调试两种开发模式。',
  'displayname_cn': '微信开发者工具',
  'icon': '/usr/share/kylin-software-center/data/icons/wechat-devtools.png',
  'version': ''},

  {'appname': 'kylin-wine-wechat',
  'discription': '微信，超过10亿人使用，能够通过网络给好友发送文字消息、表情和图片，还可以传送文件，与朋友视频聊天，让你的沟通更方便。并提供有多种语言界面。',
  'displayname_cn': '微信（Kylin-wine版）',
  'icon': '/home/lit/.cache/uksc/icons/kylin-wine-wechat.png',
  'version': ''},

  {'appname': 'kylin-kwre-wechat',
  'discription': '微信，超过10亿人使用，能够通过网络给好友发送文字消息、表情和图片，还可以传送文件，与朋友视频聊天，让你的沟通更方便。并提供有多种语言界面。',
  'displayname_cn': '微信（Win32版）',
  'icon': '/usr/share/kylin-software-center/data/icons/kylin-kwre-wechat.png',
  'version': ''}

]


lit@lit-pc:~$ dbus-send --session --print-reply --dest="com.kylin.softwarecenter.getsearchresults" /com/kylin/softwarecenter/getsearchresults com.kylin.getsearchresults.get_search_result string:"wechat"
method return time=1739241609.713889 sender=:1.185 -> destination=:1.828 serial=256 reply_serial=2
array [
	array [
	 dict entry(
		string "appname"
		string "wechat-devtools"
	 )
	 dict entry(
		string "discription"
		string "为了帮助开发者简单和高效地开发和调试微信小程序，我们在原有的公众号网页调试工具的基础上，推出了全新的微信开发者工具，集成了公众号网页调试和小程序调试两种开发模式。"
	 )
	 dict entry(
		string "displayname_cn"
		string "微信开发者工具"
	 )
	 dict entry(
		string "icon"
		string "/usr/share/kylin-software-center/data/icons/wechat-devtools.png"
	 )
	 dict entry(
		string "version"
		string ""
	 )
	]
	array [
	 dict entry(
		string "appname"
		string "kylin-wine-wechat"
	 )
	 dict entry(
		string "discription"
		string "微信，超过10亿人使用，能够通过网络给好友发送文字消息、表情和图片，还可以传送文件，与朋友视频聊天，让你的沟通更方便。并提供有多种语言界面。"
	 )
	 dict entry(
		string "displayname_cn"
		string "微信（Kylin-wine版）"
	 )
	 dict entry(
		string "icon"
		string "/home/lit/.cache/uksc/icons/kylin-wine-wechat.png"
	 )
	 dict entry(
		string "version"
		string ""
	 )
	]
	array [
	 dict entry(
		string "appname"
		string "kylin-kwre-wechat"
	 )
	 dict entry(
		string "discription"
		string "微信，超过10亿人使用，能够通过网络给好友发送文字消息、表情和图片，还可以传送文件，与朋友视频聊天，让你的沟通更方便。并提供有多种语言界面。"
	 )
	 dict entry(
		string "displayname_cn"
		string "微信（Win32版）"
	 )
	 dict entry(
		string "icon"
		string "/usr/share/kylin-software-center/data/icons/kylin-kwre-wechat.png"
	 )
	 dict entry(
		string "version"
		string ""
	 )
	]
]

dbus-send --session --print-reply --dest="com.kylin.softwarecenter.getsearchresults" /com/kylin/softwarecenter/getsearchresults com.kylin.getsearchresults.get_search_result string:"wechat"

dbus-send --session --print-reply --dest="com.kylin.softwarecenter.getsearchresults" /com/kylin/softwarecenter/getsearchresults com.kylin.getsearchresults.get_search_result string:"gdb"

dbus-send --session --print-reply --dest="com.kylin.softwarecenter.getsearchresults" /com/kylin/softwarecenter/getsearchresults com.kylin.softwarecenter.getsearchresults.get_search_result  string:"gdb"

dbus-send --system --print-reply --dest="com.kylin.softwarecenter.getsearchresults" /com/kylin/softwarecenter/getsearchresults com.kylin.softwarecenter.getsearchresults.get_search_result  string:"gdb"

dbus-send --system --print-reply --dest="com.kylin.softwarecenter.getsearchresults" /com/kylin/softwarecenter/getsearchresults com.kylin.softwarecenter.getsearchresults.get_search_result  string:"gdb"

dbus-send --system --print-reply --dest="com.kylin.softwarecenter.getsearchresults" /com/kylin/softwarecenter/getsearchresults com.kylin.softwarecenter.getsearchresults.getsearchresults  string:"gdb"


dbus-send --system --print-reply --dest="com.kylin.systemupgrade" /com/kylin/systemupgrade com.kylin.systemupgrade.interface.InstallPackages  array:string:"gdb"



20250114
修改联调sysfunc.app.get接口功能逻辑(添加未安装应用状态)
联调sysfunc.app.install接口功能
参加年度KO会议




20250113
梳理研究可安装应用搜索dbus接口
调试CMake可安装应用搜索gdbus接口代码生成
设计可安装应用搜索功能模块
开发可安装应用搜索功能模块




E20250113 17:32:34.183627 23353 log_stream.cc:29] app manager center proxy_new_for_bus_sync error:
Error calling StartServiceByName for com.kylin.softwarecenter.getsearchresults: Cannot do system-bus activation with no user

(process:23353): GLib-GIO-CRITICAL **: 17:32:34.183: g_dbus_proxy_call_sync_internal: assertion 'G_IS_DBUS_PROXY (proxy)' failed
Segmentation fault (core dumped)



搜索接口
提供DBUS接口
SERVICE: "com.kylin.softwarecenter.getsearchresults"
PATH: "/com/kylin/softwarecenter/getsearchresults"
接口名称	作用说明	参数说明	备注
get_search_result
(QString appName)	获取商店含有关键字的上架应用	in_signature='s' {keyword}
out_signature='aa{ss}'	返回样例：
[{“appName”:”xxx”,
“displayname_cn”:”中文名”，
”icon”:”iconPath”,
”version”;”1.0.0”,
”description”:””}]



20250110
调测CMake自动化生成kylin_system_upgrade接口代码
修改软件安装同步调用和线程安全逻辑
修改软件安装完成信号捕获功能
添加软件安装时异常捕获处理逻辑


问题: kylin system update dbus应用安装接口提示 "其他任务正在更新升级中，请稍后再试。"
解决方法: (kylin系统bug，安装补丁包解决)
2403-upgrade.tar.gz
sudo dpkg -i *.deb



20250109
编写sysfunc测试程序，搭建自测环境
排查解决ukui-search守护进程dbus服务无法连接问题
调测sysfunc.app.get功能接口
调测sysfunc.app.install功能接口，定位阻塞"其他任务正在更新升级中"问题


(1, '其他任务正在更新升级中，请稍后再试。')



  // std::vector<const gchar*> c_strings(2);
  // c_strings[0] = package_name.c_str();
  // c_strings[1] = NULL; // 添加 NULL 终止符
  // auto in_params_strv = g_variant_new_strv(c_strings.data(), 1);
  // GVariant* in_params = g_variant_new("(as)", in_params_strv);
  // g_variant_unref(in_params_strv);




I20250109 16:43:08.819300  7908 log_stream.cc:21] params: kylin-video, gdb
I20250109 16:43:08.819355  7908 log_stream.cc:21] app manager dbus name: com.kylin.systemupgrade
I20250109 16:43:08.819360  7908 log_stream.cc:21] app manager dbus path: /com/kylin/systemupgrade
I20250109 16:43:08.819363  7908 log_stream.cc:21] app manager dbus interface: com.kylin.systemupgrade.interface

I20250109 16:43:08.822460  7908 log_stream.cc:21] app manager dbus method: InstallPackages
I20250109 16:43:09.262569  7914 log_stream.cc:21] app manager received signal InstallDetectStatus
	params: (false, '#0210')
I20250109 16:43:09.262611  7914 log_stream.cc:21] app manager received signal UpdateInstallFinished
	params: (false, ['k', 'y', 'l', 'i', 'n', '-', 'v', 'i', 'd', 'e', 'o'], ' ', 'Package is not in cache')

I20250109 16:43:10.173252  7908 log_stream.cc:21] app manager call InstallPackages kylin-video return: (0, '')


I20250109 16:43:10.173382  7908 log_stream.cc:21] app manager dbus method: InstallPackages
I20250109 16:43:10.175218  7908 log_stream.cc:21] app manager call InstallPackages gdb return: (1, '其他任务正在更新升级中，请稍后再试。')
I20250109 16:43:10.175284  7908 log_stream.cc:21] callback({"cmd":"sysfunc.app.install","eot":true,"private":"test sysfunc","sessionId":101,"state":{"code":0,"extend":"","info":"success"}})



(process:7908): GLib-GObject-WARNING **: 16:43:08.822: invalid (NULL) pointer instance

(process:7908): GLib-GObject-CRITICAL **: 16:43:08.822: g_signal_emit_by_name: assertion 'G_TYPE_CHECK_INSTANCE (instance)' failed


busctl list 2332

systemctl status session-4.scope


/run/systemd/transient/session-4.scope; transient


I20250109 15:06:03.172401 803487 log_stream.cc:21] params: gdb, browser360-cn-stable
I20250109 15:06:03.172430 803487 log_stream.cc:21] app manager dbus name: com.kylin.systemupgrade
I20250109 15:06:03.172433 803487 log_stream.cc:21] app manager dbus path: /com/kylin/systemupgrade
I20250109 15:06:03.172436 803487 log_stream.cc:21] app manager dbus interface: com.kylin.systemupgrade.interface
I20250109 15:06:03.196077 803487 log_stream.cc:21] app manager dbus method: InstallPackages
I20250109 15:06:03.816720 803491 log_stream.cc:21] app manager received signal InstallDetectStatus from :1.85
I20250109 15:06:03.817231 803491 log_stream.cc:21] app manager received signal UpdateInstallFinished from :1.85
I20250109 15:06:03.817327 803491 log_stream.cc:21] app manager received signal UpdateInstallFinished : <85>^?
I20250109 15:06:04.851660 803487 log_stream.cc:21] InstallPackages gdb return: 0
I20250109 15:06:04.851752 803487 log_stream.cc:21] get_app_by_key():gdb
I20250109 15:06:04.855350 803487 log_stream.cc:21] get_app_by_key():[]
I20250109 15:06:04.855430 803487 log_stream.cc:21] error: [json.exception.type_error.309] cannot use insert() with null
I20250109 15:06:04.855440 803487 log_stream.cc:21] callback({"cmd":"sysfunc.app.install","data":null,"eot":true,"private":"test sysfunc","sessionId":101,"state":{"code":500,"extend":"","info":"[json.exception.type_error.309] cannot use insert() with null"}})
I20250109 15:06:04.855448 803487 log_stream.cc:21] kModuleDestroy pInstance = 0x8b5640
I20250109 15:06:04.855454 803487 log_stream.cc:21] [printer] PrinterScanner::~PrinterScanner



获取函数指针: kModuleDestroy

(process:803487): GLib-GObject-WARNING **: 15:06:03.195: invalid (NULL) pointer instance
(process:803487): GLib-GObject-CRITICAL **: 15:06:03.196: g_signal_emit_by_name: assertion 'G_TYPE_CHECK_INSTANCE (instance)' failed
(process:803487): GLib-CRITICAL **: 15:06:03.817: the GVariant format string '(s)' has a type of '(s)' but the given value has a type of '(basss)'
(process:803487): GLib-CRITICAL **: 15:06:03.817: g_variant_get: assertion 'valid_format_string (format_string, TRUE, value)' failed
(process:803487): GLib-CRITICAL **: 15:06:04.851: the GVariant format string '(i)' has a type of '(i)' but the given value has a type of '(is)'
(process:803487): GLib-CRITICAL **: 15:06:04.851: g_variant_get: assertion 'valid_format_string (format_string, TRUE, value)' failed
App info database currunt connection name: "932862936"




Create signalTransformer Interface Failed Because:  QDBusError("org.freedesktop.DBus.Error.Spawn.FileInvalid", "Cannot do system-bus activation with no user\n")
QSqlQuery::prepare: database not open
QSqlError("", "Driver not loaded", "Driver not loaded") QSqlError("", "Driver not loaded", "Driver not loaded") "" QMap()


export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/dbus/system_bus_socket

busctl status

busctl tree
busctl list

Create signalTransformer Interface Failed Because:  QDBusError("org.freedesktop.DBus.Error.NotSupported", "Using X11 for dbus-daemon autolaunch was disabled at compile time,
set your DBUS_SESSION_BUS_ADDRESS instead")

QSqlQuery::prepare: database not open
QSqlError("", "Driver not loaded", "Driver not loaded") QSqlError("", "Driver not loaded", "Driver not loaded") "" QMap()



20250108
学习GDBusProxy接口使用流程
开发kylin dbus软件包安装功能
开发kylin dbus软件安装状态信号捕获功能
开发sysfunc.app.install功能接口


20250107
安装操作系统补丁包kylin-system-updater及其依赖包，排查解决kylin-backup-server无安装源问题
研究kylin从源安装软件包的dbus接口及gdbus使用方法
调研安装软件包时InstallPackages对应信号的捕获及使用方法
设计应用管理app_manager模块



20250106
重构设计原CHnwsModule模块
研究kddbus signal功能接口集成方法
开发kddbus集成app status change signal接口
开发sysfunc.app.get功能接口


add_custom_command(
  OUTPUT ${PROJECT_SOURCE_DIR}/sysfunc/inc/kylin_system_upgrade.h
  OUTPUT ${PROJECT_SOURCE_DIR}/sysfunc/inc/kylin_system_upgrade.c
  COMMAND gdbus-codegen
  ARGS --generate-c-code kylin_system_upgrade
       --c-namespace kdm
       --interface-prefix com.kylin.systemupgrade.
       --output-directory ${PROJECT_SOURCE_DIR}/sysfunc
  ${PROJECT_SOURCE_DIR}/sysfunc/com.kylin.systemupgrade.xml
)


add_custom_command(
	COMMAND gdbus-codegen
	ARGS --generate-c-code kylin_system_upgrade --c-namespace kdm
	--output ${PROJECT_SOURCE_DIR}/sysfunc/inc/kylin_system_upgrade.h
	--output ${PROJECT_SOURCE_DIR}/sysfunc/inc/kylin_system_upgrade.c
	--interface-prefix com.kylin.systemupgrade.
	${PROJECT_SOURCE_DIR}/sysfunc/com.kylin.systemupgrade.xml
)

add_custom_command(
	OUTPUT ${PROJECT_SOURCE_DIR}/sysfunc/inc/kylin_system_upgrade.h
	OUTPUT ${PROJECT_SOURCE_DIR}/sysfunc/inc/kylin_system_upgrade.c
	COMMAND gdbus-codegen
	ARGS --generate-c-code kylin_system_upgrade
	--c-namespace kdm
	--interface-prefix com.kylin.systemupgrade.
	${PROJECT_SOURCE_DIR}/sysfunc/com.kylin.systemupgrade.xml
)

add_custom_command(
  TARGET sysfunc
  PRE_BUILD
  COMMAND gdbus-codegen
  ARGS --c-namespace kdm
       --generate-c-code kylin_system_upgrade
       --interface-prefix com.kylin.systemupgrade.
       --output-directory ${PROJECT_SOURCE_DIR}/sysfunc
  ${PROJECT_SOURCE_DIR}/sysfunc/com.kylin.systemupgrade.xml
  COMMAND mv ARGS ${PROJECT_SOURCE_DIR}/sysfunc/kylin_system_upgrade.h
                  ${PROJECT_SOURCE_DIR}/sysfunc/inc/
  COMMAND mv ARGS ${PROJECT_SOURCE_DIR}/sysfunc/kylin_system_upgrade.c
                  ${PROJECT_SOURCE_DIR}/sysfunc/src/
)

--generate-c-code kylin_system_upgrade

gdbus-codegen --output sysfunc/inc/kylin_system_upgrade.h --output sysfunc/inc/kylin_system_upgrade.c --c-namespace kdm --interface-prefix com.kylin.systemupgrade. sysfunc/com.kylin.systemupgrade.xml

gdbus-codegen --output sysfunc/inc/kylin_system_upgrade.h --output sysfunc/inc/kylin_system_upgrade.c --generate-c-code kylin_system_upgrade --c-namespace kdm --interface-prefix com.kylin.systemupgrade. sysfunc/com.kylin.systemupgrade.xml


gdbus-codegen --output-directory sysfunc --generate-c-code kylin_system_upgrade --c-namespace kdm --interface-prefix com.kylin.systemupgrade. sysfunc/com.kylin.systemupgrade.xml


gdbus-codegen --output-directory kddbus --generate-c-code KdserviceDbus --c-namespace KdserviceDbus --interface-prefix com.knowdee.Service. kddbus/com.knowdee.Service.xml

gdbus-codegen --output-directory kddbus --generate-c-code KdserviceDbus --c-namespace KdserviceDbus --interface-prefix com.knowdee.Service. kddbus/com.knowdee.Service.xml

gdbus-codegen --output kddbus/inc/KdserviceDbus.h --output kddbus/src/KdserviceDbus.c --generate-c-code KdserviceDbus --c-namespace KdserviceDbus --interface-prefix com.knowdee.Service. kddbus/com.knowdee.Service.xml


OUTPUT  "${PROJECT_SOURCE_DIR}/kddbus/inc/KdserviceDbus.h"  "${PROJECT_SOURCE_DIR}/kddbus/src/KdserviceDbus.c"
COMMAND gdbus-codegen
ARGS --generate-c-code KdserviceDbus
--c-namespace KdserviceDbus
--interface-prefix com.knowdee.Service.
${PROJECT_SOURCE_DIR}/kddbus/com.knowdee.Service.xml



20250103
开发文本向量化预处理功能
开发文本向量化模型推理功能
开发文本向量化后处理功能
kt-lib/intent集成文本向量化



20250102
优化原有解密模块CAesGcmModule
重构设计原有intent规则匹配
开发intent规则匹配模块
重构设计原有intent文本向量化



20241231
研究kt-lib/intent模块结构组成与调用流程
梳理kt-lib/intent模块内的组件模块划分
梳理kt-lib/intent模块内部功能接口
重构设计kt-lib/intent模块工程


// 1 模型和配置信息解码(加载规则)
CAesGcmModule* caceGcmModel;

// 2 意图识别 IR(intent recognition)

	// 2.1 规则匹配意图(rule match intent)
	CRuleMatchIntent* ruleMatchIntent;

	// 2.2 模型匹配意图(model match intent)
		// 2.2.1 文本向量化
		CEmbeddingModule* cmodel;
		// 2.2.2 向量化后检索——topN
		CHnwsModule* chnwModel;
		// 2.2.3 结果排序——精排top1
		CSortModel* smodel;

20241231
研究kt-lib/intent模块结构组成与调用流程
梳理kt-lib/intent模块内的组件模块划分
梳理kt-lib/intent模块内部功能接口
重构设计kt-lib/intent模块工程



20241230
定位解决graphicsmagick三方依赖符号查找失败问题
重新编译kt-lib/logger arm64版本动态库
调试test_kdm_image_embedding编译
测试test_kdm_image_embedding图像向量化功能



(gdb) set environment LD_LIBRARY_PATH=../lib:$LD_LIBRARY_PATH
(gdb) b main
Breakpoint 1 at 0x39f4
(gdb) b main.cc:79
No symbol table is loaded.  Use the "file" command.
Make breakpoint pending on future shared library load? (y or [n]) y
Breakpoint 2 (main.cc:79) pending.
(gdb) r
Starting program: /data/lit/image/bin/bin/test_kdm_image_embedding
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/aarch64-linux-gnu/libthread_db.so.1".

Program received signal SIGSEGV, Segmentation fault.
0x0000007ff4464774 in _GLOBAL__sub_I_logging.cc () from ../lib/libglog.so.1
(gdb) bt
#0  0x0000007ff4464774 in _GLOBAL__sub_I_logging.cc () from ../lib/libglog.so.1
#1  0x0000007ff7fda8b4 in call_init (l=<optimized out>, argc=argc@entry=1, argv=argv@entry=0x7ffffff0d8, env=env@entry=0x7ffffff0e8) at dl-init.c:72
#2  0x0000007ff7fda9b4 in call_init (env=0x7ffffff0e8, argv=0x7ffffff0d8, argc=1, l=<optimized out>) at dl-init.c:30
#3  _dl_init (main_map=0x7ff7fff210, argc=1, argv=0x7ffffff0d8, env=0x7ffffff0e8) at dl-init.c:119
#4  0x0000007ff7fcd184 in _dl_start_user () from /lib/ld-linux-aarch64.so.1
Backtrace stopped: previous frame identical to this frame (corrupt stack?)
(gdb)



20241227
编译安装kt-lib/logger arm64版本
编译安装graphicsmagick及其依赖 arm64版本静态库
调试test_kdm_image_embedding编译报错问题
调试graphicsmagick三方依赖符号查找失败问题



ubuntu20.04 cross platform compile arm64 bin and lib:
apt install gcc-aarch64-linux-gnu
apt install g++-aarch64-linux-gnu
vcpkg install graphicsmagick:arm64-linux

[100%] Linking CXX executable test_kdm_image_embedding
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `deflateInit_'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `gzerror'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `lzma_stream_decoder'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `BZ2_bzDecompress'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `BZ2_bzread'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `deflateInit2_'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `BZ2_bzCompressInit'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `BZ2_bzwrite'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `BZ2_bzCompressEnd'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `zlibVersion'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `BZ2_bzerror'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `gzseek'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `FT_Load_Glyph'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `gzeof'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `FT_Get_Kerning'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `BZ2_bzopen'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `deflate'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `gzflush'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `FT_Outline_Get_BBox'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `deflateEnd'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `FT_Get_Glyph'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `gztell'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `lzma_memusage'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `FT_Init_FreeType'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `crc32'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `FT_Glyph_Transform'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `FT_Get_Char_Index'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `inflate'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `SharpYuvConvert'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `lzma_lzma_preset'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `inflateInit2_'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `inflateInit_'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `BZ2_bzDecompressEnd'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `BZ2_bzDecompressInit'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `SharpYuvInit'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `inflateEnd'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `FT_Outline_Decompose'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `BZ2_bzCompress'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `FT_Glyph_To_Bitmap'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `FT_Set_Charmap'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `inflateReset2'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `inflateReset'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `FT_Vector_Transform'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `deflateReset'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `gzwrite'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `gzopen'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `FT_Select_Charmap'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `lzma_code'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `FT_Done_FreeType'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `FT_Done_Glyph'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `BZ2_bzflush'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `FT_Set_Char_Size'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `gzclose'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `SharpYuvGetConversionMatrix'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `gzgets'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `FT_New_Face'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `BZ2_bzclose'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `gzread'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `FT_Done_Face'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `adler32'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `lzma_end'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `inflateValidate'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `deflateParams'
/usr/bin/ld: ../src/libkdm_image_embedding.so: undefined reference to `lzma_stream_encoder'
collect2: error: ld returned 1 exit status

gdb -tui ./exe
(gdb) tui enable

一旦进入了 GDB，你可以使用 layout 命令来切换到不同的布局，从而开启 TUI 模式。以下是几个常用的 layout 子命令：
layout src：显示源代码窗口。
layout asm：显示汇编代码窗口。
layout split：同时显示源代码和汇编代码窗口。
layout reg：显示寄存器窗口。


20241226
开发kt-lib/ner中match模型后处理支持batch模式
调测kt-lib/ner中match模型后处理支持batch模式
定位解决kt-lib/ner中match模型后处理解析batch输出异常问题
调测kt-lib/ner中match模型整体功能


20241225
修改kdm asr-proxy以submodule方式集成到kds kd-asr-proxy中
定位解决kd-asr-proxy服务libhv解析请求消息异常coredump问题
构建kd-asr-proxy debug6.0版本镜像，同高宇联调测试语音识别结果为空情况
调测kt-lib/ner中match模型预处理支持batch模式




git submodule add git@gitlab.knowdee.com:kdm/cpp/knowdee/asr-proxy.git third_party/asr-proxy
git add .gitmodules third_party/asr-proxy
git commit -m "add kdm asr-proxy as thirdparty with submodule"


20241224
集成开发libhv网络库，替换kd-asr-proxy服务中mongoose
调测kd-asr-proxy中libhv网络库http服务功能
调测kt-lib/ner中match模型推理支持batch模式时coredump问题
开发kt-lib/ner中match模型预处理支持batch模式



vcpkg install libhv

libhv provides CMake targets:

  # this is heuristically generated, and may not be correct
  find_package(libhv CONFIG REQUIRED)
  target_link_libraries(main PRIVATE hv_static)

20241223
优化修改kt-lib/ner中uie模型结果输出接口
开发kt-lib/ner预置意图与固定槽位映射信息Json解析功能
开发kt-lib/ner中match模型推理支持batch模式
下载安装三方依赖libhv网络库



20241221
定位分析山西热力线上kd-asr-proxy服务运行24小时后http网络连接不上问题
调研三方依赖httplib底层网络IO多路复用机制(select/poll)，适合追求简单性和快速开发的小型项目
调研三方依赖uWebSocket底层网络IO多路复用机制(libuv:epoll/kqueue/IOCP)，特别适合对实时通信有要求的应用(游戏服务器或聊天应用)
调研三方依赖libhv底层网络IO多路复用机制(epoll/kqueue)，针对需要高性能和多协议支持的大规模应用
下载安装三方依赖libhv网络库



#问题表现： kd-asr-proxy服务运行24小时后http网络连接不上问题
排查网络库mongoose接收http delete请求时，报错:"connection reset by peer"
mongoose所用IO多路复用select调用: 1036(fd) > 1024(FD_SETSIZE)

问题分析：cti delete请求少发送 --> kd-asr-proxy服务udp port占用逐渐增加 --> 当前asr_service进程占用fd逐渐增加 1036(fd) > 1024(FD_SETSIZE)


2024-12-19 01:45:00    mongoose.cpp:1261:http_cb kds---->5  0 0
2024-12-19 01:45:00    mongoose.cpp:3141:mg_mgr_ 1 -- tchrc
2024-12-19 01:45:00    mongoose.cpp:3102:mg_iote kds---->select active(r/w) connect num = 2
2024-12-19 01:45:00    mongoose.cpp:3136:mg_mgr_ kds---->poll current time = 1734572700154
2024-12-19 01:45:00    mongoose.cpp:3141:mg_mgr_ 174 -w tchrc
2024-12-19 01:45:00    mongoose.cpp:2737:ll_writ 174 tuc 39/39 0
2024-12-19 01:45:00    mongoose.cpp:3141:mg_mgr_ 1 r- tchrc
2024-12-19 01:45:00  E mongoose.cpp:2966:accept_ 1036 > 1024
2024-12-19 01:46:57  E mongoose.cpp:2966:accept_ 1060 > 1024
2024-12-19 01:46:57  E mongoose.cpp:2966:accept_ 1060 > 1024
2024-12-19 01:47:08  E mongoose.cpp:2966:accept_ 1035 > 1024
2024-12-19 01:47:08  E mongoose.cpp:2966:accept_ 1035 > 1024
2024-12-19 01:47:40  E mongoose.cpp:2966:accept_ 1035 > 1024
2024-12-19 01:47:40  E mongoose.cpp:2966:accept_ 1035 > 1024
2024-12-19 01:47:43  E mongoose.cpp:2966:accept_ 1039 > 1024
2024-12-19 01:47:43  E mongoose.cpp:2966:accept_ 1039 > 1024
2024-12-19 01:54:35  E mongoose.cpp:2966:accept_ 1037 > 1024
2024-12-19 01:54:35  E mongoose.cpp:2966:accept_ 1037 > 1024
2024-12-19 01:55:09  E mongoose.cpp:2966:accept_ 1045 > 1024
2024-12-19 01:56:35  E mongoose.cpp:2966:accept_ 1038 > 1024





20241220
研究kdm-asr-proxy讯飞语音识别结果回传逻辑
定位分析kd-asr-proxy服务镜像5.0版本存在语音识别结果为空的问题
修改优化kdm-asr-proxy讯飞语音识别结果回传逻辑
调测kdm-asr-proxy编译和运行报错等问题

加密
鉴权
限流
削峰填谷
异地多活
异地灾备
HA
CA/CK

类似联想开天 AIPC 等端设备上通常可用硬件资源比较紧张，尤其当多个 AI 模型部署同时运行，占用资源较高，如何在有限的条件下，实现端设备交互智能化，存在极大挑战。

已完成初步改造和沉淀的语音相关KDM/KDS，在架构设计和代码质量等方面仍存在历史性的负债，还需深入优化与设计。


20241219
定位排查uie模型预处理时coredump问题
开发uie模型后处理支持batch模式
调测uie模型后处理支持batch模式
调测uie模型推理整体功能


20241218
山西热力线上测试kd-asr-proxy镜像5.0版本，定位语音识别结果存在为空、讯飞网络连接10秒逾期关闭、udp端口号未释放问题(cti少发一次delete请求造成)
开发uie模型预处理支持batch模式
调测uie模型预处理支持batch模式
排查uie模型预处理时coredump问题


20241217
修改kd-asr-proxy三方依赖的boost, aws, kdm_asr_proxy，解决调用asr引擎厂商出错问题
构建打包kd-asr-proxy debug版本镜像5.0版本
联调kd-asr-proxy debug版本镜像4.0版本和5.0版本
更新修改kdm_asr_proxy三方依赖的boost, aws


20241216
开发uie模型onnx推理支持batch模式
配合高宇测试kd-asr-proxy服务
排查kd-asr-proxy创建会话时调用asr引擎厂商出错问题
构建打包kd-asr-proxy debug版本镜像4.0


LOG_DEBUG("ASR OPTIONS: AsrRenderId {} {}", asropt->_iAsrRenderId, asropt->_iAsrRenderGiven);



kds: kd-asr-proxy
OnSessionCreate()


kdm: asr-proxy
2 : RECO_ASR_LENOVO_HTTP
3 : RECO_ASR_IFLYTEK


2. asr result is empty:


20000001

家里测试环境172.70.10.210:
20000002
2602

msgFactory.h
speech::msgFactory::processMsg
speech::msgFactory::processIflyMsg
speech::msgFactory::createMsg
printf("CreateMsg Index = %d, point = %p\n", iIndex, _pMsg);


kd-asr-proxy.log:
"msg":"recieve result sid , file /var/asr_record/f9ab4b4b-e44d-420a-94da-3909070a481a_0015.wav, result , index 15, pos 0, beginTime 46900, endTime 50080"



1. http connect timeout:
mg_iotest（select）

mg_mgr_poll
accept_conn


LOG(LL_INFO,
  ("kds---->%d %d\n%.*s", ev, hm.message.len, (int) c->recv.len, c->recv.buf));


LOG(LL_DEBUG, ("%lu accepted %s", c->id, buf));


LOG(LL_INFO, ("%lu accepting on %s", c->id, url));

2024-12-12 03:29:16  I mongoose.cpp:3056:mg_list 1 accepting on 172.70.10.210:10208



URL="http://172.70.10.210:30208/asr/session"
CONCURRENT=1000 # 并发请求数
TOTAL_REQUESTS=10000  # 总请求数


# 使用 xargs 发起并发请求
seq $TOTAL_REQUESTS | xargs -n 1 -P $CONCURRENT -I {} curl -s -o /dev/null -w "time_total: %{time_total}s\n" $URL

curl -s -o /dev/null -w "time_total: %{time_total}s\n" http://172.70.10.210:30208/asr/session

curl -s -o /dev/null -w "time_total: %{time_total}s\n" http://172.70.10.210:30208/asr/session


curl --request POST -s -o /dev/null -w "time_total: %{time_total}s\n" \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: PostmanRuntime-ApipostRuntime/1.1.0' \
  --data '{
    "sessionID": "f0459ab4-4f04-4982-b7db-f810fee12f0c_50032"
}' \
  http://172.70.10.210:30208/asr/session


curl --request POST -s -w "time_total: %{time_total}s\n" --header 'Content-Type: application/json'  --data '{"sessionID": "f0459ab4-4f04-4982-b7db-f810fee12f0c_50032"}' http://172.70.10.210:30208/asr/session


curl --request DELETE \
  --url http://172.30.207.30:30208/asr/session \
  --header 'Accept: */*' \
  --header 'Accept-Encoding: gzip, deflate, br' \
  --header 'Connection: keep-alive' \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: PostmanRuntime-ApipostRuntime/1.1.0' \
  --data '{
    "sessionID": "f0459ab4-4f04-4982-b7db-f810fee12f0c_50032"
}'

curl http://172.30.207.30:30208/asr/session
 

curl --request DELETE --url http://172.30.207.30:30208/asr/session --header 'Accept: */*' --header 'Accept-Encoding: gzip, deflate, br' --header 'Connection: keep-alive' --header 'Content-Type: application/json' --header 'User-Agent: PostmanRuntime-ApipostRuntime/1.1.0'  --data '{"sessionID": "f0459ab4-4f04-4982-b7db-f810fee12f0c_50032"}'



搜索 "SESSION_DESTORY" （1个文件中匹配到8次，总计查找1次） [普通: 大小写]
  D:\work\knowdee\projects\ivr\asr\log\knodi_asr_proxy_event.log （匹配8次）
#	行  58: {"project":"hoicee","module":"knodi_asr_proxy","timestamp":"2024-12-06T10:47:54.914","level":"info","host":"localhost.localdomain","hostIp":"127.0.0.1","event":{"appId":"servicePool_test_appId","sessionId":"5a9afca4-0e6a-4928-8aaf-19c03eae4029_50006"},"eventId":"fb25b82f-5b33-4887-b11e-dac144142d85","eventName":"SESSION_DESTORY"}
#	行  86: {"project":"hoicee","module":"knodi_asr_proxy","timestamp":"2024-12-06T10:48:19.023","level":"info","host":"localhost.localdomain","hostIp":"127.0.0.1","event":{"appId":"servicePool_test_appId","sessionId":"4a9112ca-243c-4edb-92de-ed76550b2c4a_50014"},"eventId":"daa86914-b903-4f11-a04c-53d1e95f4d65","eventName":"SESSION_DESTORY"}
#	行 133: {"project":"hoicee","module":"knodi_asr_proxy","timestamp":"2024-12-06T10:49:17.018","level":"info","host":"localhost.localdomain","hostIp":"127.0.0.1","event":{"appId":"servicePool_test_appId","sessionId":"6fb16b6a-0c96-48b3-b5b1-9accd1f25ad2_50010"},"eventId":"847aedb6-23c1-486d-ae78-6a8ad0705b42","eventName":"SESSION_DESTORY"}
#	行 134: {"project":"hoicee","module":"knodi_asr_proxy","timestamp":"2024-12-06T10:49:18.185","level":"info","host":"localhost.localdomain","hostIp":"127.0.0.1","event":{"appId":"servicePool_test_appId","sessionId":"cad62022-6090-4be1-ac86-94e88fa49942_50002"},"eventId":"94ffe0e0-c252-41fe-bdc3-92618e07c172","eventName":"SESSION_DESTORY"}
#	行 196: {"project":"hoicee","module":"knodi_asr_proxy","timestamp":"2024-12-06T10:51:05.061","level":"info","host":"localhost.localdomain","hostIp":"127.0.0.1","event":{"appId":"servicePool_test_appId","sessionId":"40a6e984-fa2d-4148-8e85-415b1dd418cb_50022"},"eventId":"82c9b2d2-d802-4fd0-8ee1-dd6700413be7","eventName":"SESSION_DESTORY"}
#	行 209: {"project":"hoicee","module":"knodi_asr_proxy","timestamp":"2024-12-06T10:51:28.420","level":"info","host":"localhost.localdomain","hostIp":"127.0.0.1","event":{"appId":"servicePool_test_appId","sessionId":"d5fc7750-184a-407c-8b0e-a7777e1da9f0_50018"},"eventId":"1e246715-4d04-47ec-9c39-c455d06292f9","eventName":"SESSION_DESTORY"}
#	行 252: {"project":"hoicee","module":"knodi_asr_proxy","timestamp":"2024-12-06T10:53:18.955","level":"info","host":"localhost.localdomain","hostIp":"127.0.0.1","event":{"appId":"servicePool_test_appId","sessionId":"f0459ab4-4f04-4982-b7db-f810fee12f0c_50030"},"eventId":"333c7952-5599-4ca8-a2ec-671969d2070c","eventName":"SESSION_DESTORY"}
#	行 312: {"project":"hoicee","module":"knodi_asr_proxy","timestamp":"2024-12-06T10:55:15.921","level":"info","host":"localhost.localdomain","hostIp":"127.0.0.1","event":{"appId":"servicePool_test_appId","sessionId":"f0d105d4-2998-48ef-90ee-f65c1cbcff52_50028"},"eventId":"9df21e2d-0711-4654-9137-e810a1bdf72a","eventName":"SESSION_DESTORY"}

搜索 "SESSION_CREATE" （1个文件中匹配到18次，总计查找1次） [普通: 大小写]
  D:\work\knowdee\projects\ivr\asr\log\knodi_asr_proxy_event.log （匹配18次）
	#行   1: {"project":"hoicee","module":"knodi_asr_proxy","timestamp":"2024-12-06T10:45:12.867","level":"info","host":"localhost.localdomain","hostIp":"127.0.0.1","event":{"appId":"servicePool_test_appId","asrOptions":{"engine":"Xunfei"},"callId":"cad62022-6090-4be1-ac86-94e88fa49942","channelId":"cad62022-6090-4be1-ac86-94e88fa49942","channelType":"user","port":50002,"sessionId":"cad62022-6090-4be1-ac86-94e88fa49942_50002"},"eventId":"cc8545d7-91cc-452f-96ed-a1b233c8cb08","eventName":"SESSION_CREATE"}
	行   2: {"project":"hoicee","module":"knodi_asr_proxy","timestamp":"2024-12-06T10:45:12.868","level":"info","host":"localhost.localdomain","hostIp":"127.0.0.1","event":{"appId":"servicePool_test_appId","asrOptions":{"engine":"Xunfei"},"callId":"cad62022-6090-4be1-ac86-94e88fa49942","channelId":"05bf807e-9628-4d32-86af-695380c98ead","channelType":"agent","port":50004,"sessionId":"cad62022-6090-4be1-ac86-94e88fa49942_50004"},"eventId":"45452581-8fee-4b87-b921-450095c196b4","eventName":"SESSION_CREATE"}
	#行  42: {"project":"hoicee","module":"knodi_asr_proxy","timestamp":"2024-12-06T10:47:15.598","level":"info","host":"localhost.localdomain","hostIp":"127.0.0.1","event":{"appId":"servicePool_test_appId","asrOptions":{"engine":"Xunfei"},"callId":"5a9afca4-0e6a-4928-8aaf-19c03eae4029","channelId":"5a9afca4-0e6a-4928-8aaf-19c03eae4029","channelType":"user","port":50006,"sessionId":"5a9afca4-0e6a-4928-8aaf-19c03eae4029_50006"},"eventId":"829e9a01-8e51-4c8c-bfa5-9bc82329b643","eventName":"SESSION_CREATE"}
	行  43: {"project":"hoicee","module":"knodi_asr_proxy","timestamp":"2024-12-06T10:47:15.599","level":"info","host":"localhost.localdomain","hostIp":"127.0.0.1","event":{"appId":"servicePool_test_appId","asrOptions":{"engine":"Xunfei"},"callId":"5a9afca4-0e6a-4928-8aaf-19c03eae4029","channelId":"6c1a4b41-2fa9-4166-b2bc-cfb9da2c6585","channelType":"agent","port":50008,"sessionId":"5a9afca4-0e6a-4928-8aaf-19c03eae4029_50008"},"eventId":"d2d46c14-f83c-46f4-be74-f16ed335aea4","eventName":"SESSION_CREATE"}
	#行  49: {"project":"hoicee","module":"knodi_asr_proxy","timestamp":"2024-12-06T10:47:37.276","level":"info","host":"localhost.localdomain","hostIp":"127.0.0.1","event":{"appId":"servicePool_test_appId","asrOptions":{"engine":"Xunfei"},"callId":"6fb16b6a-0c96-48b3-b5b1-9accd1f25ad2","channelId":"6fb16b6a-0c96-48b3-b5b1-9accd1f25ad2","channelType":"user","port":50010,"sessionId":"6fb16b6a-0c96-48b3-b5b1-9accd1f25ad2_50010"},"eventId":"2103778d-87c6-4c31-a124-96e88bf5ee21","eventName":"SESSION_CREATE"}
	行  50: {"project":"hoicee","module":"knodi_asr_proxy","timestamp":"2024-12-06T10:47:37.277","level":"info","host":"localhost.localdomain","hostIp":"127.0.0.1","event":{"appId":"servicePool_test_appId","asrOptions":{"engine":"Xunfei"},"callId":"6fb16b6a-0c96-48b3-b5b1-9accd1f25ad2","channelId":"30d9504f-f793-41ad-8fe4-031daef1fa5f","channelType":"agent","port":50012,"sessionId":"6fb16b6a-0c96-48b3-b5b1-9accd1f25ad2_50012"},"eventId":"48d1228c-fb29-4618-98d4-7b1700d52da2","eventName":"SESSION_CREATE"}
	#行  59: {"project":"hoicee","module":"knodi_asr_proxy","timestamp":"2024-12-06T10:47:54.914","level":"info","host":"localhost.localdomain","hostIp":"127.0.0.1","event":{"appId":"servicePool_test_appId","asrOptions":{"engine":"Xunfei"},"callId":"4a9112ca-243c-4edb-92de-ed76550b2c4a","channelId":"4a9112ca-243c-4edb-92de-ed76550b2c4a","channelType":"user","port":50014,"sessionId":"4a9112ca-243c-4edb-92de-ed76550b2c4a_50014"},"eventId":"f856990f-fde2-4f35-88e0-f4feb2f62ad2","eventName":"SESSION_CREATE"}
	行  60: {"project":"hoicee","module":"knodi_asr_proxy","timestamp":"2024-12-06T10:47:54.915","level":"info","host":"localhost.localdomain","hostIp":"127.0.0.1","event":{"appId":"servicePool_test_appId","asrOptions":{"engine":"Xunfei"},"callId":"4a9112ca-243c-4edb-92de-ed76550b2c4a","channelId":"149d5a81-9a0a-4d8e-859a-52f6c77f3a06","channelType":"agent","port":50016,"sessionId":"4a9112ca-243c-4edb-92de-ed76550b2c4a_50016"},"eventId":"a445aef6-c7af-440d-8ed6-ab776e2c7520","eventName":"SESSION_CREATE"}
	#行 135: {"project":"hoicee","module":"knodi_asr_proxy","timestamp":"2024-12-06T10:49:32.933","level":"info","host":"localhost.localdomain","hostIp":"127.0.0.1","event":{"appId":"servicePool_test_appId","asrOptions":{"engine":"Xunfei"},"callId":"d5fc7750-184a-407c-8b0e-a7777e1da9f0","channelId":"d5fc7750-184a-407c-8b0e-a7777e1da9f0","channelType":"user","port":50018,"sessionId":"d5fc7750-184a-407c-8b0e-a7777e1da9f0_50018"},"eventId":"0f8d64e4-4b74-44a5-ae6a-038bca817083","eventName":"SESSION_CREATE"}
	行 136: {"project":"hoicee","module":"knodi_asr_proxy","timestamp":"2024-12-06T10:49:32.934","level":"info","host":"localhost.localdomain","hostIp":"127.0.0.1","event":{"appId":"servicePool_test_appId","asrOptions":{"engine":"Xunfei"},"callId":"d5fc7750-184a-407c-8b0e-a7777e1da9f0","channelId":"84b05dda-48f1-46c7-9590-44edd728e062","channelType":"agent","port":50020,"sessionId":"d5fc7750-184a-407c-8b0e-a7777e1da9f0_50020"},"eventId":"a16eac3e-9926-4e07-9585-77d59cdb742a","eventName":"SESSION_CREATE"}
	#行 140: {"project":"hoicee","module":"knodi_asr_proxy","timestamp":"2024-12-06T10:49:49.571","level":"info","host":"localhost.localdomain","hostIp":"127.0.0.1","event":{"appId":"servicePool_test_appId","asrOptions":{"engine":"Xunfei"},"callId":"40a6e984-fa2d-4148-8e85-415b1dd418cb","channelId":"40a6e984-fa2d-4148-8e85-415b1dd418cb","channelType":"user","port":50022,"sessionId":"40a6e984-fa2d-4148-8e85-415b1dd418cb_50022"},"eventId":"c0a8cb55-4554-418c-bcc5-8e3a4a8acaea","eventName":"SESSION_CREATE"}

	行 141: {"project":"hoicee","module":"knodi_asr_proxy","timestamp":"2024-12-06T10:49:49.572","level":"info","host":"localhost.localdomain","hostIp":"127.0.0.1","event":{"appId":"servicePool_test_appId","asrOptions":{"engine":"Xunfei"},"callId":"40a6e984-fa2d-4148-8e85-415b1dd418cb","channelId":"e011e253-e335-49f7-bea5-55a7ff0dabf4","channelType":"agent","port":50024,"sessionId":"40a6e984-fa2d-4148-8e85-415b1dd418cb_50024"},"eventId":"ce95de3f-db5f-41cf-9fca-3239ad09bf48","eventName":"SESSION_CREATE"}
	行 177: {"project":"hoicee","module":"knodi_asr_proxy","timestamp":"2024-12-06T10:50:46.035","level":"info","host":"localhost.localdomain","hostIp":"127.0.0.1","event":{"appId":"servicePool_test_appId","asrOptions":{"engine":"Xunfei"},"callId":"f0d105d4-2998-48ef-90ee-f65c1cbcff52","channelId":"f0d105d4-2998-48ef-90ee-f65c1cbcff52","channelType":"user","port":50026,"sessionId":"f0d105d4-2998-48ef-90ee-f65c1cbcff52_50026"},"eventId":"1cf9ac98-dce9-4f3e-9026-e49adadb3837","eventName":"SESSION_CREATE"}
	#行 178: {"project":"hoicee","module":"knodi_asr_proxy","timestamp":"2024-12-06T10:50:46.036","level":"info","host":"localhost.localdomain","hostIp":"127.0.0.1","event":{"appId":"servicePool_test_appId","asrOptions":{"engine":"Xunfei"},"callId":"f0d105d4-2998-48ef-90ee-f65c1cbcff52","channelId":"83b70294-2e6b-49ee-90aa-c260dfe31452","channelType":"agent","port":50028,"sessionId":"f0d105d4-2998-48ef-90ee-f65c1cbcff52_50028"},"eventId":"9a691284-a0df-4cf3-b4cc-bc92a74e92bd","eventName":"SESSION_CREATE"}
	#行 212: {"project":"hoicee","module":"knodi_asr_proxy","timestamp":"2024-12-06T10:51:37.981","level":"info","host":"localhost.localdomain","hostIp":"127.0.0.1","event":{"appId":"servicePool_test_appId","asrOptions":{"engine":"Xunfei"},"callId":"f0459ab4-4f04-4982-b7db-f810fee12f0c","channelId":"f0459ab4-4f04-4982-b7db-f810fee12f0c","channelType":"user","port":50030,"sessionId":"f0459ab4-4f04-4982-b7db-f810fee12f0c_50030"},"eventId":"b2f32bbe-5bd3-48f5-93ee-bc9f313685bd","eventName":"SESSION_CREATE"}

	行 213: {"project":"hoicee","module":"knodi_asr_proxy","timestamp":"2024-12-06T10:51:37.982","level":"info","host":"localhost.localdomain","hostIp":"127.0.0.1","event":{"appId":"servicePool_test_appId","asrOptions":{"engine":"Xunfei"},"callId":"f0459ab4-4f04-4982-b7db-f810fee12f0c","channelId":"423066f4-6bb8-4723-a005-0be3d88fe0a1","channelType":"agent","port":50032,"sessionId":"f0459ab4-4f04-4982-b7db-f810fee12f0c_50032"},"eventId":"8890498c-e9c7-4ebb-93be-138d3e9292f4","eventName":"SESSION_CREATE"}
	行 266: {"project":"hoicee","module":"knodi_asr_proxy","timestamp":"2024-12-06T10:54:10.888","level":"info","host":"localhost.localdomain","hostIp":"127.0.0.1","event":{"appId":"servicePool_test_appId","asrOptions":{"engine":"Xunfei"},"callId":"24719f54-9218-4960-9b28-d4bd3d64ef48","channelId":"24719f54-9218-4960-9b28-d4bd3d64ef48","channelType":"user","port":50034,"sessionId":"24719f54-9218-4960-9b28-d4bd3d64ef48_50034"},"eventId":"73c0baa7-1315-4f25-808d-1785f4cc558c","eventName":"SESSION_CREATE"}
	行 267: {"project":"hoicee","module":"knodi_asr_proxy","timestamp":"2024-12-06T10:54:10.890","level":"info","host":"localhost.localdomain","hostIp":"127.0.0.1","event":{"appId":"servicePool_test_appId","asrOptions":{"engine":"Xunfei"},"callId":"24719f54-9218-4960-9b28-d4bd3d64ef48","channelId":"ef5263eb-9153-438c-99c0-aba26af5d164","channelType":"agent","port":50036,"sessionId":"24719f54-9218-4960-9b28-d4bd3d64ef48_50036"},"eventId":"25abba00-c112-42fb-bd93-6483606c8384","eventName":"SESSION_CREATE"}



20241213
构建打包kd-asr-proxy debug版本docker镜像(参考docker-compose测试环境210)
调测kd-asr-proxy docker镜像，解决容器运行时目录异常启动失败问题
研究uie模型python推理所用schema与预置信息融合算法
与孝政梳理沟通预置槽位信息、schema作用和平替、槽名接口、与开天一期槽名变化等问题



使用docker build 和 dockerfile构建镜像时，报错如下，因文件系统不兼容导致的文件权限不一致造成，通过本机拷贝到其他目录即可构建镜像
ERROR: failed to solve: archive/tar: unknown file mode ?rwxr-xr-x


20241212
添加kd-asr-proxy/mongoose网络库的调试跟踪日志
调测kd-asr-proxy/mongoose日志输出功能
开发kt-lib/ner预置意图与可变槽位映射信息Json解析功能
研究梳理uie模型python推理所用schema与预置信息融合算法


20241211
调试解决kd-asr-proxy解析配置参数时coredump问题
定位解决kd-asr-proxy创建VAD init失败问题
压测kd-asr-proxy并发http请求复现超时问题
开发kt-lib/ner中预置意图与槽位信息json文件加载功能


20241210
测试kd-asr-proxy debug版本功能
调测kt-lib/ner抽槽整体功能
设计意图与槽位映射信息预置表格转换结构
开发意图与槽位映射信息预置表格加载和转换Json功能


intent_name
slot_name
slot_value


root@docker-desktop:/work/litt/cpp_dev/ner# curl -sSL https://install.python-poetry.org | python3 -
Retrieving Poetry metadata

# Welcome to Poetry!

This will download and install the latest version of Poetry,
a dependency and package manager for Python.

It will add the `poetry` command to Poetry's bin directory, located at:

/root/.local/bin

You can uninstall at any time by executing this script with the --uninstall option,
and these changes will be reverted.

Installing Poetry (1.8.5): Done

Poetry (1.8.5) is installed now. Great!

To get started you need Poetry's bin directory (/root/.local/bin) in your `PATH`
environment variable.

Add `export PATH="/root/.local/bin:$PATH"` to your shell configuration file.

Alternatively, you can call Poetry explicitly with `/root/.local/bin/poetry`.

You can test that everything is set up by executing:

`poetry --version`


echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
或者如果你使用的是 Zsh，请将上面的 .bashrc 替换为 .zshrc


20241209
调研分析原生python uie模型推理后分数获取逻辑
开发调整kt-lib/ner抽槽uie模型后处理分数计算
排查线上kd-asr-proxy服务无法连接报超时问题(服务进程在跑，但无法收到建立网络连接，只有每个session user通道销毁，agent通道未销毁导致ws连接也超时断连)
编译kd-asr-proxy debug版本和搭建其gdb调试docker镜像



20241206
添加kt-lib/ner抽槽uie模型输出槽位分数
修改kt-lib/ner抽槽uie模型输出结果整合逻辑
修改kt-lib/ner抽槽pipeline调用逻辑
压测复现kd-asr-proxy服务http并发请求时超时问题





172.70.10.210 root msHsJgKuEu+dO45E8l
目录：/home/hoicee/cti

能帮推语音流过来压测下吗，看看是不是后面转发语音数据哪个环节出问题导致的，

想要复现超时问题，估计还得推语音流过来，


20241205
调研fast_tokenizer/sentencepiece支持处理bpe分词
添加kt-lib/ner抽槽match模型输出槽位分数
修改kt-lib/ner抽槽match模型输出结果整合逻辑
调测kt-lib/ner抽槽match模型整体功能

intent(5个模型)


20241204
排查解决tts-proxy依赖库libevent中未定义引用问题
调试梳理tts-proxy kdm所有的三方依赖
优化tts-proxy安装位置及头文件和动态库命名
分析算法组更新的ner抽槽逻辑变化(python)


bufferevent_openssl_set_allow_dirty_shutdown


20241203
架构会review kd-unimrcp和修改部分review问题
定位解决asr-proxy系统依赖uuid版本不兼容问题
kd-unimrcp以submodule方式引入三方依赖tts-proxy(kdm)
调测kd-unimrcp运行时tts-proxy的三方依赖


禅道：
补充历史工时
迭代需要开始

Design:
流程图中客户端改名为调用端，区分非mrcp中的客户端
流程图中消息流程的时序性，可以用序号来表示

API:
可突出如何调用 plugin 的 三套 API 的介绍
可以表达 Reco Plugin 和 Sync Plugin 的工作流程以及集成方法

KDS.JSON:
端口范围放到基础语音服务，找高宇

Scello:
需要和高宇一起做C++服务的支持


unimrcp build options:
--disable-option-checking  ignore unrecognized --enable/--with options
--disable-FEATURE       do not include FEATURE (same as --enable-FEATURE=no)
--disable-silent-rules  verbose build output (undo: "make V=0")
--disable-dependency-tracking
--disable-libtool-lock  avoid locking (might break parallel builds)
--disable-interlib-deps
					  disable inter-library dependencies (might break
--disable-client-lib    exclude unimrcpclient lib from build
--disable-client-app    exclude sample unimrcpclient app from build
--disable-umc           exclude sample unimrcpclient C++ app from build
--disable-asr-client    exclude misc ASR client lib and app from build
--disable-server-lib    exclude unimrcpserver lib from build
--disable-server-app    exclude unimrcpserver app from build
--disable-demosynth-plugin
--disable-demorecog-plugin
--disable-demoverifier-plugin
--disable-recorder-plugin


hoicee:
https://wiki.knowdee.com/bin/view/%E5%86%85%E9%83%A8%E5%B7%A5%E5%85%B7%E5%B9%B3%E5%8F%B0/hoicee/%E4%BA%A4%E6%8E%A5%E5%88%97%E8%A1%A8/


k8s
https://wiki.knowdee.com/bin/view/03-%E5%9B%A2%E9%98%9F/%E8%BF%90%E7%BB%B4%E5%9B%A2%E9%98%9F/%E8%BF%90%E7%BB%B4%E6%96%87%E6%A1%A3/%E6%B5%81%E7%A8%8B%E8%A7%84%E8%8C%83/docker%E6%96%B9%E5%BC%8F%E9%83%A8%E7%BD%B2%E5%86%85%E9%83%A8test%E7%8E%AF%E5%A2%83/


scello部署：k8s-->全量--->harbor 方式，下载deploy-script.tar包，上传内网服务器。

ASRPROXY_ASR_ENGINE=Xunfei
Xunfei
Lenovo

https://jumpserver.knowdee.com/
gaoyu/gaoyu!qweASD
AsrEngine
yhy-pre-2

scello.knowdee.com/:
admin/admin/123

scello地址:
https://devops.knowdee.com

现在这个scello支持打镜像，然后镜像去颐和园预发部署


chatbotbase/centos_c_compile:7.9.2009


wss://ws-api.xfyun.cn/v2/iat
opt->_iSampleRatio = 8000;


设计intent中意图label模块
提取模型和分词所用公共组件
分离具体功能组件和pipeline逻辑代码


creator_zone各个模块代码同步
编译更新各个模块dll
测试pipeline整体功能



客户的环境出现异常问题:
kd_asr_proxy(讯飞asr接口wss:443端口)有key timer expired超时情况


适配
优化


HTTP
WebSocket
MRCP

SIP/RTSP
SDP
RTP/RTCP

tcp/udp
ip

freeswitch:

unimrcp:

mrcp_generic_header_t *generic_header = mrcp_generic_header_get(request);
if(generic_header && generic_header->vendor_specific_params){
	// recog_channel->vendor_params = apt_pair_array_copy(generic_header->vendor_specific_params, request->pool);
	asrRender = vendor_param_find(generic_header->vendor_specific_params, "engine");
	sessionId = vendor_param_find(generic_header->vendor_specific_params, "sessionId");
	vadEnergyStart = vendor_param_find(generic_header->vendor_specific_params, "Speech-vad-energy-start");
	vadPause = vendor_param_find(generic_header->vendor_specific_params, "Speech-vad-pause");
}



20241202
编写kd-unimrcp文档dockerfile
编写kd-unimrcp文档docker-compose
编写kd-unimrcp文档README.md
编写kd-unimrcp文档design.md




作图：creator_zone/creator_zone_multi
搜图：image_embedding
抠图


creator_zone发版地址:
http://172.70.10.53:6740/tree/1128_cz_fb
root



20241129
测试creator_zone_multi/PoPipelineTest arm64版本整体功能
整理creator_zone_multi环境，并打包提供元月arm64版本安装包
kd-unimrcp以submodule方式引入三方依赖asr-proxy(kdm)
排查解决kd-unimrcp服务启动时asr-proxy依赖缺失问题

UniMRCP version............... : 1.7.0

APR version................... : 1.5.2
APR-util version.............. : 1.5.4
Sofia-SIP version............. : 1.12.11-239-g54ef3e2

Compiler...................... : gcc
Compiler flags................ : -g -O2 -pthread
Preprocessor definitions...... : -DLINUX -D_REENTRANT -D_GNU_SOURCE
Linker flags.................. :

UniMRCP client lib............ : yes
Sample UniMRCP client app..... : yes
Sample UMC C++ client app..... : yes
Misc ASR client lib and app... : yes

UniMRCP server lib............ : yes
UniMRCP server app............ : yes

Demo synthesizer plugin....... : yes
Demo recognizer plugin........ : yes
Demo verifier plugin.......... : yes
Recorder plugin............... : yes

Installation layout........... : classic
Installation directory........ : /work/knowdee/projects/kds/kd-unimrcp/kd-unimrcp


定位解决DimExtract时运行抛出异常
缺少classify voc词表文件



20241128
源码编译sentencepiece依赖arm64版本
适配creator_zone_multi/DimExtract支持arm64平台
适配creator_zone_multi/Classification支持arm64平台
适配creator_zone_multi/PoPipeline支持arm64平台


20241127
适配creator_zone_multi/DimSearch支持arm64平台
适配creator_zone_multi/DimSearchTest支持arm64平台
适配creator_zone_multi/DimRec支持arm64平台
适配creator_zone_multi/DimRecTest支持arm64平台



20241126
搭建kds标准工程kd-unimrcp
迁移unimrcp工程代码至kd-unimrcp
编译调试kd-unimrcp工程代码
编写kd-unimrcp文档kds.json


20241125
梳理unimrcp-dep依赖集成方式
清理unimrcp工程编译中间文件
编译调试unimrcp工程
优化编译脚本和unimrcp-dep非侵入式集成



2024-11-26 19:33:02:186151 [INFO]   Load Plugin [Demo-Synth-1] [/work/knowdee/projects/kds/kd-unimrcp/kd-unimrcp/plugin/demosynth.so]
2024-11-26 19:33:02:213123 [WARN]   Failed to Load DSO: libaws-cpp-sdk-s3.so: cannot open shared object file: No such file or directory
2024-11-26 19:33:02:213154 [INFO]   Load Plugin [Demo-Recog-1] [/work/knowdee/projects/kds/kd-unimrcp/kd-unimrcp/plugin/demorecog.so]
2024-11-26 19:33:02:348832 [WARN]   Failed to Load DSO: libMicrosoft.CognitiveServices.Speech.core.so: cannot open shared object file: No such file or directory
2024-11-26 19:33:02:348872 [INFO]   Load Plugin [Demo-Verifier-1] [/work/knowdee/projects/kds/kd-unimrcp/kd-unimrcp/plugin/demoverifier.so]



git submodule add <repository> [<path>]
git submodule add https://github.com/user/external-library.git libs/external-library

git add .gitmodules libs/external-library
git commit -m "Add external-library as a submodule"

git clone --recursive <repository>




ubuntu20.04:
1 /work/knowdee/projects/ivr/mrcp/unimrcp-deps-1.6.0/build-dep-libs.sh
2 make_deployment.sh

>>>>>> Step 8: Copying contents of out/plugin to deployment/plugin... >>>>>>
>>>>>> Step 9: Copying asr and tts lib to deployment/lib... >>>>>>
cp: cannot stat '../recoproxy/api/librecoProxy.so': No such file or directory
cp: cannot stat '../ttsProxy/api/libttsProxy.so': No such file or directory
>>>>>> Step 10: Congratulations it is completed... >>>>>>


Making install in unimrcp-server
make[2]: Entering directory '/work/knowdee/projects/ivr/mrcp/unimrcp/platforms/unimrcp-server'
make[3]: Entering directory '/work/knowdee/projects/ivr/mrcp/unimrcp/platforms/unimrcp-server'
 /usr/bin/mkdir -p '/work/knowdee/projects/ivr/mrcp/unimrcp/out/bin'
  /bin/bash ../../libtool   --mode=install /usr/bin/install -c unimrcpserver '/work/knowdee/projects/ivr/mrcp/unimrcp/out/bin'
libtool: install: /usr/bin/install -c .libs/unimrcpserver /work/knowdee/projects/ivr/mrcp/unimrcp/out/bin/unimrcpserver

libtool: install: /usr/bin/install -c .libs/libunimrcpserver.a /work/knowdee/projects/ivr/mrcp/unimrcp/out/lib/libunimrcpserver.a
libtool: install: chmod 644 /work/knowdee/projects/ivr/mrcp/unimrcp/out/lib/libunimrcpserver.a
libtool: install: ranlib /work/knowdee/projects/ivr/mrcp/unimrcp/out/lib/libunimrcpserver.a
libtool: finish: PATH="/root/vcpkg:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/sbin" ldconfig -n /work/knowdee/projects/ivr/mrcp/unimrcp/out/lib

libtool: install: /usr/bin/install -c .libs/libasrclient.a /work/knowdee/projects/ivr/mrcp/unimrcp/out/lib/libasrclient.a
libtool: install: chmod 644 /work/knowdee/projects/ivr/mrcp/unimrcp/out/lib/libasrclient.a
libtool: install: ranlib /work/knowdee/projects/ivr/mrcp/unimrcp/out/lib/libasrclient.a
libtool: finish: PATH="/root/vcpkg:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/sbin" ldconfig -n /work/knowdee/projects/ivr/mrcp/unimrcp/out/lib

libtool: install: chmod 644 /work/knowdee/projects/ivr/mrcp/unimrcp/out/lib/libunimrcpclient.a
libtool: install: ranlib /work/knowdee/projects/ivr/mrcp/unimrcp/out/lib/libunimrcpclient.a
libtool: finish: PATH="/root/vcpkg:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/sbin" ldconfig -n /work/knowdee/projects/ivr/mrcp/unimrcp/out/lib

libtool: install: /usr/bin/install -c .libs/mrcprecorder.a /work/knowdee/projects/ivr/mrcp/unimrcp/out/plugin/mrcprecorder.a
libtool: install: chmod 644 /work/knowdee/projects/ivr/mrcp/unimrcp/out/plugin/mrcprecorder.a
libtool: install: ranlib /work/knowdee/projects/ivr/mrcp/unimrcp/out/plugin/mrcprecorder.a
libtool: finish: PATH="/root/vcpkg:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/sbin" ldconfig -n /work/knowdee/projects/ivr/mrcp/unimrcp/out/plugin

libtool: install: chmod 644 /work/knowdee/projects/ivr/mrcp/unimrcp/out/plugin/demoverifier.a
libtool: install: ranlib /work/knowdee/projects/ivr/mrcp/unimrcp/out/plugin/demoverifier.a
libtool: finish: PATH="/root/vcpkg:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/sbin" ldconfig -n /work/knowdee/projects/ivr/mrcp/unimrcp/out/plugin

libtool: install: chmod 644 /work/knowdee/projects/ivr/mrcp/unimrcp/out/plugin/demorecog.a
libtool: install: ranlib /work/knowdee/projects/ivr/mrcp/unimrcp/out/plugin/demorecog.a
libtool: finish: PATH="/root/vcpkg:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/sbin" ldconfig -n /work/knowdee/projects/ivr/mrcp/unimrcp/out/plugin

libtool: install: chmod 644 /work/knowdee/projects/ivr/mrcp/unimrcp/out/plugin/demosynth.a
libtool: install: ranlib /work/knowdee/projects/ivr/mrcp/unimrcp/out/plugin/demosynth.a
libtool: finish: PATH="/root/vcpkg:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/sbin" ldconfig -n /work/knowdee/projects/ivr/mrcp/unimrcp/out/plugin
----------------------------------------------------------------------
Libraries have been installed in:
   /work/knowdee/projects/ivr/mrcp/unimrcp/out/plugin

If you ever happen to want to link against installed libraries
in a given directory, LIBDIR, you must either use libtool, and
specify the full pathname of the library, or use the '-LLIBDIR'
flag during linking and do at least one of the following:
   - add LIBDIR to the 'LD_LIBRARY_PATH' environment variable
     during execution
   - add LIBDIR to the 'LD_RUN_PATH' environment variable
     during linking
   - use the '-Wl,-rpath -Wl,LIBDIR' linker flag
   - have your system administrator add LIBDIR to '/etc/ld.so.conf'

See any operating system documentation about shared libraries for
more information, such as the ld(1) and ld.so(8) manual pages.
----------------------------------------------------------------------


20241122
研究现有unimrcp工程结构
对比原unimrcp，分析现有unimrcp增改变化
搭建unimrcp开发环境
源码编译unimrcp-dep依赖包



asr-proxy review:
kdm.json:
OS 使用：逐渐抛弃 CentOS，采用 Ubuntu 和 rocky linux

Desingn:
架构写的太泛，需要架构的逻辑
核心流程没有做表达，需要把调用到vad以及如何调用到 ASR 服务的流程体现

API：
接口需要逐渐优化，改为新定义的接口(vad参数优化)


搭建asr_proxy Ubuntu20.04开发环境
asr_proxy编译适配Ubuntu20.04平台
调测asr_proxy测试用例




-- Build files have been written to: /work/knowdee/projects/kdm/asr-proxy/build
[ 50%] Linking CXX executable test_kdm_asr_proxy

/usr/bin/ld: /work/knowdee/projects/kdm/asr-proxy/install/lib/libkdm_asr_proxy.so: undefined reference to `curl_formadd'
/usr/bin/ld: /work/knowdee/projects/kdm/asr-proxy/install/lib/libkdm_asr_proxy.so: undefined reference to `curl_slist_append'
/usr/bin/ld: /work/knowdee/projects/kdm/asr-proxy/install/lib/libkdm_asr_proxy.so: undefined reference to `curl_easy_perform'
/usr/bin/ld: /work/knowdee/projects/kdm/asr-proxy/install/lib/libkdm_asr_proxy.so: undefined reference to `curl_easy_init'
/usr/bin/ld: /work/knowdee/projects/kdm/asr-proxy/install/lib/libkdm_asr_proxy.so: undefined reference to `curl_formfree'
/usr/bin/ld: /work/knowdee/projects/kdm/asr-proxy/install/lib/libkdm_asr_proxy.so: undefined reference to `curl_global_init'
/usr/bin/ld: /work/knowdee/projects/kdm/asr-proxy/install/lib/libkdm_asr_proxy.so: undefined reference to `curl_easy_cleanup'
/usr/bin/ld: /work/knowdee/projects/kdm/asr-proxy/install/lib/libkdm_asr_proxy.so: undefined reference to `curl_global_cleanup'
/usr/bin/ld: /work/knowdee/projects/kdm/asr-proxy/install/lib/libkdm_asr_proxy.so: undefined reference to `curl_easy_setopt'
/usr/bin/ld: /work/knowdee/projects/kdm/asr-proxy/install/lib/libkdm_asr_proxy.so: undefined reference to `curl_easy_getinfo'
/usr/bin/ld: /work/knowdee/projects/kdm/asr-proxy/install/lib/libkdm_asr_proxy.so: undefined reference to `curl_slist_free_all'
/usr/bin/ld: /work/knowdee/projects/kdm/asr-proxy/install/lib/libcjsonLog.so: undefined reference to `uuid_generate'
/usr/bin/ld: /work/knowdee/projects/kdm/asr-proxy/install/lib/libkdm_asr_proxy.so: undefined reference to `curl_easy_strerror'


collect2: error: ld returned 1 exit status
make[2]: *** [example/CMakeFiles/test_kdm_asr_proxy.dir/build.make:97: example/test_kdm_asr_proxy] Error 1
make[1]: *** [CMakeFiles/Makefile2:98: example/CMakeFiles/test_kdm_asr_proxy.dir/all] Error 2
make: *** [Makefile:136: all] Error 2


20241121
架构会review kdm asr_proxy
修改调测asr_proxy运行时依赖安装
修改asr_proxy review部分文档问题
排查客户环境kd_asr_proxy鉴权超时问题


-L./SDK -lrecoProxy  -Wl,-rpath=./SDK

gcc (GCC) 4.8.5


scl enable devtoolset-9 bash


#!/bin/bash

set -e

cp /etc/yum.repos.d/CentOS-SCLo-scl.repo /etc/yum.repos.d/CentOS-SCLo-scl.repo.backup
cp /etc/yum.repos.d/CentOS-SCLo-scl-rh.repo /etc/yum.repos.d/CentOS-SCLo-scl-rh.repo.backup
cat <<EOF > /etc/yum.repos.d/CentOS-SCLo-rh.repo
  [centos-sclo-rh]
  name=CentOS-7 - SCLo rh
  baseurl=https://mirrors.aliyun.com/centos/7/sclo/x86_64/rh/
  gpgcheck=1
  enabled=1
  gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-SCLo
EOF

cp /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo

yum clean all && yum makecache && yum update -y
yum install -y wget gcc gcc-c++ librdkafka-devel openssl openssl-devel centos-release-scl devtoolset-9-gcc*

scl enable devtoolset-9 bash




20241120
规整asr_proxy运行时依赖
梳理asr_proxy外层API入参出参
编写asr_proxy接口文档apis.md
编写asr_proxy设计文档design.md


20241119
梳理调试asr_proxy三方依赖
定位测试用例启动时报错undefined symbol问题
编写asr_proxy标准文件kdm.json
编写asr_proxy标准文件README.md


/usr/bin/ld: warning: libssl.so.10, needed by /work/knowdee/projects/ivr/asr/recoproxy/src/../third_party/aws-sdk-cpp/lib/libaws-cpp-sdk-core.so, not found (try using -rpath or -rpath-link)
/usr/bin/ld: warning: libcrypto.so.10, needed by /work/knowdee/projects/ivr/asr/recoproxy/src/../third_party/aws-sdk-cpp/lib/libaws-cpp-sdk-core.so, not found (try using -rpath or -rpath-link)

/usr/bin/ld: ../src/libRECO_PROXY.so: undefined reference to `iflytekAsrRequestParam::BUSINESSARGS_PART2'

/usr/bin/ld: /work/knowdee/projects/ivr/asr/recoproxy/src/../third_party/cjson/lib/libcjsonLog.so: undefined reference to `uuid_generate'
此依赖库需要uuid，但其没有依赖链接libuuid.so，故依赖libcjsonLog.so时，需要在编译时加"-luuid"


000000000011a090 W _ZN22iflytekAsrRequestParam13 getFirstFrame B5cxx11EiPvi
00000000001180d0 W _ZN22iflytekAsrRequestParam14 getCommonFrame B5cxx11EiPvi
                 U _ZN22iflytekAsrRequestParam9 createUrl B5cxx11Ev
                 U _ZN22iflytekAsrRequestParam13 getCommonArgs B5cxx11Ev
				 U _ZN22iflytekAsrRequestParam18 BUSINESSARGS_PART1 E
                 U _ZN22iflytekAsrRequestParam18 BUSINESSARGS_PART2 E
0000000000116a90 W _ZN22iflytekAsrRequestParam D1Ev
0000000000116a90 W _ZN22iflytekAsrRequestParam D2Ev




0000000000890964 W _ZN22iflytekAsrRequestParam8getFrameEiPvi
0000000000890922 W _ZN22iflytekAsrRequestParam11setLanguageEPc
0000000000890afa W _ZN22iflytekAsrRequestParam13base64_encodeEPhj
0000000000890d52 W _ZN22iflytekAsrRequestParam13getFirstFrameEiPvi
0000000000891160 W _ZN22iflytekAsrRequestParam14getCommonFrameEiPvi
000000000089094c W _ZN22iflytekAsrRequestParam14setSampleRatioEi
                 U _ZN22iflytekAsrRequestParam9createUrlEv
				 U _ZN22iflytekAsrRequestParam13getCommonArgsEv
                 U _ZN22iflytekAsrRequestParam18BUSINESSARGS_PART1E
                 U _ZN22iflytekAsrRequestParam18BUSINESSARGS_PART2E
0000000000890898 W _ZN22iflytekAsrRequestParamC1Ev
0000000000890898 W _ZN22iflytekAsrRequestParamC2Ev
00000000008908da W _ZN22iflytekAsrRequestParamD1Ev
00000000008908da W _ZN22iflytekAsrRequestParamD2Ev


20241118
排查解决recoproxy代码编译wss时报错问题
调测recoproxy测试用例
构建kdm工程asr_proxy
迁移recoproxy代码至asr_proxy


requirements:
3rd-party:
boost 1.74.0
aws-cpp-sdk 1.8.0
websocketpp 0.8.2


std::put_time(c++14)

cjsonLog.so(uuid)
AWS SDK
ubuntu:
apt install libcurl4-openssl-dev libssl-dev uuid-dev

centos:7.9.2009(gcc9.3):
yum install libcurl-devel openssl-devel libuuid cmake

pCreateRecoProxy
pFeedDataToRecoProxy
pCloseRecoProxy

RECOPROXY_PROCESS_PARTIAL

const static int VAD_BUFF_LEN = 2*64*1000;

20241115
整理arm版本creator_zone代码工程
整理并打包arm版本PoPipelineTest(已提交洪辉)
梳理现有recoproxy代码结构
编译调试recoproxy代码，解决libcurl依赖缺失问题



沟通交接creator_zone数据库相关文档
梳理creator_zone工程代码
各个模型筛选指标和阈值改为动态可配config



## 深度神经网络DNN模型推理框架:
vllm
onnxruntime
TensorRT
OpenMP


## GPU compute graph(算子，计算图，矩阵运算，数学库):
cudnn
cuda


## GPU硬件驱动:
nvidia-smi


## GPU硬件
4090
T4
A100 40G/80G(DGX A100 八张卡)
H100



20241114
arm平台编译调试Classification
arm平台编译调试PoPipeline
测试arm平台PoPipelineTest整体功能
排查解决PoPipelineTest启动时依赖加载异常问题


20241113
arm平台源码编译sqlcipher
arm平台源码编译openssl
arm平台编译调试DimExtract
arm平台编译调试DimRec


# laa/creator_zone
## dependence:
PoPipeline.dll
Classification.dll
DimExtract.dll
DimRec.dll
DimSearch.dll

core_tokenizers.dll
icudt70.dll
icuuc70.dll

onnxruntime.dll
onnxruntime_providers_shared.dll

sqlcipher.dll(x64)/sqlite3.dll(arm64)
libcrypto-3-x64.dll(x64)


# sqlcipher build(dll: nmake.exe -f ..\Makefile.msc TOP=..\ (in "Developer PowerShell for VS 2022"))

@build sqlcipher
@ 1. clone sqlcipher somewhere (in a sqlcipher directory).
@ 2. install a proper tclsh.exe and put it in the path https://www.activestate.com/products/tcl/
@ 3. install open SSL binaries & static libs https://slproweb.com/products/Win32OpenSSL.html
@ 4. create a "build" directory at same level
@ 5. create a "x64" directory under "build"
@ 6. copy this file in build\x64
@ 7. open "x64 Native Tools Command Prompt for VS 20XX"
@ 8. cd build\x64
@ 9. run buildx64.bat (this file copied in build\x64)
@ 10. after run (somewarning can be ignored and last error about "shell" too) you will get an sqlite.x64.dll (~7 Mb in size)
@ also adapt paths
@ nmake /f ..\Makefile.msc TOP=..\ FOR_WIN10=1 SQLITE3DLL=sqlite3.x64.dll PLATFORM=x64
mkdir build
cd build
@nmake /f ..\Makefile.msc TOP=..\ FOR_WIN10=1  PLATFORM=arm64
nmake /f ..\Makefile.msc TOP=..\

## Makefile.msc modify

# Flags to include OpenSSL
# TCC = $(TCC) -DSQLITE_HAS_CODEC -I"C:\Users\lit\vcpkg\packages\openssl_arm64-windows-static\include"
# RCC = $(RCC) -DSQLITE_HAS_CODEC -I"C:\Users\lit\vcpkg\packages\openssl_arm64-windows-static\include"
TCC = $(TCC) -DSQLITE_HAS_CODEC -I"C:\Users\lit\vcpkg\packages\openssl_x64-windows-static\include"
RCC = $(RCC) -DSQLITE_HAS_CODEC -I"C:\Users\lit\vcpkg\packages\openssl_x64-windows-static\include"

# linker options for OpenSSL
# LTLIBPATHS = $(LTLIBPATHS) /LIBPATH:$(ICULIBDIR) /LIBPATH:"C:\Users\lit\vcpkg\packages\openssl_arm64-windows-static\lib"
LTLIBPATHS = $(LTLIBPATHS) /LIBPATH:$(ICULIBDIR) /LIBPATH:"C:\Users\lit\vcpkg\packages\openssl_x64-windows-static\lib"
LTLIBS = $(LTLIBS) libssl.lib libcrypto.lib ws2_32.lib shell32.lib advapi32.lib gdi32.lib user32.lib crypt32.lib kernel32.lib


## requirements:
openssl(lib:vcpkg install openssl:arm64-windows-static)
tcl(exe:Git\mingw64\bin)

vs2022(c++、.net)
vcpkg
git
cmake


sqlcipher
openssl				C:\Users\lit\vcpkg\packages\openssl_arm64-windows-static\include
tcl



20241112
搭建arm平台源码编译环境
编译安装依赖库easylogger
调试排查fast_tokenizer依赖加载异常报错
编译调试creator_zone/dimSearch(sqlcipher版本不兼容)


20241111
调研安装sqlcipher arm版本
源码交叉编译sqlcipher arm版本(内置编译脚本不支持)
源码交叉编译openssl arm版本
源码交叉编译tcl arm版本



20241108
熟悉creator_zone整体代码结构与组成
同洪辉探讨梳理creator_zone业务流程与逻辑
调研Windows Arm架构交叉编译可行性
安装VS2022 Arm交叉编译所需工具集



CZ工程开发内容优化
任务描述
1、初始化load占用18m，执行业务后，unload，剩余75m，没卸载干净
2、config 动态指标设计
  a.分类模型中的labellist(全量)
  b.检索模型中的粗筛数量(200,config)，topk_gxaric,topk_statiç(通过接口自定义)以及分....
  c.推荐模型必选项(0.6，越高越好，confg)，可选项(0.8，越高越好，config)
3、数据库分库(.db 明文)(.db vec)
4、抽取和推荐业务逻辑互斥逻辑优化(优先级低)

以下是cz工程化当前需要推进的内容：
1. 业务逻辑，工程代码熟悉，交接
2. 数据库部分代码的改写，支持同时使用加密的prompt片段数据库和未加密的vec数据库
3. 支持ARM架构




Kd-asr-proxy
设计：
架构中体现一下可能依赖的rewrite服务
后续可演化为多SAAS服务的实时调度设置（思考抛开电话业务，此服务的演进）

API：
Create session 接口：
APPID：后续KDS升级时改为，AKSK的完整验证
流式传输接口如何定义



20241107
架构会review服务kd-asr-proxy
细化补充kd-asr-proxy文档README.md、kds.json
优化kd-asr-proxy工程服务名及代码命名规范
优化kd-asr-proxy设计文档design.md


kt-lib/intent
laa/creator_zone



20241106
组内review工程kd_asr_proxy
细化kd_asr_proxy接口rest api参数说明
调整补充kd_asr_proxy文档design.md
修改kd_asr_proxy文档README.md


20241105
排查解决kd_asr_proxy提交软连接文件异常问题
绘制kd_asr_proxy架构设计图design.md
编写kd_asr_proxy工程README.md
测试使用nexus基础镜像部署kd_asr_proxy


测试使用新版scello部署kd_asr_proxy


20241104
迁移hoicee_asr_proxy代码到kds工程kd_asr_proxy
编译调试kds工程代码kd_asr_proxy
梳理修改third_party依赖，解决运行时重定位依赖库问题
梳理hoicee_asr_proxy服务架构设计


20241101
梳理hoicee_asr_proxy接口代码
编写hoicee_asr_proxy接口apis文档
修改kds标准文件kds.json
补充scello所用脚本


20241031
测试sqlcipher工具加密db文件功能
沟通探讨sqlcipher工具集成方式及问题
编写sqlcipher加解密db文件的代码样例
调测代码用例加解密db文件功能


研究sqlite_vec使用方法
设计sqlite向量数据插入接口
设计sqlite删除向量数据接口
设计sqlite修改向量数据接口
设计sqlite清库接口



20241030
调试creator_zone/DimSearch开发环境
研究现有creator_zone/DimSearch代码
调研sqlcipher加密工具
编译安装sqlcipher工具windows版本


#define SQLITE_VERSION        "3.45.3"
#define SQLITE_VERSION_NUMBER 3045003
#define SQLITE_SOURCE_ID      "2024-04-15 13:34:05 8653b758870e6ef0c98d46b3ace27849054af85da891eb121e9aaa537f1ealt1"


#define SQLITE_VERSION        "3.46.1"
#define SQLITE_VERSION_NUMBER 3046001
#define SQLITE_SOURCE_ID      "2024-08-13 09:16:08 c9c2ab54ba1f5f46360f1b4f35d849cd3f080e6fc2b6c60e91b16c63f69a1e33"



vcpkg install sqlcipher:x64-windows

# this is heuristically generated, and may not be correct
find_package(sqlcipher CONFIG REQUIRED)
target_link_libraries(main PRIVATE sqlcipher::sqlcipher)

sqlcipher provides pkg-config modules:

# SQL database engine
sqlcipher


vcpkg install sqlitecpp[sqlcipher]:x64-windows

  # this is heuristically generated, and may not be correct
  find_package(SQLiteCpp CONFIG REQUIRED)
  target_link_libraries(main PRIVATE SQLiteCpp)


20241029
优化原有规则抽槽CNerMatchModule
修改intent抽槽新版API接口
调测intent抽槽新版API接口功能
安装vs2022准备creator_zone开发环境

与洪辉沟通creator_zone向量库增删改等操作功能接口



20241028
排查测试kt-lib/intent资源加载失败问题
测试旧版intent接口功能
优化原有规则抽槽TrieSbcConvert及Util
优化原有规则抽槽解密CAesGcmModule


20241025
优化match模型推理框架
调整kt-lib/intent调用抽槽模块
修改kt-lib/intent测试程序
调试定位kt-lib编译问题


20241024
优化uie模块tokenizer
优化match模块tokenizer
优化uie模型推理框架
定位uie模型推理无结果问题

uie model structure:
input_ids
name: input_ids
tensor: int64[batch,sequence]
token_type_ids
name: token_type_ids
tensor: int64[batch,sequence]
attention_mask
name: attention_mask
tensor: int64[batch,sequence]


start_prob
name: start_prob
tensor: float32[batch,sequence]
end_prob
name: end_prob
tensor: float32[batch,sequence]


match model structure:
input_ids
name: input_ids
tensor: int64[batch_size,sequence_size]
attention_mask
name: attention_mask
tensor: int64[batch_size,sequence_size]

output
name: output
tensor: float32[batch_size,2]


20241023
调测整合后ner模块内规则抽槽功能
排查规则抽槽初始化失败，解决解密配置文件失败问题
集成ner抽槽模块到kt-lib/intent
调测kt-lib/intent调用抽槽功能，定位解决规则抽槽无结果问题


20241022
排查解决uie模型预测无结果问题
排查解决match模型tokenize结果异常
定位match模型预测抛异常问题
整合规则匹配槽位到ner抽槽模块内


ner No.1 slots: 腾 讯 会 议
ner rule re sentence = 打开微信, intent = 打开应用
label:我的文档, pattern:.*(我的文档|my document).*
label:我的图片, pattern:.*(我的图片|my picture).*
label:我的音乐, pattern:.*(我的音乐|my music).*
label:我的视频, pattern:.*(我的视频|my video).*
label:我的下载, pattern:.*(我的下载|my download).*
label:截图, pattern:.*(截图|shootcut|shoot cut|截屏|抓图|截取).*
label:系统信息, pattern:.*(系统配置|硬件信息|处理器型号|主板型号|内存容量|硬盘型号|显卡型号|操作系统|内核版本|注册信息|驱动程序|版本|厂商|安装时间|软件版本|版本信息|系统日志).*
label:TEXTTYPE, pattern:{.*, TEXTTYPE | NUMTYPE}

ner rule re output slots = ["TEXTTYPE","微信"]


110号

4号楼1单元3204

腾 讯 会 议
微信

20241021
调试uie模型预测接口
调试uie模型后处理接口
编写抽槽测试用例
调测整体流程和功能


20241018
开发调试match模型后处理接口
调试match模型预处理接口
调试match模型预测接口
调试uie模型预处理接口


20241017
开发抽槽uie模型后处理接口
开发抽槽match模型调用流程
开发抽槽match模型预处理接口
开发抽槽match模型预测接口


20241016
开发抽槽uie模型调用流程
开发抽槽uie模型预处理接口
开发抽槽uie模型预测接口
测试hoicee_asr_proxy讯飞接口功能，定位解决配置无效问题，相对原来联想接口识别效果不太好


20241015
构建抽槽模块工程框架
设计抽槽模块调用流程
设计抽槽模块功能接口
开发抽槽模块功能接口


20241014
熟悉抽槽模型windows工程框架及环境
研究抽槽模型调用流程
梳理抽槽模型功能接口
设计抽槽模块linux工程框架



kt-lib/intent:
hnsw-algo:一种用于近似最近邻搜索（Approximate Nearest Neighbor, ANN）的数据结构，旨在解决大规模高维数据集中的高效近似最近邻搜索问题。

finalres["intent"] = rule_label;
finalres["slots"]
finalres["aux_case"] = aux_case_rec;
finalres["score"] = rec_score;

kt-lib/intent/docs/apis.md:
| `data`           | object | 包含识别结果的对象                                  |
| `aux_case`       | string | 识别出的辅助信息，解释文本中的相关行为              |
| `intent_code`    | string | 识别出的意图标识                                    |
| `intent_content` | string | 识别出的意图内容描述                                |
| `score`          | float  | 识别结果的置信度分数，范围为 0~1                    |
| `slots`          | array  | 识别出的槽位信息，包含槽位标识、内容及槽位类型       |
| `slot_code`      | string | 槽位标识，如地点、时间、应用等                      |
| `slot_content`   | string | 槽位内容                                            |
| `slot_type`      | string | 槽位类型，可能值为 `TEXTTYPE` 或 `NUMTYPE`          |


// 1 模型和配置信息解码(加载规则)
CAesGcmModule* caceGcmModel;

// 2 意图识别 IR(intent recognition)

	// 2.1 规则匹配意图(rule match intent)
	CRuleMatchIntent* ruleMatchIntent;

	// 2.2 模型匹配意图(model match intent)
		// 2.2.1 文本向量化
		CEmbeddingModule* cmodel;
		// 2.2.2 向量化后检索——topN
		CHnwsModule* chnwModel;
		// 2.2.3 结果排序——精排top1
		CSortModel* smodel;

// 3 槽位抽取 NER(named entity recognition)
CNerMatchModule* nerMatchModel;

	// 3.1 规则匹配槽位(rule match ner)
	CRuleMatchNer* ruleMatchNer;

	// 3.2 模型匹配槽位(model match ner)
		// 2.2.1 文本向量化
		CEmbeddingModule* cmodel;
		// 2.2.2 向量化后检索——topN
		CHnwsModule* chnwModel;
		// 2.2.3 结果排序——精排top1
		CSortModel* smodel;


RE-intent:规则匹配意图(CRuleMatchIntent)
NER:命名实体识别(CNerMatchModule)
input:	{std::string:sentence, std::string:intent}
output:	{std::vector<slot>: slots}


UIE:通用信息提取{vocab_file[fast_tokenizer], onnx_model[onnxruntime]}
input:text(看电影), type
output:start, end


kd_uie_mod.0.0.2.onnx
input_ids
name: input_ids
tensor: int64[batch,sequence]
token_type_ids
name: token_type_ids
tensor: int64[batch,sequence]
attention_mask
name: attention_mask
tensor: int64[batch,sequence]

start_prob
name: start_prob
tensor: float32[batch,sequence]
end_prob
name: end_prob
tensor: float32[batch,sequence]



20241012
研究学习creator_zone项目功能接口
编写hoicee_asr_proxy工程kds标准文件
修改补充hoicee_asr_proxy工程脚本
研究scello平台nexus仓库中的C/C++开发和部署基础镜像环境


20241011
定位解决非jpeg格式图片缩放失败问题
测试统计图片向量化和文本分词向量化耗时
修改补充kdm_image文档review相关问题
研究熟悉creator_zone项目工程架构


text：0.0446931 秒	51个汉字
text：0.0363529 秒	17个汉字
text：0.0362122 秒	3个汉字

image: 0.428111 秒	anima.png		9.3MB	4000x2667(4K:3840x2160)
image: 0.201518 秒	appback.png		1.0MB	1920x1080(2K)
image: 0.161042 秒	intro.jpg		411KB	1920x1080(2K)
image: 0.135175 秒	pokemon.jpeg	6.07KB	224x224(input)

image resize time(s) = 0.0542023
image resize time(s) = 0.0534377
image resize time(s) = 0.055892
image resize time(s) = 0.0638162
image resize time(s) = 0.063987


20241010
review图像向量化工程kdm_image
优化修改kdm_image工程review代码规范问题
测试用例添加图像向量化平均耗时统计功能
调测修改后的kdm_image整体功能


Image-embedding kdm review：
# 抽时间进行图片向量化的耗时统计补充统计结果
# image工程名称需要修改成为image-embedding等可以体现具体功能的名称
协同算法团队，考虑将fp32降为fp16
架构中一样的 runtime 放到公共区域作为支撑
# 流程 sentence / feature 补充 限制
和算法同事确认：224x224图片大小是否可以改为和用户平时使用的大小对齐
# 流程中的快模块连接线要由表达，输出是什么
# 输入文本的参数建议添加对文本编码的描述
传入的路径需要兼容或约束以兼容跨操作系统
# kdmg 修改为正确的分组
# kdm_description: 添加文搜图，图搜图的描述，说明使用场景


20241009
研究学习scello CICD使用流程
使用scello构建hoicee_asr_proxy镜像
排查构建hoicee_asr_proxy镜像失败问题
调整hoicee_asr_proxy工程结构


20241008
排查hoicee_asr_proxy s3初始化连接失败问题
测试hoicee_asr_proxy使用dockerfile构建运行镜像
测试hoicee_asr_proxy使用docker-compose.yaml运行实例
优化kdm_image接口和相关文档


20240930
修改kdm_image接口Init传参
同步更新kdm_image相关文档
搭建hoicee_asr_proxy测试环境
测试hoicee_asr_proxy运行


20240929
学习使用drawio绘图工具
绘制kdm_image主体框架设计图
绘制kdm_image图像向量化流程图
绘制kdm_image文本分词向量化流程图


20240927
编写kdm_image文档apis.md
编写kdm_image文档design.md
研究梳理hoicee_asr_proxy部署流程
修改docker-compose.yaml部署环境


20240926
熟悉hoicee_asr_proxy代码
搭建centos编译hoicee_asr_proxy开发环境
编译调试hoicee_asr_proxy代码
修改dockerfile开发环境


20240925
修改kdm_image部分三方依赖
合并kdm_image到kt-lib工程
调测kt-lib中kdm_image模块及整体编译安装
编写添加图像工程文件kdm_image.json


20240924
排查图像通道获取异常问题
定位张量矩阵转换失败问题
调试图像模型推理功能
调试图像向量化结果后处理功能


20240923
开发图像预处理-张量转换
开发图像预处理-张量标准化
编写图像向量化测试用例demo
调试图像预处理功能


opencv4
GraphicsMagick++、
imageMagick/Magick++

Eigen

  # this is heuristically generated, and may not be correct
  find_package(Eigen3 CONFIG REQUIRED)
  target_link_libraries(main PRIVATE Eigen3::Eigen)



  # this is heuristically generated, and may not be correct
  find_package(Eigen3 CONFIG REQUIRED)
  target_link_libraries(main PRIVATE Eigen3::Eigen)



vcpkg install graphicsmagick:x64-linux-dynamic

  # this is heuristically generated, and may not be correct
  find_package(unofficial-graphicsmagick CONFIG REQUIRED)
  target_link_libraries(main PRIVATE unofficial::graphicsmagick::graphicsmagick)

graphicsmagick provides CMake targets:

  # this is heuristically generated, and may not be correct
  find_package(unofficial-graphicsmagick CONFIG REQUIRED)
  target_link_libraries(main PRIVATE unofficial::graphicsmagick::graphicsmagick)


_ZN8
CryptoPP
21
SimpleKeyingInterface
6
SetKeyEPKhmRKNS
_14
NameValuePairs
E

SetKeyEPKhmRKNS

20240920
集成graphicsmagick图像处理库
开发图像预处理-resize、RGB转换功能
开发图像预处理-像素点归一化
调研张量矩阵运算库Eigen


20240919
调研图像处理库
安装opencv及其依赖库
开发图像向量化模型推理功能
开发图像向量化结果后处理功能

```
vcpkg install opencv4[core,default-features,dnn,gtk,jpeg,png,quirc,tiff,webp]:x64-linux-dynamic
apt install libx11-dev libxft-dev libxext-dev libgles2-mesa-dev

```

```
vcpkg install graphicsmagick:x64-linux-dynamic

```

20240918
定位解决文本模型推理负值问题
设计图像向量化功能API
添加构建图像向量化功能模块结构
开发图像向量化模型加载、卸载功能


20240914
修复gitlab/kt-lib-ext/.gitignore和对应模块代码及其依赖
编写文本向量化功能接口测试用例
调测文本向量化功能接口，定位推理时入参无效问题
修改kdm_image相对路径link依赖


20240913
文本向量化结果后处理开发
文本向量化功能接口日志添加
增加各个功能接口状态查询
编译调试功能接口


网络router跟踪:
sngrep


20240912
开发文本预处理功能
开发文本向量化模型加载、卸载功能
开发文本向量化模型推理
调整API接口设计添加错误码功能


20240911
调研张量转换、堆叠、去单C++实现
设计图像的文本分词及向量化功能API
搭建文本分词及向量化工程结构
集成开发fast_tokenizer分词


# image embedding_text
text
name: text
tensor: int64[1,52]
unnorm_text_features
name: unnorm_text_features
tensor: float32[1,512]

# image embedding_image
image
name: image
tensor: float32[1,3,224,224]
unnorm_image_features
name: unnorm_image_features
tensor: float32[1,512]


# intent text_token_embedding
input_ids
name: input_ids
tensor: int64[batch_size,sequence_size]
attention_mask
name: attention_mask
tensor: int64[batch_size,sequence_size]
output
name: output
tensor: float32[batch_size,Divoutput_dim_1]


# intent sort_topN精排序
input_ids
name: input_ids
tensor: int64[batch_size,sequence_size]
attention_mask
name: attention_mask
tensor: int64[batch_size,sequence_size]
output
name: output
tensor: float32[batch_size,2]


# senword
input_ids
name: input_ids
tensor: int64[batch_size,sequence_length]
attention_mask
name: attention_mask
tensor: int64[batch_size,sequence_length]
output
name: output
tensor: float32[batch_size,sequence_length]


20240910
熟悉intent向量化模块
研究现有intent文本分词模块
沟通底层图片向量化及其文本分词向量化
梳理图片向量化及其文本分词向量化的功能模块


// 1 模型和配置信息解码(加载规则)
CAesGcmModule* caceGcmModel;

// 2 意图识别 IR(intent recognition)

	// 2.1 规则匹配意图(rule match intent)
	CRuleMatchIntent* ruleMatchIntent;

	// 2.2 模型匹配意图(model match intent)
		// 2.2.1 文本向量化
		CEmbeddingModule* cmodel;
		// 2.2.2 向量化后检索——topN
		CHnwsModule* chnwModel;
		// 2.2.3 结果排序——精排top1
		CSortModel* smodel;

// 3 槽位抽取 NER(named entity recognition)
CNerMatchModule* nerMatchModel;


20240909
熟悉kt-lib:intent代码结构
归纳汇总intent对外功能API
KDM ASR添加错误码和测试
调试hmac_sha1秘钥编码功能


20240906
调试虚拟机联网问题，待解决
kt-lib:master分支代码修改
kt-lib:master编译调试打包
kt-lib-ext代码合并上传


20240905
修改ErroCode定义
调研hmac_sha1秘钥编码
将sha1编码改为hmac_sha1秘钥编码
外出开天现场熟悉和配置环境


20240904
ErroCode设计与定义
排查解决讯飞签名失败signature, 修改签名公式：base64(hmac_sha1(md5(app_id + timestamp), api_key))实现
KDM ASR增加logger模块
logger功能测试


20240903
修改支持SSL的websocket client库
修改KDM ASR测试用例
测试实时语音识别功能
功能架构拆分会议探讨


20240902
讯飞ASR接口适配调整，添加md5、sha1、base64等功能以支持数字签名；
调试讯飞ASR接口
调试KDM ASR API测试用例
申请讯飞账号key测试功能


20240830
vcpkg尝试编译第三方websocket库
集成websocket框架客户端
调试websocket框架客户端
开发讯飞ASR接口适配


20240829
调研websocket框架
安装vcpkg依赖包管理
开发KDM ASR API测试用例
调试解决KDM ASR接口运行时config文件解析异常


20240828
参加新员工入职培训
kdm_asr toml配置库改为nlohmann-json
调试VSCode + MinGW_GCC编译环境
调试kdm_asr编译问题


20240827
细化libnm API功能列表
麒麟OS产品用户手册阅读
麒麟OS SDK开发指南阅读
汇总使用麒麟OS SDK功能列表


WinLibs standalone build of GCC and MinGW-w64 for Windows：
https://winlibs.com


下周五前：（20240830）
WiFi无线网络和有线网络交互切换配置，调研系统层接口可处理哪些能力；
麒麟商店，调研查询、安装等可用接口，如何用；


1、麒麟操作系统的网络连接 WiFi 和 有线网		调研wifi和有线可以调用到的能力(接口、命令)
WiFi无线网络和有线网络交互切换配置，调研系统层接口可处理哪些能力；

2、软件安装	调用麒麟商店接口，协调麒麟的查询、安装接口
麒麟商店，调研查询、安装等可用接口，如何用；


梳理麒麟软件商店-查询、安装接口

大家上午好，我是研发部端上语音团队的C++开发——李廷，之前一直从事智能语音引擎相关工作，对AI语音模型推理和工程落地这方面比较熟悉，来到诺谛大家庭已半个月左右，主要也是围绕语音和C++工程开发方面开展工作。
希望未来和大家一起努力工作，相互学习，共同成长，为我们这个大家庭的未来发展增砖添瓦，贡献一份力量。


命令行apt/libapt-pkg
麒麟操作系统的官方API d-bus


https://www.kylinos.cn/upload/product/20240613/87e4b1d1e8520f894c247e2fac4a2087.pdf

调研sdbus-c++库
调研dbus-cxx库


20240826
补充dbus和nm配合使用功能列表
调研sdbus-c++库
调研麒麟商店软件查询接口
调研麒麟商店软件安装接口


20240823
调研dbus和nm配合使用API管控系统网络
调研dbus-cxx库
调研libnm库
汇总dbus和nm配合使用功能列表


20240822
调研ip/ifconfig命令管控系统网络
调研wicd-cli/nmcli命令管控系统网络
调研dbus框架
调研dbus和wicd配合使用API管控系统网络


20240821
开发KDM ASR配置功能
搭建vcpkg依赖环境
调试CMake预设配置
编译调试KDM ASR接口框架


20240820
分析recogProxy讯飞ASR接口
分析recogProxy微软ASR接口
设计开发KDM ASR整体接口
编写标准化kd_asr.kdm


20240819
调研讯飞云侧ASR API接口
调研微软云侧ASR API接口
构建KDM ASR软件工程
设计KDM ASR API接口

### 开发环境依赖项

- 语言版本：`C++17`
- 所需的第三方库或框架：`vcpkg`、`Boost`、`Websocket`

### 开发环境搭建步骤

1. 安装依赖项：
   - Linux 开发环境：

    ```bash

    <!-- 基础依赖 -->
    sudo apt install -y vim ssh curl zip unzip git cmake build-essential pkg-config

    <!-- cmake 3.30 -->
    wget cmake.sh

    <!-- C++依赖管理器 -->
    git clone https://github.com/microsoft/vcpkg.git ~/vcpkg
    cd ~/vcpkg
    ./bootstrap-vcpkg.sh

    ```

2. 配置环境变量（如适用）：

   ```bash

    echo 'export VCPKG_ROOT="$HOME/vcpkg"' >> ~/.bashrc
    echo 'export PATH="$VCPKG_ROOT:$PATH"' >> ~/.bashrc
    source ~/.bashrc

   ```

3. 克隆仓库并编译代码：

   ```bash

   git clone http://gitlab.knowdee.com/kdm/cpp/knowdee/voice-processer.git


   ```


KD_ASR_API SDK:
KdAsr(compsited with AsrApi instance)
	AsrApi(inherite from this)
		XfyunAsr
		MsAsr(microsoft)
		KnowDeeAsr(local)
		FunAsr
		BaiDuAsr
		TencentAsr

kt-lib代码运行时加载so失败问题
4、消息协议json string

ssh lenovo@192.168.51.215
scp lenovo@192.168.51.215:/app/com.knowdee.


20240816
AIPC功能体验和感受汇总
梳理kt-lib代码grpc各类cmd消息处理流程
kt-lib代码运行时kdm-pkg::create_directory抛异常
kt-lib代码问题汇总



20240815
kt-lib代码阅读熟悉				学习kt-lib代码架构，通过nodejs调用各个功能KModuleInstance和grpc调用各个功能KModuleInstance
AIPC功能体验（10个体验感受）			遇到卡死无结果返回情况，文本交互没走完流程
kt-lib代码编译依赖安装								安装虚拟机编译环境的kt-lib所需依赖
kt-lib代码编译过程中resource缺少问题排查					拷贝215环境的文件解决

（Make Error at CMakeLists.txt:40 (file):  file COPY cannot find "/data/usershare/projects/kt/kt-lib/../resource": No  such file or



kt-lib代码问题：
1、kt-lib整体软件架构属于传统的软件架构风格，是大而全，可以按照功能拆分为多个轻量化架构的敏捷软件工程，便于其中各个功能模块复用到未来其他软件工程。
2、同一个软件repos的编程范式比较多样，揉合了面向过程C、基于对象C++、面向对象C++、函数式编程的多种编程范式，建议以其中一种编程范式为主，必要时可以另一种编程范式为辅，最好不超过两种，特殊情况除外。
3、同一个软件repos的代码style多种多样，后续标准化可按照约定统一规范。
4、C++软件工程中，使用了C语言风格的代码写法，最好以现代C++的写法替代（如函数回调typedef以std::function替代C风格的函数指针和参数等）。
5、void*等裸指针和new堆内存的写法较多，可以考虑使用现代C++的智能指针（如std::shared_ptr或std::unique_ptr）代替，避免内存泄漏或双重释放。
6、函数传参和返回值有一些是by value传值写法，可考虑改为by reference写法，同时只读参数和只读返回值建议统一加上const修饰符，以提高代码效率和安全性。
7、头文件的分层和依赖比较随意，尽可能在.cc和.cpp中include需要的头文件，.h文件只包含必须的头文件和类型定义，避免过多对外暴露实现，造成不可预知的冲突。
8、命名空间的引入比较重，尽量避免直接在头文件中using namespace std或指定引入具体使用的std::something。
9、各个模块代码没有做命名空间的管理，建议各个模块代码放入对应命令空间内。
10、缺乏公共基础工具的统一集中管理，造成各个模块内部有一些小功能重复code。
11、有些指针缺少安全性检查，可对此添加空指针和非法指针检查。
12、可能抛异常的函数调用，酌情使用try-catch块处理异常安全，明确nothrow方法，避免使用异常捕获。



AIPC体验感受：
1、app启动后弹出的对话框UI挺迅速漂亮。
2、文本对话交互时，指示其打开操作系统中的常规应用（如计算器、终端、谷歌浏览器、文件资源管理等）比较顺畅无误。
3、指示其打开设置时，识别可能出错了，总是打开麒麟管家。
4、日常话题问答对话时，总是提示，感受不太友好，希望能够覆盖广泛的主题领域知识。
5、对话的实时响应速度还可以，没有延迟很长时间，能接受，但响应速度不如通义千问快。
6、交互时有的问题，会出现答非所问的情况，意图识别的准确率待提高。




20240814
PC端搭建虚拟机VMware和麒麟系统等运行调试环境
系统概要设计 - AIPC端服务技术文档学习
系统概要设计 - AIPC小天端应用技术文档学习
kt-lib代码阅读熟悉


AIPC功能体验
AIPC现有代码学习


20240813
CICD流程，Gitlab的目录结构管理等柔性软件工程学习
KDS,KDM相关规约描述及其分层等柔性软件工程学习
端上&语音相关技术架构文档学习
C++开发环境搭建配置


20240812
入职手续办理
个人PC办公环境安装
各个系统（wiki/钉钉/禅道/企业邮箱）账号登录验证
个人信息采集填写
学习员工手册和管理规定



公共讨论会议及其他团队事务


lenovo@lenovo-pc:~$ ldd --version
ldd (Ubuntu GLIBC 2.31-0kylin9.1k21.2) 2.31
Copyright (C) 2020 自由软件基金会。
这是一个自由软件；请见源代码的授权条款。本软件不含任何没有担保；甚至不保证适销性
或者适合某些特殊目的。
由 Roland McGrath 和 Ulrich Drepper 编写。
lenovo@lenovo-pc:~$ g++ --version
g++ (Kylin 9.3.0-10kylin5k0.5) 9.3.0
Copyright (C) 2019 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

lenovo@lenovo-pc:~$ gcc --version
gcc (Kylin 9.3.0-10kylin5k0.5) 9.3.0
Copyright (C) 2019 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

root@docker-desktop:/\work# ldd --version
ldd (Ubuntu GLIBC 2.31-0ubuntu9.16) 2.31
Copyright (C) 2020 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
Written by Roland McGrath and Ulrich Drepper.


root@docker-desktop:/\work# gcc --version
gcc (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0
Copyright (C) 2019 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

root@docker-desktop:/\work# g++ --version
g++ (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0
Copyright (C) 2019 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

sudo nano /etc/systemd/system/tinysshd.service

D:\Virtual Machines\Kylin10\Kylin10.vmdk

D:\tools\Kylin-Desktop-V10-SP1-2403-Beta2-20240103-x86_64.iso

AIPC1.0 测试机器：
192.168.51.215
lenovo/qwer1234


ldap/vpn/wiki/gitlab:
litt/liting2131

禅道：
litt/Liting2131.

企业邮箱：
litt@knowdee.com/Liting2131.
litt@knowdee.com/Liting2131,


新版scello地址：
http://scello.knowdee.com
litt/Liting2131

hyper-v:kylin2403系统账号
lit/7777777
