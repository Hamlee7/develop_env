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


马上金融
华夏基金


kd-asr-proxy
rtp端口号范围太小时，服务启动log提示端口配置不合理并自动退出
(max-min)/4 < 1

windows 磁盘清理

调试coredump文件工具：
coredumpctl
fs/mod_unimrcp/apt_timer_queue.c:

apt_timer_queue_advance
apt_timer_set/apt_timers_reschedule



线上测试kd-asr-proxy镜像5.0版本，定位http超时问题
修改sysfunc中intent调用流程与逻辑，因抽槽模块更新，sysfunc解析槽位信息无法兼容

mrcp和freeswitch
测试freeswitch服务功能
构建freeswitch docker镜像


libglibmm-2.4-dev \
libgiomm-2.4-dev
${GIOMM_LIBRARIES} Qt5::Gui




宋Pro DM-i
宋Plus DM-i
宋L DM-i


## FreeSWITCH高可用部署与云原生集群部署
### 主备双机HA
[LiveVideoStack](https://cloud.tencent.com/developer/article/2208126)

FreeSWITCH的主备切换原理：首先主机包含一个Param，参数为：<params name=“track-calls” value=“true”/>，如果我们开启此参数，它就会实时的将通话数据写入数据库当中。当然这个会有一定的开销，因为需要实时的写入数据库，比如每秒有一千路通话、一万路通话，它的开销就会很大，所以这种双机切换会对系统的吞吐量有一定影响。但在一些必要的场景下，我们往往是需要牺牲一些性能来更好的实现高可用的。

当备机发生切换的时候，备机会执行一个 sofia recover 命令，从数据库中取得数据重建通话的场景，向A和B发送 reINVITE。前面我们说A和B感知不到，其实也能感知到，因为A和B收到了重新建连的邀请，继续进行通话。一般这个通话过程大概在1-3秒内解决，A和B只是觉得会短暂的卡顿，不用挂断重新呼叫。

### 三机HA

### 自动弹性伸缩HA

asr engine:AWS、Xunfei、Azure、Lenovo_HTTP、Azure_cont
tts engine:AWS、Xunfei、Lenovo


mod_xml_curl


tts:
https://learn.microsoft.com/en-us/azure/ai-services/speech-service/text-to-speech

asr:
https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-to-text


lua: socket.core


港铁POC:
fs和mrcp环境目录是192.168.109.85:/home/hoicee/freeswitch
堡垒机地址 ：http://172.70.90.2/
港铁demo目录下 服务器
192.168.109.84    bot
192.168.109.85   db+hoicee



freeswitch:0.1.0
lua-socket
apr
mrcp-deps

手动构建kd-unimrcp docker镜像

支持微软asr/tts(azure sdk)
调研确认微软asr/tts支持中文普通话、粤语、英语



lsof -i UDP -a -c freeswitch|grep ":26"|wc -l

ss -tulwnp
ss -unlp | grep "freeswitch"




ss -unlp | grep "freeswitch"|grep ":26*"|wc -l
ss -unlp | grep "unimrcp"|grep ":15"|wc -l
ss -unlp | grep "asr"|grep ":30"|wc -l

38
0
14
26



54
0
18
36


300
60


    <!-- <param name="rtp-start-port" value="26184"/> -->
    <param name="rtp-start-port" value="26424"/>
    <param name="rtp-end-port" value="26484"/>




徐工asr识别问题

20250526
定位asr相关代码并修复其结果累加BUG




xugong_prd:
knodi_asr_proxy  | [kd-mrcp-asr] lenovoVadInst::init vad iVadEnergyStart = 70
knodi_asr_proxy  | [kd-mrcp-asr] lenovoVadInst::init iVadEnergeStop = 40
knodi_asr_proxy  | [kd-mrcp-asr] lenovoVadInst::init iMaxSpPause = 500 ms, iLRelax = 250 ms

gongtie_poc:
unimrcp5  | [kd-mrcp-asr] lenovoVadInst::init vad iVadEnergyStart = 60
unimrcp5  | [kd-mrcp-asr] lenovoVadInst::init iVadEnergeStop = 30
unimrcp5  | [kd-mrcp-asr] lenovoVadInst::init iMaxSpPause = 600 ms, iLRelax = 250 ms




aws ecr get-login-password --region cn-north-1 | docker login --username AWS  --password-stdin  865677308458.dkr.ecr.cn-north-1.amazonaws.com.cn
aws ecr get-login-password --region cn-north-1 | docker login --username AWS  --password-stdin  865677308458.dkr.ecr.cn-north-1.amazonaws.com.cn




kd-asr-proxy

devel:
apt install -y wget gcc gcc-c++ curl librdkafka-dev libcurl4-gnutls-dev

runtime:
apt update && apt install -y libcurl4-gnutls-dev

libcppkafka.so
librdkafka.so
librdkafka++.so
libaws-cpp-sdk-s3.so
libjrtplib.so
libyaml-cpp.a


20250527
排查解决kd-asr-proxy服务启动时崩溃问题
合并分支修改kd-asr-proxy代码，剥离s3模块
构建kd-asr-proxy docker镜像
调试kd-asr-proxy镜像运行，修复容器内启动缺少curl依赖问题



20250526
kd-asr-proxy工程适配ubuntu22.04
源码编译依赖yaml ubuntu版本
源码编译依赖kafka ubuntu版本
源码编译依赖jrtplib ubuntu版本


freeswitch -> voice_agent:
websocket传输音频流
websocket接收处理后音频
调试桥接电话功能
session 连接websocket server
mod_audio_stream监听音频
mod_audio_stream监听事件
mod_audio_fork
桥接到软电话
桥接阻塞调试
联调音频传输和分析
寻找异步处理方式


xugong_prd:
2025-04-24 22:40:34.641277 0.00% [NOTICE] mrcp_client.c:719 () MRCP Client Started
2025-04-24 22:40:34.641284 0.00% [DEBUG] apt_consumer_task.c:135 () Wait for Messages [MRCP Client]
2025-04-24 22:40:34.641290 0.00% [CONSOLE] switch_loadable_module.c:1772 Successfully Loaded [mod_unimrcp]
2025-04-24 22:40:34.641301 0.00% [NOTICE] switch_loadable_module.c:537 Adding Speech interface 'unimrcp'
2025-04-24 22:40:34.641320 0.00% [NOTICE] switch_loadable_module.c:565 Adding ASR interface 'unimrcp'
2025-04-24 22:40:34.641611 0.00% [CONSOLE] switch_loadable_module.c:1772 Successfully Loaded [mod_event_socket]
2025-04-24 22:40:34.641629 0.00% [NOTICE] switch_loadable_module.c:329 Adding Application 'socket'
2025-04-24 22:40:34.641649 0.00% [NOTICE] switch_loadable_module.c:389 Adding API Function 'event_sink'
2025-04-24 22:40:34.642822 0.00% [INFO] mod_sofia.c:6665 Starting initial message thread.
2025-04-24 22:40:34.642904 0.00% [DEBUG] sofia.c:4727 debug [0]
2025-04-24 22:40:34.642912 0.00% [DEBUG] sofia.c:4727 sip-trace [no]
2025-04-24 22:40:34.642915 0.00% [DEBUG] sofia.c:4727 NDLB-received-in-nat-reg-contact [true]
2025-04-24 22:40:34.642933 0.00% [DEBUG] sofia.c:4727 apply-candidate-acl [rfc1918.auto]
2025-04-24 22:40:34.642948 0.00% [DEBUG] sofia.c:4727 apply-candidate-acl [wan.auto]
2025-04-24 22:40:34.642957 0.00% [DEBUG] sofia.c:4727 codecs [OPUS,G722,PCMU,PCMA,H264,VP8]
2025-04-24 22:40:34.642972 0.00% [DEBUG] sofia.c:4727 odbc-dsn [pgsql://host=10.188.6.233 port=5432 dbname=freeswitch user=postgres password=3or+l2fZuXoSiLsFSwo]
2025-04-24 22:40:34.642979 0.00% [DEBUG] sofia.c:4727 sip-capture [no]
2025-04-24 22:40:34.642982 0.00% [DEBUG] sofia.c:4727 rfc2833-pt [101]
2025-04-24 22:40:34.642985 0.00% [DEBUG] sofia.c:4727 sip-port [15080]
2025-04-24 22:40:34.642989 0.00% [DEBUG] sofia.c:4727 dialplan [XML]
2025-04-24 22:40:34.642995 0.00% [DEBUG] sofia.c:4727 context [public]
2025-04-24 22:40:34.643000 0.00% [DEBUG] sofia.c:4727 dtmf-duration [2000]
2025-04-24 22:40:34.643006 0.00% [DEBUG] sofia.c:4727 inbound-codec-prefs [OPUS,G722,PCMU,PCMA,H264,VP8]
2025-04-24 22:40:34.643018 0.00% [DEBUG] sofia.c:4727 outbound-codec-prefs [OPUS,G722,PCMU,PCMA,H264,VP8]
2025-04-24 22:40:34.643026 0.00% [DEBUG] sofia.c:4727 hold-music [local_stream://moh]
2025-04-24 22:40:34.643030 0.00% [DEBUG] sofia.c:4727 rtp-timer-name [soft]
2025-04-24 22:40:34.643038 0.00% [DEBUG] sofia.c:4727 aggressive-nat-detection [true]
2025-04-24 22:40:34.643042 0.00% [DEBUG] sofia.c:4727 local-network-acl [none]
2025-04-24 22:40:34.643055 0.00% [DEBUG] sofia.c:4727 manage-presence [false]
2025-04-24 22:40:34.643059 0.00% [DEBUG] sofia.c:4727 aggressive-nat-detection [true]
2025-04-24 22:40:34.643062 0.00% [DEBUG] sofia.c:4727 inbound-codec-negotiation [generous]
2025-04-24 22:40:34.643067 0.00% [DEBUG] sofia.c:4727 nonce-ttl [60]
2025-04-24 22:40:34.643073 0.00% [DEBUG] sofia.c:4727 auth-calls [false]
2025-04-24 22:40:34.643080 0.00% [DEBUG] sofia.c:4727 inbound-late-negotiation [true]
2025-04-24 22:40:34.643095 0.00% [DEBUG] sofia.c:4727 inbound-zrtp-passthru [true]
2025-04-24 22:40:34.643100 0.00% [DEBUG] sofia.c:4727 rtp-ip [10.188.6.233]
2025-04-24 22:40:34.643104 0.00% [DEBUG] sofia.c:4727 sip-ip [10.188.6.233]
2025-04-24 22:40:34.643107 0.00% [DEBUG] sofia.c:4727 ext-sip-ip [223.109.89.196]
2025-04-24 22:40:34.643117 0.00% [DEBUG] sofia.c:4727 ext-rtp-ip [223.109.89.196]
2025-04-24 22:40:34.643124 0.00% [DEBUG] sofia.c:4727 rtp-timeout-sec [300]
2025-04-24 22:40:34.643127 0.00% [WARNING] sofia.c:5328 rtp-timeout-sec deprecated use media_timeout variable.
2025-04-24 22:40:34.643130 0.00% [DEBUG] sofia.c:4727 rtp-hold-timeout-sec [1800]
2025-04-24 22:40:34.643133 0.00% [WARNING] sofia.c:5335 rtp-hold-timeout-sec deprecated use media_hold_timeout variable.
2025-04-24 22:40:34.643136 0.00% [DEBUG] sofia.c:4727 tls [true]
2025-04-24 22:40:34.643143 0.00% [DEBUG] sofia.c:4727 tls-only [false]
2025-04-24 22:40:34.643150 0.00% [DEBUG] sofia.c:4727 tls-bind-params [transport=tls]
2025-04-24 22:40:34.643156 0.00% [DEBUG] sofia.c:4727 tls-sip-port [5081]
2025-04-24 22:40:34.643160 0.00% [DEBUG] sofia.c:4727 tls-cert-dir [/usr/local/freeswitch/certs]
2025-04-24 22:40:34.643166 0.00% [DEBUG] sofia.c:4727 tls-passphrase []
2025-04-24 22:40:34.643172 0.00% [DEBUG] sofia.c:4727 tls-verify-date [true]
2025-04-24 22:40:34.643178 0.00% [DEBUG] sofia.c:4727 tls-verify-policy [none]
2025-04-24 22:40:34.643183 0.00% [DEBUG] sofia.c:4727 tls-verify-depth [2]
2025-04-24 22:40:34.643188 0.00% [DEBUG] sofia.c:4727 tls-verify-in-subjects []
2025-04-24 22:40:34.643193 0.00% [DEBUG] sofia.c:4727 tls-version [tlsv1,tlsv1.1,tlsv1.2]
2025-04-24 22:40:34.643204 0.00% [DEBUG] sofia.c:4727 ws-binding [:5066]
2025-04-24 22:40:34.643211 0.00% [DEBUG] sofia.c:4727 wss-binding [:7443]
2025-04-24 22:40:34.643231 0.00% [INFO] sofia.c:6187 Setting MAX Auth Validity to 0 Attempts
2025-04-24 22:40:34.643314 0.00% [NOTICE] sofia.c:6347 Connecting ODBC Profile external [sofia_reg_external]
2025-04-24 22:40:34.643383 0.00% [DEBUG] sofia.c:3162 Creating agent for external




210:
2025-05-14 13:23:10.158159 0.00% [NOTICE] mrcp_client.c:719 () MRCP Client Started
2025-05-14 13:23:10.158182 0.00% [DEBUG] apt_consumer_task.c:135 () Wait for Messages [MRCP Client]
2025-05-14 13:23:10.158245 0.00% [CONSOLE] switch_loadable_module.c:1772 Successfully Loaded [mod_unimrcp]
2025-05-14 13:23:10.158300 0.00% [NOTICE] switch_loadable_module.c:537 Adding Speech interface 'unimrcp'
2025-05-14 13:23:10.158371 0.00% [NOTICE] switch_loadable_module.c:565 Adding ASR interface 'unimrcp'
2025-05-14 13:23:10.159051 0.00% [CONSOLE] switch_loadable_module.c:1772 Successfully Loaded [mod_event_socket]
2025-05-14 13:23:10.159102 0.00% [NOTICE] switch_loadable_module.c:329 Adding Application 'socket'
2025-05-14 13:23:10.159142 0.00% [NOTICE] switch_loadable_module.c:389 Adding API Function 'event_sink'
2025-05-14 13:23:10.161856 0.00% [INFO] mod_sofia.c:6665 Starting initial message thread.
2025-05-19 15:40:55.117498 0.00% [INFO] mod_sofia.c:6665 Starting initial message thread.
2025-05-19 15:40:55.117658 0.00% [DEBUG] sofia.c:4727 debug [0]
2025-05-19 15:40:55.117689 0.00% [DEBUG] sofia.c:4727 sip-trace [no]
2025-05-19 15:40:55.117696 0.00% [DEBUG] sofia.c:4727 NDLB-received-in-nat-reg-contact [true]
2025-05-19 15:40:55.117717 0.00% [DEBUG] sofia.c:4727 apply-candidate-acl [rfc1918.auto]
2025-05-19 15:40:55.117732 0.00% [DEBUG] sofia.c:4727 apply-candidate-acl [wan.auto]
2025-05-19 15:40:55.117741 0.00% [DEBUG] sofia.c:4727 codecs [OPUS,G722,PCMU,PCMA,H264,VP8]
2025-05-19 15:40:55.117762 0.00% [DEBUG] sofia.c:4727 sip-capture [no]
2025-05-19 15:40:55.117768 0.00% [DEBUG] sofia.c:4727 rfc2833-pt [101]
2025-05-19 15:40:55.117776 0.00% [DEBUG] sofia.c:4727 sip-port [15080]
2025-05-19 15:40:55.117783 0.00% [DEBUG] sofia.c:4727 dialplan [XML]
2025-05-19 15:40:55.117796 0.00% [DEBUG] sofia.c:4727 context [public]
2025-05-19 15:40:55.117804 0.00% [DEBUG] sofia.c:4727 dtmf-duration [2000]
2025-05-19 15:40:55.117813 0.00% [DEBUG] sofia.c:4727 inbound-codec-prefs [OPUS,G722,PCMU,PCMA,H264,VP8]
2025-05-19 15:40:55.117827 0.00% [DEBUG] sofia.c:4727 outbound-codec-prefs [OPUS,G722,PCMU,PCMA,H264,VP8]
2025-05-19 15:40:55.117850 0.00% [DEBUG] sofia.c:4727 hold-music [local_stream://moh]
2025-05-19 15:40:55.117858 0.00% [DEBUG] sofia.c:4727 rtp-timer-name [soft]
2025-05-19 15:40:55.117865 0.00% [DEBUG] sofia.c:4727 aggressive-nat-detection [true]
2025-05-19 15:40:55.117870 0.00% [DEBUG] sofia.c:4727 local-network-acl [none]
2025-05-19 15:40:55.117877 0.00% [DEBUG] sofia.c:4727 manage-presence [false]
2025-05-19 15:40:55.117883 0.00% [DEBUG] sofia.c:4727 aggressive-nat-detection [true]
2025-05-19 15:40:55.117889 0.00% [DEBUG] sofia.c:4727 inbound-codec-negotiation [generous]
2025-05-19 15:40:55.117896 0.00% [DEBUG] sofia.c:4727 nonce-ttl [60]
2025-05-19 15:40:55.117923 0.00% [DEBUG] sofia.c:4727 auth-calls [false]
2025-05-19 15:40:55.117934 0.00% [DEBUG] sofia.c:4727 inbound-late-negotiation [true]
2025-05-19 15:40:55.117939 0.00% [DEBUG] sofia.c:4727 inbound-zrtp-passthru [true]
2025-05-19 15:40:55.117967 0.00% [DEBUG] sofia.c:4727 rtp-ip [172.70.10.210]
2025-05-19 15:40:55.117976 0.00% [DEBUG] sofia.c:4727 sip-ip [172.70.10.210]
2025-05-19 15:40:55.117983 0.00% [DEBUG] sofia.c:4727 ext-sip-ip [172.70.10.210]
2025-05-19 15:40:55.118001 0.00% [DEBUG] sofia.c:4727 ext-rtp-ip [172.70.10.210]
2025-05-19 15:40:55.118011 0.00% [DEBUG] sofia.c:4727 rtp-timeout-sec [300]
2025-05-19 15:40:55.118018 0.00% [WARNING] sofia.c:5328 rtp-timeout-sec deprecated use media_timeout variable.
2025-05-19 15:40:55.118042 0.00% [DEBUG] sofia.c:4727 rtp-hold-timeout-sec [1800]
2025-05-19 15:40:55.118050 0.00% [WARNING] sofia.c:5335 rtp-hold-timeout-sec deprecated use media_hold_timeout variable.
2025-05-19 15:40:55.118055 0.00% [DEBUG] sofia.c:4727 tls [true]
2025-05-19 15:40:55.118064 0.00% [DEBUG] sofia.c:4727 tls-only [false]
2025-05-19 15:40:55.118077 0.00% [DEBUG] sofia.c:4727 tls-bind-params [transport=tls]
2025-05-19 15:40:55.118085 0.00% [DEBUG] sofia.c:4727 tls-sip-port [5081]
2025-05-19 15:40:55.118094 0.00% [DEBUG] sofia.c:4727 tls-cert-dir [/usr/local/freeswitch/certs]
2025-05-19 15:40:55.118109 0.00% [DEBUG] sofia.c:4727 tls-passphrase []
2025-05-19 15:40:55.118130 0.00% [DEBUG] sofia.c:4727 tls-verify-date [true]
2025-05-19 15:40:55.118139 0.00% [DEBUG] sofia.c:4727 tls-verify-policy [none]
2025-05-19 15:40:55.118150 0.00% [DEBUG] sofia.c:4727 tls-verify-depth [2]
2025-05-19 15:40:55.118158 0.00% [DEBUG] sofia.c:4727 tls-verify-in-subjects []
2025-05-19 15:40:55.118165 0.00% [DEBUG] sofia.c:4727 tls-version [tlsv1,tlsv1.1,tlsv1.2]
2025-05-19 15:40:55.118175 0.00% [DEBUG] sofia.c:4727 ws-binding [:5066]
2025-05-19 15:40:55.118182 0.00% [DEBUG] sofia.c:4727 wss-binding [:37443]
2025-05-19 15:40:55.118195 0.00% [INFO] sofia.c:6187 Setting MAX Auth Validity to 0 Attempts
2025-05-19 15:40:55.118400 0.00% [NOTICE] sofia.c:6347 Connecting ODBC Profile external [sofia_reg_external]
2025-05-19 15:40:55.118650 0.00% [DEBUG] sofia.c:3162 Creating agent for external



20250523
定位解决颐和园PRE测试asr吞字问题
排查颐和园PRE测试按键选择无效问题
分析徐工PRD环境asr服务日志
修复徐工PRD转人工后kd-asr-proxy服务转写结果累加问题


/usr/bin/ld: src/utils/kafka/libKafka.a(kafka.cpp.o): in function `utils::KafkaImpl::Init(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)':
/usr/local/src/.local/lit/kd-asr-proxy/src/utils/kafka/kafka.cpp:26: undefined reference to `cppkafka::Configuration::set(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)'
/usr/bin/ld: /usr/local/src/.local/lit/kd-asr-proxy/src/utils/kafka/kafka.cpp:35: undefined reference to `cppkafka::Configuration::set_error_callback(std::function<void (cppkafka::KafkaHandleBase&, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)>)'


/usr/bin/ld: src/utils/kafka/libKafka.a(kafka.cpp.o): in function `utils::KafkaImpl::Produce(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)':
/usr/local/src/.local/lit/kd-asr-proxy/src/utils/kafka/kafka.cpp:46: undefined reference to `cppkafka::Buffer::Buffer(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)'


/usr/bin/ld: src/utils/kafka/libKafka.a(kafka.cpp.o): in function `std::_Function_handler<void (cppkafka::Producer&, cppkafka::Message const&), utils::KafkaImpl::Init(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)::{lambda(cppkafka::Producer&, cppkafka::Message const&)#1}>::_M_invoke(std::_Any_data const&, cppkafka::Producer&, cppkafka::Message const&)':
/usr/local/src/.local/lit/kd-asr-proxy/src/utils/kafka/kafka.cpp:28: undefined reference to `cppkafka::Error::to_string[abi:cxx11]() const'


/usr/bin/ld: src/session/libSession.a(rtp_session.cpp.o): in function `session::RTP::errorCheck(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&)':
/usr/local/src/.local/lit/kd-asr-proxy/src/session/rtp_session.cpp:124: undefined reference to `jrtplib::RTPGetErrorString[abi:cxx11](int)'


/usr/bin/ld: src/utils/s3/libAwsS3.a(s3.cpp.o): in function `utils::aws_s3::Client::ListBuckets(std::set<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::less<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >&)':
/usr/local/src/.local/lit/kd-asr-proxy/src/utils/s3/s3.cpp:241: undefined reference to `Aws::S3::S3Client::ListBuckets() const'


collect2: error: ld returned 1 exit status






20250522
准备并安装徐工PRD环境网络相关工具
统计徐工PRD环境fs语音流端口占用情况
查找并下载徐工PRD环境asr转写结果累加badcase对应asr日志
定位徐工PRD环境转人工后asr转写结果累加问题






排查徐工PRD 转人工asr转写
排查徐工PRD 转人工asr转写 fs调用tts交互流程

定位fs->mrcp->asr各个流程未发现异常问题，讯飞返回识别结果少部分句子



徐工线上语音端口占用问题排查(rtp/udp)
fs:300/150/26-64
- RTP_START_PORT=26184
# for verfiy port jump
#- RTP_START_PORT=26444
- RTP_END_PORT=26484

mrcp:100/50/0-6
- RTP_PORT_MIN=15184
- RTP_PORT_MAX=15284

kd-asr-proxy:300/150/6-20
- ASRPROXY_RTP_MIN=30000
- ASRPROXY_RTP_MAX=30300







  <cli-keybindings>
    <key name="1" value="help"/>
    <key name="2" value="status"/>
    <key name="3" value="show channels"/>
    <key name="4" value="show calls"/>
    <key name="5" value="sofia status"/>
    <key name="6" value="reloadxml"/>
    <key name="7" value="console loglevel 0"/>
    <key name="8" value="console loglevel 7"/>
    <key name="9" value="sofia status profile internal"/>
    <key name="10" value="sofia profile internal siptrace on"/>
    <key name="11" value="sofia profile internal siptrace off"/>
    <key name="12" value="version"/>
  </cli-keybindings>


2a05b193-2a1f-485f-9452-cba8c0a6ba3b 2025-05-22 14:37:24.275714 85.13% [DEBUG] sofia.c:7493 Channel sofia/external/9898000630388946@223.109.89.196 entering state [completing][200]
2a05b193-2a1f-485f-9452-cba8c0a6ba3b 2025-05-22 14:37:24.275714 85.13% [DEBUG] sofia.c:7503 Remote SDP:
2a05b193-2a1f-485f-9452-cba8c0a6ba3b v=0
2a05b193-2a1f-485f-9452-cba8c0a6ba3b o=- 8996708521907119029 3 IN IP4 127.0.0.1
2a05b193-2a1f-485f-9452-cba8c0a6ba3b s=-
2a05b193-2a1f-485f-9452-cba8c0a6ba3b t=0 0
2a05b193-2a1f-485f-9452-cba8c0a6ba3b a=msid-semantic: WMS c40f738d-0ed4-4268-b8e8-30982490dcd4
2a05b193-2a1f-485f-9452-cba8c0a6ba3b m=audio 53769 RTP/SAVPF 8 101
2a05b193-2a1f-485f-9452-cba8c0a6ba3b c=IN IP4 10.1.88.4
2a05b193-2a1f-485f-9452-cba8c0a6ba3b a=rtpmap:8 PCMA/8000
2a05b193-2a1f-485f-9452-cba8c0a6ba3b a=rtpmap:101 telephone-event/8000
2a05b193-2a1f-485f-9452-cba8c0a6ba3b a=rtcp:9 IN IP4 0.0.0.0
2a05b193-2a1f-485f-9452-cba8c0a6ba3b a=candidate:348375836 1 udp 2122260223 10.1.88.4 53769 typ host generation 0 network-id 1
2a05b193-2a1f-485f-9452-cba8c0a6ba3b a=candidate:3932757896 1 tcp 1518280447 10.1.88.4 9 typ host tcptype active generation 0 network-id 1
2a05b193-2a1f-485f-9452-cba8c0a6ba3b a=ice-ufrag:Rx6W
2a05b193-2a1f-485f-9452-cba8c0a6ba3b a=ice-pwd:RcHG0VUwcfcOydDtAk/JBq1e
2a05b193-2a1f-485f-9452-cba8c0a6ba3b a=ice-options:trickle
2a05b193-2a1f-485f-9452-cba8c0a6ba3b a=fingerprint:sha-256 18:2D:C8:0E:AB:05:24:90:7F:39:A2:EA:44:F8:AB:52:39:40:6C:45:93:40:94:AB:D1:5C:43:22:6C:70:F9:06
2a05b193-2a1f-485f-9452-cba8c0a6ba3b a=setup:active
2a05b193-2a1f-485f-9452-cba8c0a6ba3b a=mid:0
2a05b193-2a1f-485f-9452-cba8c0a6ba3b a=rtcp-mux
2a05b193-2a1f-485f-9452-cba8c0a6ba3b a=ssrc:2030615433 cname:w2Z3stqi9dRZMiBM
2a05b193-2a1f-485f-9452-cba8c0a6ba3b a=ssrc:2030615433 msid:c40f738d-0ed4-4268-b8e8-30982490dcd4 daa3c70b-4ec3-4d5d-bb19-43aa577e8ace
2a05b193-2a1f-485f-9452-cba8c0a6ba3b
2a05b193-2a1f-485f-9452-cba8c0a6ba3b 2025-05-22 14:37:24.295714 85.13% [DEBUG] sofia.c:7493 Channel sofia/external/9898000630388946@223.109.89.196 entering state [ready][200]




34317225-57fe-4e9b-9346-eb0c058be764 2025-04-28 09:58:40.575714 98.57% [NOTICE] switch_rtp.c:1436 Auto Changing audio stun/rtp/dtls port from 10.1.88.17:64246 to 221.178.242.16:53222 idx:-1
34317225-57fe-4e9b-9346-eb0c058be764 2025-04-28 09:58:40.575714 98.57% [DEBUG] switch_ivr_async.c:1778 No silence detection configured; assuming start of speech


ecs-prd-crm-vrs-0001-0001:ssh                                    => 10.1.1.52                                                        10.3Mb  10.1Mb  9.41Mb
                                                                 <=                                                                   230Kb   231Kb   221Kb
ecs-prd-crm-vrs-0001-0001:35774                                  => 100.125.32.71                                                       0b   2.89Mb  1.29Mb
                                                                 <=                                                                     0b   2.14Kb  1.88Kb
ecs-prd-crm-vrs-0001-0001:28021                                  => 10.188.6.52                                                       138Kb   268Kb   238Kb
                                                                 <=                                                                  5.34Kb  7.13Kb  5.71Kb
ecs-prd-crm-vrs-0001-0001:57352                                  => 114.118.65.88                                                     212Kb   217Kb  87.3Kb
                                                                 <=                                                                  11.6Kb  13.2Kb  4.67Kb
ecs-prd-crm-vrs-0001-0001:57358                                  => 114.118.65.88                                                    63.0Kb   185Kb  54.4Kb
                                                                 <=                                                                  6.86Kb  11.2Kb  3.12Kb
ecs-prd-crm-vrs-0001-0001:60988                                  => 10.188.6.61                                                         0b    176Kb  44.1Kb
                                                                 <=                                                                     0b   3.74Kb   958b
ecs-prd-crm-vrs-0001-0001:26444                                  => 10.1.88.69                                                       83.2Kb  85.4Kb  85.3Kb
                                                                 <=                                                                  81.6Kb  83.7Kb  83.6Kb
ecs-prd-crm-vrs-0001-0001:26468                                  => 58.218.196.214                                                   82.6Kb  85.0Kb  84.7Kb
                                                                 <=                                                                  80.8Kb  83.6Kb  83.6Kb
ecs-prd-crm-vrs-0001-0001:26292                                  => 10.1.88.60                                                       82.4Kb  85.2Kb  85.0Kb
                                                                 <=                                                                  81.2Kb  83.4Kb  83.6Kb
ecs-prd-crm-vrs-0001-0001:26324                                  => 10.1.88.71                                                       83.2Kb  85.1Kb  84.9Kb
                                                                 <=                                                                  81.6Kb  83.5Kb  83.6Kb
ecs-prd-crm-vrs-0001-0001:26448                                  => 153.36.106.124                                                   82.4Kb  84.9Kb  84.9Kb
                                                                 <=                                                                  81.6Kb  83.7Kb  83.6Kb
ecs-prd-crm-vrs-0001-0001:26402                                  => 10.1.88.4                                                        82.4Kb  84.9Kb  84.9Kb
                                                                 <=                                                                  81.6Kb  83.5Kb  83.6Kb
ecs-prd-crm-vrs-0001-0001:26328                                  => 221.178.242.16                                                   83.2Kb  84.9Kb  84.8Kb
                                                                 <=                                                                  80.8Kb  83.5Kb  83.5Kb
ecs-prd-crm-vrs-0001-0001:26428                                  => 10.1.88.47                                                       82.0Kb  84.8Kb  84.8Kb
                                                                 <=                                                                  81.5Kb  83.5Kb  83.6Kb
ecs-prd-crm-vrs-0001-0001:26332                                  => 221.178.242.16                                                   82.0Kb  84.8Kb  84.8Kb
                                                                 <=                                                                  80.7Kb  83.5Kb  83.6Kb
ecs-prd-crm-vrs-0001-0001:26202                                  => 221.178.242.16                                                   82.8Kb  84.8Kb  84.8Kb
                                                                 <=                                                                  81.1Kb  83.5Kb  83.6Kb




10.188.6.233:36274                                               => 114.118.65.87:80                                                  618Kb   124Kb  30.9Kb
10.188.6.233:41134                                               => 114.118.65.88:80                                                  237Kb  47.4Kb  11.9Kb
10.188.6.233:53822                                               => 123.56.17.44:80                                                   220Kb  44.0Kb  11.0Kb
10.188.6.233:41128                                               => 114.118.65.88:80                                                  209Kb   203Kb  50.8Kb
10.188.6.233:60376                                               => 124.243.239.204:80                                                207Kb  59.0Kb  14.7Kb
10.188.6.233:53856                                               => 114.118.75.150:80                                                 204Kb  40.8Kb  10.2Kb
10.188.6.233:50354                                               => 39.105.54.181:80                                                  167Kb   207Kb  62.1Kb
10.188.6.233:53840                                               => 114.118.75.150:80                                                 147Kb  29.3Kb  7.33Kb
10.188.6.233:53862                                               => 114.118.75.150:80                                                 133Kb  26.6Kb  6.66Kb
10.188.6.233:53828                                               => 123.56.17.44:80                                                   107Kb  21.4Kb  5.34Kb
10.188.6.233:41136                                               => 114.118.65.88:80                                                  106Kb  21.3Kb  5.31Kb
10.188.6.233:58748                                               => 125.254.169.35:80                                                88.7Kb  54.5Kb  13.6Kb
10.188.6.233:26218                                               => 10.1.88.11:59977                                                 83.2Kb  86.4Kb  84.4Kb
10.188.6.233:26192                                               => 221.178.242.16:14671                                             82.6Kb  86.5Kb  65.4Kb
10.188.6.233:26336                                               => 10.1.88.6:56609                                                  82.4Kb  86.2Kb  62.3Kb
10.188.6.233:26200                                               => 10.1.88.211:54930                                                82.4Kb  86.2Kb  56.4Kb
10.188.6.233:26448                                               => 58.218.196.214:12465                                             82.4Kb  86.1Kb  44.6Kb
10.188.6.233:26294                                               => 10.1.88.20:63543                                                 82.2Kb  82.3Kb  20.7Kb
10.188.6.233:26428                                               => 10.1.88.37:52575                                                 82.0Kb  86.3Kb  84.5Kb
10.188.6.233:26398                                               => 58.218.196.215:29768                                             81.8Kb  86.2Kb  84.3Kb
10.188.6.233:26320                                               => 10.1.88.8:60614                                                  81.8Kb  30.0Kb  7.49Kb
10.188.6.233:26194                                               => 153.36.106.124:57567                                             81.4Kb  89.0Kb  22.2Kb
10.188.6.233:26414                                               => 10.1.88.46:54827                                                 81.1Kb  78.3Kb  19.7Kb
10.188.6.233:26372                                               => 221.181.213.18:18704                                             76.6Kb  79.7Kb  78.0Kb
10.188.6.233:26236                                               => 221.181.213.18:17872                                             76.6Kb  79.7Kb  57.0Kb
10.188.6.233:26264                                               => 221.181.213.17:25702                                             76.6Kb  74.5Kb  18.6Kb
10.188.6.233:26220                                               => 221.181.213.17:19080                                             75.8Kb  80.6Kb  40.1Kb
10.188.6.233:26188                                               => 221.181.213.17:10700                                             75.8Kb  79.7Kb  78.0Kb
10.188.6.233:26240                                               => 223.109.89.196:26306                                             75.8Kb  79.7Kb  78.0Kb
10.188.6.233:26386                                               => 223.109.89.196:26208                                             75.8Kb  79.7Kb  71.5Kb
10.188.6.233:26208                                               => 223.109.89.196:26386                                             75.8Kb  79.7Kb  65.4Kb
10.188.6.233:26232                                               => 221.181.213.17:22278                                             75.8Kb  79.7Kb  59.1Kb


8582
4376 createSession response 200
4206 destorySession response 200


knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000e4010@dx196b9e99b2cb830802","data":{"result":{"sn":1,"ls":false,"bg":0,"ed":0,"ws":[{"bg":25,"cw":[{"sc":0,"w":"到"}]},{"cw":[{"sc":0,"w":"现在"}],"bg":45},{"bg":77,"cw":[{"sc":0,"w":"嘛"}]},{"bg":89,"cw":[{"sc":0,"w":"我"}]},{"cw":[{"sc":0,"w":"都"}],"bg":101},{"bg":129,"cw":[{"w":"问","sc":0}]},{"bg":141,"cw":[{"w":"他","sc":0}]},{"bg":153,"cw":[{"sc":0,"w":"我"}]},{"bg":165,"cw":[{"sc":0,"w":"说"}]},{"bg":173,"cw":[{"sc":0,"w":"我"}]},{"bg":181,"cw":[{"sc":0,"w":"这"}]},{"bg":201,"cw":[{"sc":0,"w":"2058"}]},{"bg":257,"cw":[{"sc":0,"w":"G"}]},{"bg":281,"cw":[{"sc":0,"w":"要"}]},{"bg":297,"cw":[{"sc":0,"w":"保养"}]},{"bg":337,"cw":[{"sc":0,"w":"呢"}]}]},"status":0}}


knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000dbd77@dx196b9d60b38a140802","data":{"result":{"sn":1,"ls":false,"bg":0,"ed":0,"ws":[{"bg":25,"cw":[{"sc":0,"w":"嗯"}]}]},"status":0}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000dbd77@dx196b9d60b38a140802","data":{"result":{"ls":true,"bg":0,"ed":0,"ws":[{"bg":0,"cw":[{"sc":0,"w":""}]}],"sn":2},"status":2}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000dd4a3@dx196b9d6448cb95d802","data":{"result":{"ls":true,"bg":0,"ed":0,"ws":[{"bg":0,"cw":[{"sc":0,"w":""}]}],"sn":1},"status":2}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000d4cf9@dx196b9dc90e2a140802","data":{"result":{"sn":1,"ls":false,"bg":0,"ed":0,"ws":[{"bg":25,"cw":[{"w":"但","sc":0}]},{"bg":41,"cw":[{"sc":0,"w":"我"}]},{"bg":53,"cw":[{"sc":0,"w":"不"}]},{"bg":69,"cw":[{"sc":0,"w":"认识"}]},{"cw":[{"sc":0,"w":"他"}],"bg":97},{"bg":145,"cw":[{"sc":0,"w":"我"}]},{"bg":157,"cw":[{"w":"也","sc":0}]},{"bg":169,"cw":[{"sc":0,"w":"没"}]},{"bg":189,"cw":[{"w":"跟","sc":0}]},{"bg":197,"cw":[{"sc":0,"w":"他"}]},{"bg":213,"cw":[{"w":"签","sc":0}]},{"bg":245,"cw":[{"sc":0,"w":"这个"}]},{"bg":273,"cw":[{"sc":0,"w":"钱"}]},{"cw":[{"sc":0,"w":"这个"}],"bg":313},{"cw":[{"sc":0,"w":"钱"}],"bg":345},{"bg":377,"cw":[{"w":"钱","sc":0}]}]},"status":0}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000d4cf9@dx196b9dc90e2a140802","data":{"status":2,"result":{"sn":2,"ls":true,"bg":0,"ed":0,"ws":[{"cw":[{"w":"","sc":0}],"bg":0}]}}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000d6866@dx196b9dd5299a427802","data":{"status":0,"result":{"sn":1,"ls":false,"bg":0,"ed":0,"ws":[{"bg":33,"cw":[{"sc":0,"w":"我"}]},{"bg":65,"cw":[{"sc":0,"w":"我"}]},{"bg":77,"cw":[{"sc":0,"w":"有"}]},{"bg":97,"cw":[{"sc":0,"w":"证据"}]},{"bg":137,"cw":[{"w":"我","sc":0}]},{"bg":153,"cw":[{"sc":0,"w":"打"}]},{"bg":169,"cw":[{"sc":0,"w":"给"}]},{"bg":181,"cw":[{"sc":0,"w":"他"}]},{"bg":201,"cw":[{"sc":0,"w":"的"}]},{"bg":225,"cw":[{"sc":0,"w":"我"}]},{"bg":237,"cw":[{"w":"有","sc":0}]},{"bg":257,"cw":[{"sc":0,"w":"证据"}]}]}}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000d6866@dx196b9dd5299a427802","data":{"result":{"sn":2,"ls":true,"bg":0,"ed":0,"ws":[{"bg":0,"cw":[{"sc":0,"w":""}]}]},"status":2}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000df5a3@dx196b9dd8f83b9ec802","data":{"result":{"sn":1,"ls":false,"bg":0,"ed":0,"ws":[{"bg":9,"cw":[{"sc":0,"w":"对"}]},{"bg":33,"cw":[{"sc":0,"w":"我"}]},{"bg":57,"cw":[{"w":"我","sc":0}]},{"cw":[{"sc":0,"w":"打"}],"bg":81},{"bg":101,"cw":[{"sc":0,"w":"给"}]},{"cw":[{"sc":0,"w":"的"}],"bg":113},{"bg":125,"cw":[{"sc":0,"w":"就是"}]},{"bg":141,"cw":[{"sc":0,"w":"这个"}]},{"bg":157,"cw":[{"sc":0,"w":"销售"}]},{"cw":[{"sc":0,"w":"经理"}],"bg":189},{"bg":221,"cw":[{"sc":0,"w":"嘛"}]},{"bg":241,"cw":[{"sc":0,"w":"他"}]},{"bg":253,"cw":[{"sc":0,"w":"就是"}]},{"bg":289,"cw":[{"sc":0,"w":"是"}]},{"bg":305,"cw":[{"sc":0,"w":"徐"}]},{"bg":317,"cw":[{"sc":0,"w":"工"}]},{"bg":329,"cw":[{"sc":0,"w":"系"}]},{"bg":341,"cw":[{"sc":0,"w":"他们"}]},{"bg":365,"cw":[{"sc":0,"w":"销售"}]},{"cw":[{"sc":0,"w":"经理"}],"bg":393},{"bg":449,"cw":[{"sc":0,"w":"他"}]}]},"status":0}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000df5a3@dx196b9dd8f83b9ec802","data":{"status":2,"result":{"sn":2,"ls":true,"bg":0,"ed":0,"ws":[{"bg":0,"cw":[{"w":"","sc":0}]}]}}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000d714f@dx196b9de1139a4f0802","data":{"result":{"sn":1,"ls":false,"bg":0,"ed":0,"ws":[{"bg":25,"cw":[{"sc":0,"w":"打"}]},{"bg":37,"cw":[{"sc":0,"w":"电话"}]},{"cw":[{"sc":0,"w":"就"}],"bg":69},{"bg":85,"cw":[{"sc":0,"w":"这样"}]},{"cw":[{"sc":0,"w":"跟"}],"bg":113},{"bg":125,"cw":[{"sc":0,"w":"我"}]},{"bg":141,"cw":[{"sc":0,"w":"说"}]},{"bg":157,"cw":[{"sc":0,"w":"了"}]},{"bg":173,"cw":[{"sc":0,"w":"他"}]},{"bg":193,"cw":[{"sc":0,"w":"说是"}]},{"bg":257,"cw":[{"sc":0,"w":"你"}]},{"bg":297,"cw":[{"sc":0,"w":"如果"}]},{"bg":321,"cw":[{"sc":0,"w":"再"}]},{"bg":345,"cw":[{"w":"拨打","sc":0}]},{"bg":373,"cw":[{"sc":0,"w":"400"}]},{"bg":413,"cw":[{"sc":0,"w":"电话"}]},{"bg":441,"cw":[{"w":"那","sc":0}]},{"bg":457,"cw":[{"sc":0,"w":"我"}]},{"bg":477,"cw":[{"sc":0,"w":"就"}]},{"bg":497,"cw":[{"sc":0,"w":"不"}]},{"bg":513,"cw":[{"sc":0,"w":"让"}]},{"bg":525,"cw":[{"sc":0,"w":"你"}]},{"bg":545,"cw":[{"sc":0,"w":"好过"}]}]},"status":0}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000d714f@dx196b9de1139a4f0802","data":{"result":{"ed":0,"ws":[{"bg":0,"cw":[{"sc":0,"w":""}]}],"sn":2,"ls":true,"bg":0},"status":2}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000e6632@dx196b9e05de3a12b802","data":{"result":{"ls":true,"bg":0,"ed":0,"ws":[{"bg":17,"cw":[{"sc":0,"w":"对"}]},{"bg":29,"cw":[{"sc":0,"w":"对"}]},{"bg":45,"cw":[{"sc":0,"w":"对"}]},{"bg":0,"cw":[{"sc":0,"w":""}]}],"sn":1},"status":2}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000d5133@dx196b9e0a970a12c802","data":{"result":{"bg":0,"ed":0,"ws":[{"bg":25,"cw":[{"sc":0,"w":"嗯"}]}],"sn":1,"ls":false},"status":0}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000d5133@dx196b9e0a970a12c802","data":{"status":2,"result":{"bg":0,"ed":0,"ws":[{"bg":0,"cw":[{"sc":0,"w":""}]}],"sn":2,"ls":true}}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000d7215@dx196b9e12f06a182802","data":{"result":{"sn":1,"ls":true,"bg":0,"ed":0,"ws":[{"bg":0,"cw":[{"w":"","sc":0}]}]},"status":2}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000ddbd4@dx196b9e237e0a182802","data":{"result":{"sn":1,"ls":false,"bg":0,"ed":0,"ws":[{"bg":25,"cw":[{"sc":0,"w":"噢"}]},{"bg":65,"cw":[{"sc":0,"w":"对"}]},{"cw":[{"sc":0,"w":"是"}],"bg":105},{"bg":121,"cw":[{"w":"吧","sc":0}]}]},"status":0}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000ddbd4@dx196b9e237e0a182802","data":{"result":{"bg":0,"ed":0,"ws":[{"bg":0,"cw":[{"sc":0,"w":""}]}],"sn":2,"ls":true},"status":2}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000dcc3a@dx196b9e2dbffb95d802","data":{"result":{"sn":1,"ls":false,"bg":0,"ed":0,"ws":[{"bg":25,"cw":[{"sc":0,"w":"啊"}]},{"bg":49,"cw":[{"w":"工具箱","sc":0}]},{"bg":93,"cw":[{"sc":0,"w":"门"}]},{"bg":113,"cw":[{"sc":0,"w":"打"}]},{"bg":125,"cw":[{"sc":0,"w":"不"}]},{"bg":137,"cw":[{"sc":0,"w":"开"}]},{"bg":153,"cw":[{"sc":0,"w":"是"}]},{"cw":[{"sc":0,"w":"吧"}],"bg":169},{"bg":181,"cw":[{"sc":0,"w":"好"}]},{"bg":189,"cw":[{"w":"的","sc":0}]},{"bg":205,"cw":[{"sc":0,"w":"还有"}]},{"cw":[{"sc":0,"w":"其他"}],"bg":225},{"bg":253,"cw":[{"sc":0,"w":"问题"}]},{"bg":281,"cw":[{"sc":0,"w":"吗"}]},{"bg":297,"cw":[{"sc":0,"w":"先生"}]}]},"status":0}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000dcc3a@dx196b9e2dbffb95d802","data":{"result":{"sn":2,"ls":true,"bg":0,"ed":0,"ws":[{"bg":0,"cw":[{"sc":0,"w":""}]}]},"status":2}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000d5750@dx196b9e312c97024802","data":{"result":{"ws":[{"bg":17,"cw":[{"sc":0,"w":"对"}]},{"bg":0,"cw":[{"sc":0,"w":""}]}],"sn":1,"ls":true,"bg":0,"ed":0},"status":2}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000d8651@dx196b9e352fba4f0802","data":{"result":{"sn":1,"ls":false,"bg":0,"ed":0,"ws":[{"bg":33,"cw":[{"sc":0,"w":"咱们"}]},{"bg":65,"cw":[{"sc":0,"w":"这边"}]}]},"status":0}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000d8651@dx196b9e352fba4f0802","data":{"status":1,"result":{"sn":2,"ls":false,"bg":0,"ed":0,"ws":[{"cw":[{"sc":0,"w":"呃"}],"bg":33},{"bg":81,"cw":[{"sc":0,"w":"有"}]},{"bg":169,"cw":[{"sc":0,"w":"徐"}]},{"bg":193,"cw":[{"sc":0,"w":"工"}]}]}}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000d8651@dx196b9e352fba4f0802","data":{"result":{"ls":false,"bg":0,"ed":0,"ws":[{"bg":25,"cw":[{"sc":0,"w":"售后"}]},{"bg":81,"cw":[{"sc":0,"w":"吗"}]}],"sn":3},"status":1}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000d8651@dx196b9e352fba4f0802","data":{"result":{"ws":[{"bg":0,"cw":[{"sc":0,"w":""}]}],"sn":4,"ls":true,"bg":0,"ed":0},"status":2}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000eaae6@dx196b9e39abea12b802","data":{"result":{"sn":1,"ls":true,"bg":0,"ed":0,"ws":[{"bg":25,"cw":[{"w":"对","sc":0}]},{"bg":41,"cw":[{"sc":0,"w":"对"}]},{"bg":57,"cw":[{"sc":0,"w":"对"}]},{"bg":73,"cw":[{"sc":0,"w":"对"}]},{"bg":89,"cw":[{"sc":0,"w":"对"}]},{"bg":129,"cw":[{"sc":0,"w":"我"}]},{"bg":141,"cw":[{"sc":0,"w":"刚刚"}]},{"bg":185,"cw":[{"sc":0,"w":"忘记"}]},{"bg":225,"cw":[{"sc":0,"w":"说"}]},{"bg":237,"cw":[{"sc":0,"w":"了"}]},{"bg":257,"cw":[{"sc":0,"w":"就是说"}]},{"bg":349,"cw":[{"sc":0,"w":"就是"}]},{"bg":377,"cw":[{"sc":0,"w":"有"}]},{"bg":389,"cw":[{"sc":0,"w":"服务"}]},{"bg":413,"cw":[{"w":"人员","sc":0}]},{"cw":[{"sc":0,"w":"能不能"}],"bg":445},{"bg":477,"cw":[{"sc":0,"w":"就是"}]},{"bg":505,"cw":[{"sc":0,"w":"跟"}]},{"bg":529,"cw":[{"sc":0,"w":"我"}]},{"cw":[{"sc":0,"w":"联系"}],"bg":553},{"bg":573,"cw":[{"sc":0,"w":"一下"}]},{"bg":601,"cw":[{"w":"然后","sc":0}]},{"bg":641,"cw":[{"sc":0,"w":"我"}]},{"bg":0,"cw":[{"sc":0,"w":""}]}]},"status":2}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000ec93a@dx196b9e3e8aea12b802","data":{"status":2,"result":{"bg":0,"ed":0,"ws":[{"bg":5,"cw":[{"w":"那个","sc":0}]},{"cw":[{"sc":0,"w":"乌鲁木齐"}],"bg":33},{"bg":93,"cw":[{"sc":0,"w":"是不是"}]},{"bg":117,"cw":[{"sc":0,"w":"有"}]},{"bg":133,"cw":[{"w":"一个","sc":0}]},{"bg":153,"cw":[{"sc":0,"w":"总站"}]},{"bg":201,"cw":[{"sc":0,"w":"呢"}]},{"bg":0,"cw":[{"sc":0,"w":""}]}],"sn":1,"ls":true}}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000ed49d@dx196b9e405a9a12b802","data":{"result":{"sn":1,"ls":false,"bg":0,"ed":0,"ws":[{"bg":17,"cw":[{"sc":0,"w":"嗯"}]},{"bg":65,"cw":[{"sc":0,"w":"啊"}]},{"bg":85,"cw":[{"sc":0,"w":"好"}]},{"bg":113,"cw":[{"sc":0,"w":"的"}]},{"bg":141,"cw":[{"sc":0,"w":"那"}]},{"bg":161,"cw":[{"sc":0,"w":"祝"}]},{"bg":173,"cw":[{"sc":0,"w":"您"}]},{"bg":193,"cw":[{"w":"快乐","sc":0}]},{"bg":229,"cw":[{"sc":0,"w":"健康"}]}]},"status":0}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000ed49d@dx196b9e405a9a12b802","data":{"status":2,"result":{"ed":0,"ws":[{"bg":0,"cw":[{"sc":0,"w":""}]}],"sn":2,"ls":true,"bg":0}}}


knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000e4010@dx196b9e99b2cb830802","data":{"result":{"sn":1,"ls":false,"bg":0,"ed":0,"ws":[{"bg":25,"cw":[{"sc":0,"w":"到"}]},{"cw":[{"sc":0,"w":"现在"}],"bg":45},{"bg":77,"cw":[{"sc":0,"w":"嘛"}]},{"bg":89,"cw":[{"sc":0,"w":"我"}]},{"cw":[{"sc":0,"w":"都"}],"bg":101},{"bg":129,"cw":[{"w":"问","sc":0}]},{"bg":141,"cw":[{"w":"他","sc":0}]},{"bg":153,"cw":[{"sc":0,"w":"我"}]},{"bg":165,"cw":[{"sc":0,"w":"说"}]},{"bg":173,"cw":[{"sc":0,"w":"我"}]},{"bg":181,"cw":[{"sc":0,"w":"这"}]},{"bg":201,"cw":[{"sc":0,"w":"2058"}]},{"bg":257,"cw":[{"sc":0,"w":"G"}]},{"bg":281,"cw":[{"sc":0,"w":"要"}]},{"bg":297,"cw":[{"sc":0,"w":"保养"}]},{"bg":337,"cw":[{"sc":0,"w":"呢"}]}]},"status":0}}


knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000e4010@dx196b9e99b2cb830802","data":{"result":{"sn":2,"ls":false,"bg":0,"ed":0,"ws":[{"bg":25,"cw":[{"sc":0,"w":"液压油"}]},{"bg":73,"cw":[{"sc":0,"w":"需要"}]},{"cw":[{"w":"更换","sc":0}],"bg":101},{"bg":161,"cw":[{"sc":0,"w":"我"}]},{"bg":173,"cw":[{"sc":0,"w":"说"}]},{"bg":189,"cw":[{"sc":0,"w":"你"}]},{"bg":197,"cw":[{"w":"把","sc":0}]},{"bg":217,"cw":[{"sc":0,"w":"油"}]},{"bg":233,"cw":[{"sc":0,"w":"拿"}]},{"bg":245,"cw":[{"sc":0,"w":"过来"}]},{"bg":269,"cw":[{"sc":0,"w":"给"}]},{"bg":281,"cw":[{"sc":0,"w":"我"}]},{"bg":297,"cw":[{"sc":0,"w":"更换"}]},{"bg":325,"cw":[{"w":"掉","sc":0}]}]},"status":1}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000e4010@dx196b9e99b2cb830802","data":{"result":{"bg":0,"ed":0,"ws":[{"bg":25,"cw":[{"sc":0,"w":"大概"}]},{"bg":77,"cw":[{"sc":0,"w":"大约"}]},{"bg":121,"cw":[{"sc":0,"w":"有"}]},{"bg":153,"cw":[{"sc":0,"w":"4"}]},{"bg":169,"cw":[{"sc":0,"w":"个"}]},{"bg":185,"cw":[{"w":"月","sc":0}]},{"bg":201,"cw":[{"sc":0,"w":"了"}]},{"cw":[{"sc":0,"w":"一直"}],"bg":225},{"bg":253,"cw":[{"sc":0,"w":"在"}]},{"bg":273,"cw":[{"sc":0,"w":"推"}]},{"bg":301,"cw":[{"sc":0,"w":"他"}]},{"bg":309,"cw":[{"sc":0,"w":"说"}]},{"cw":[{"sc":0,"w":"去年"}],"bg":321},{"bg":349,"cw":[{"sc":0,"w":"年底"}]},{"bg":385,"cw":[{"w":"年底","sc":0}]},{"bg":413,"cw":[{"sc":0,"w":"嘛"}]},{"bg":433,"cw":[{"sc":0,"w":"他"}]},{"bg":465,"cw":[{"sc":0,"w":"说"}]},{"cw":[{"sc":0,"w":"唉呀"}],"bg":501},{"bg":537,"cw":[{"sc":0,"w":"我"}]},{"bg":561,"cw":[{"sc":0,"w":"回家"}]},{"bg":593,"cw":[{"sc":0,"w":"老家"}]},{"bg":621,"cw":[{"w":"有","sc":0}]},{"bg":641,"cw":[{"sc":0,"w":"事情"}]},{"bg":677,"cw":[{"w":"有","sc":0}]},{"cw":[{"sc":0,"w":"各种"}],"bg":685},{"bg":721,"cw":[{"sc":0,"w":"理由"}]}],"sn":3,"ls":false},"status":1}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000e4010@dx196b9e99b2cb830802","data":{"result":{"ls":false,"bg":0,"ed":0,"ws":[{"bg":21,"cw":[{"sc":0,"w":"然后"}]},{"bg":45,"cw":[{"sc":0,"w":"呢"}]},{"bg":53,"cw":[{"sc":0,"w":"我们"}]},{"bg":77,"cw":[{"sc":0,"w":"就"}]},{"bg":85,"cw":[{"sc":0,"w":"相信"}]},{"bg":109,"cw":[{"sc":0,"w":"他"}]},{"bg":117,"cw":[{"w":"了","sc":0}]},{"bg":129,"cw":[{"sc":0,"w":"吧"}]},{"bg":141,"cw":[{"sc":0,"w":"因为"}]},{"bg":157,"cw":[{"sc":0,"w":"他们"}]}],"sn":4},"status":1}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000e4010@dx196b9e99b2cb830802","data":{"result":{"ws":[{"bg":9,"cw":[{"sc":0,"w":"我们"}]},{"bg":41,"cw":[{"sc":0,"w":"挖"}]},{"bg":57,"cw":[{"sc":0,"w":"机"}]},{"bg":69,"cw":[{"sc":0,"w":"不是"}]},{"bg":93,"cw":[{"sc":0,"w":"很多"}]},{"bg":121,"cw":[{"w":"吗","sc":0}]},{"bg":137,"cw":[{"sc":0,"w":"都是"}]},{"bg":161,"cw":[{"sc":0,"w":"他"}]},{"bg":201,"cw":[{"sc":0,"w":"过来"}]},{"bg":221,"cw":[{"sc":0,"w":"给"}]},{"bg":229,"cw":[{"sc":0,"w":"我们"}]},{"bg":253,"cw":[{"sc":0,"w":"包养"}]},{"bg":277,"cw":[{"sc":0,"w":"的"}]},{"bg":297,"cw":[{"sc":0,"w":"吗"}]}],"sn":5,"ls":false,"bg":0,"ed":0},"status":1}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000e4010@dx196b9e99b2cb830802","data":{"result":{"sn":6,"ls":true,"bg":0,"ed":0,"ws":[{"cw":[{"sc":0,"w":""}],"bg":0}]},"status":2}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000d4bc1@dx196b9ea77407024802","data":{"result":{"sn":1,"ls":true,"bg":0,"ed":0,"ws":[{"bg":17,"cw":[{"sc":0,"w":"姓"}]},{"cw":[{"sc":0,"w":"孔"}],"bg":41},{"bg":65,"cw":[{"sc":0,"w":"孔子"}]},{"bg":101,"cw":[{"sc":0,"w":"的"}]},{"bg":113,"cw":[{"sc":0,"w":"孔"}]},{"bg":0,"cw":[{"sc":0,"w":""}]}]},"status":2}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000d9f44@dx196b9ebfdafb9ec802","data":{"result":{"ws":[{"bg":33,"cw":[{"sc":0,"w":"是"}]},{"cw":[{"sc":0,"w":"xug"}],"bg":73},{"bg":161,"cw":[{"sc":0,"w":"043"}]},{"bg":225,"cw":[{"sc":0,"w":"后面"}]},{"cw":[{"sc":0,"w":"是"}],"bg":257},{"bg":269,"cw":[{"sc":0,"w":"什么"}]}],"sn":1,"ls":false,"bg":0,"ed":0},"status":0}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000d9f44@dx196b9ebfdafb9ec802","data":{"result":{"sn":2,"ls":true,"bg":0,"ed":0,"ws":[{"bg":0,"cw":[{"sc":0,"w":""}]}]},"status":2}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000d7878@dx196b9ec4038a11f802","data":{"result":{"sn":1,"ls":false,"bg":0,"ed":0,"ws":[{"bg":33,"cw":[{"sc":0,"w":"好"}]},{"bg":65,"cw":[{"sc":0,"w":"是"}]},{"bg":81,"cw":[{"sc":0,"w":"报备"}]},{"bg":113,"cw":[{"sc":0,"w":"这"}]},{"bg":129,"cw":[{"sc":0,"w":"台"}]},{"bg":153,"cw":[{"sc":0,"w":"车"}]},{"bg":169,"cw":[{"sc":0,"w":"吗"}]}]},"status":0}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000d7878@dx196b9ec4038a11f802","data":{"result":{"sn":2,"ls":true,"bg":0,"ed":0,"ws":[{"bg":0,"cw":[{"sc":0,"w":""}]}]},"status":2}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000d7418@dx196b9ec7efea427802","data":{"result":{"sn":1,"ls":false,"bg":0,"ed":0,"ws":[{"bg":33,"cw":[{"sc":0,"w":"呃"}]},{"bg":137,"cw":[{"sc":0,"w":"我"}]},{"bg":149,"cw":[{"sc":0,"w":"有"}]},{"bg":161,"cw":[{"w":"个","sc":0}]},{"cw":[{"sc":0,"w":"车"}],"bg":173},{"bg":193,"cw":[{"sc":0,"w":"油管"}]},{"bg":225,"cw":[{"w":"爆","sc":0}]},{"bg":245,"cw":[{"sc":0,"w":"了"}]}]},"status":0}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000d7418@dx196b9ec7efea427802","data":{"status":1,"result":{"bg":0,"ed":0,"ws":[{"bg":21,"cw":[{"sc":0,"w":"明天"}]},{"bg":53,"cw":[{"sc":0,"w":"给"}]},{"bg":69,"cw":[{"sc":0,"w":"我"}]},{"bg":85,"cw":[{"w":"搞","sc":0}]},{"bg":101,"cw":[{"w":"一下","sc":0}]},{"bg":121,"cw":[{"sc":0,"w":"呗"}]}],"sn":2,"ls":false}}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000d7418@dx196b9ec7efea427802","data":{"result":{"ls":true,"bg":0,"ed":0,"ws":[{"bg":0,"cw":[{"sc":0,"w":""}]}],"sn":3},"status":2}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000df23b@dx196b9eccf00b9ec802","data":{"result":{"ed":0,"ws":[{"bg":25,"cw":[{"sc":0,"w":"啊"}]},{"bg":69,"cw":[{"w":"唉","sc":0}]},{"bg":0,"cw":[{"sc":0,"w":""}]}],"sn":1,"ls":true,"bg":0},"status":2}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000db50c@dx196b9ed1fdda427802","data":{"status":0,"result":{"sn":1,"ls":false,"bg":0,"ed":0,"ws":[{"bg":25,"cw":[{"sc":0,"w":"嗯"}]}]}}}
knodi_asr_proxy  | [kd-mrcp-asr] on_message called with hdl = 0x7f22980008d0 and message = {"code":0,"message":"success","sid":"iat000db50c@dx196b9ed1fdda427802","data":{"result":{"sn":2,"ls":true,"bg":0,"ed":0,"ws":[{"bg":0,"cw":[{"w":"","sc":0}]}]},"status":2}}




20250521
排查徐工PRD环境fs调用asr交互流程
排查徐工PRD环境fs调用tts交互流程
排查徐工PRD环境asr语音流转发过程
定位fs->mrcp->asr各个流程未发现异常问题，讯飞返回识别结果少部分句子


2025-04-24 22:40:38.704254 100.00% [INFO] switch_core.c:2503
FreeSWITCH Version 1.10.11-release~64bit ( 64bit)

FreeSWITCH Started
Max Sessions [1000]
Session Rate [30]
SQL [Enabled]
2025-04-24 22:40:38.704258 100.00% [CONSOLE] switch_core.c:2511
[This app Best viewed at 160x60 or more..]
2025-04-24 22:40:38.704647 100.00% [WARNING] switch_console.c:1056 We've become an orphan, no more console for us.
2025-04-24 22:40:38.704683 100.00% [DEBUG] switch_console.c:1088 Editline thread exiting
45980ece-7528-4739-84a0-e4950cc6a600 2025-04-24 22:40:39.635721 100.00% [NOTICE] switch_channel.c:1142 New Channel sofia/external/15069488567@223.109.89.196 [45980ece-7528-4739-84a0-e4950cc6a600]


lenovo_vad:
[2025-05-20 09:51:59.864][thread 25][,][info] : Init recoProxy
[2025-05-20 09:52:00.662][thread 224][,][info] : Index:0 T: 800 -> detected begin of speech. ret: 1
[2025-05-20 09:52:00.662][thread 224][,][info] : Reset elspased time 800
[2025-05-20 09:52:00.716][thread 224][,][info] : var->_iPos:12800 iTotal:8000 iBeginPos:4800   iBeginTime:300 pOptions->_iSampleRatio:8000
[2025-05-20 09:52:01.322][thread 224][,][info] : Index:1 T: 1460 -> detected end of speech. ret: 2
[2025-05-20 09:52:01.322][thread 224][,][info] : [kd-mrcp-asr] Session Id = ea676f52-9257-404d-8efb-fbd622a2b8ba, VAD END
[2025-05-20 09:52:01.322][thread 224][,][info] : [kd-mrcp-asr][vad end] sessionId = ea676f52-9257-404d-8efb-fbd622a2b8ba, traceId = f32e7d4e-eb9c-4140-9d07-b5ee2686f569
[2025-05-20 09:52:01.336][thread 225][,][info] : Get res ifly
[2025-05-20 09:52:04.092][thread 224][,][info] : Index:1 T: 4230 -> detected begin of speech. ret: 1
[2025-05-20 09:52:04.092][thread 224][,][info] : Reset elspased time 4230
[2025-05-20 09:52:07.372][thread 224][,][info] : var->_iPos:67680 iTotal:8000 iBeginPos:59680   iBeginTime:3730 pOptions->_iSampleRatio:8000
[2025-05-20 09:52:07.397][thread 224][,][info] : Index:2 T: 6920 -> detected end of speech. ret: 2
[2025-05-20 09:52:07.397][thread 224][,][info] : [kd-mrcp-asr] Session Id = ea676f52-9257-404d-8efb-fbd622a2b8ba, VAD END
[2025-05-20 09:52:07.397][thread 224][,][info] : [kd-mrcp-asr][vad end] sessionId = ea676f52-9257-404d-8efb-fbd622a2b8ba, traceId = 16307431-99e9-4193-b5df-133d5f510397
[2025-05-20 09:52:07.527][thread 227][,][info] : Get res ifly ~O湾~\~S~A~Y~\~I没~\~I~W~I~K~W-4bc7-494d-b088-
[2025-05-20 09:52:07.531][thread 227][,][info] : Get res ifly
[2025-05-20 09:52:14.342][thread 224][,][info] : Index:2 T: 14430 -> detected begin of speech. ret: 1
[2025-05-20 09:52:14.342][thread 224][,][info] : Reset elspased time 14430
[2025-05-20 09:52:14.375][thread 224][,][info] : var->_iPos:230880 iTotal:8000 iBeginPos:222880   iBeginTime:13930 pOptions->_iSampleRatio:8000
[2025-05-20 09:52:16.292][thread 224][,][info] : Index:3 T: 16380 -> detected end of speech. ret: 2
[2025-05-20 09:52:16.292][thread 224][,][info] : [kd-mrcp-asr] Session Id = ea676f52-9257-404d-8efb-fbd622a2b8ba, VAD END
[2025-05-20 09:52:16.292][thread 224][,][info] : [kd-mrcp-asr][vad end] sessionId = ea676f52-9257-404d-8efb-fbd622a2b8ba, traceId = 5a216380-7821-41c2-ba29-5a1c34ab6396
[2025-05-20 09:52:16.306][thread 231][,][info] : Get res ifly ~Y~X~\~_~Z~D~F~M~]~@次~F~M~]~@次ret: 1
[2025-05-20 09:52:16.307][thread 231][,][info] : Get res ifly


webrtc_vad:
[2025-05-16 12:51:25.726][thread 25][,][info] : [kd-spdlog][tts] init success
[2025-05-16 12:51:25.726][thread 25][,][info] : Init recoProxy
[2025-05-16 12:51:25.731][thread 30][,][info] : Feed data 0x7fac74003b88, Len is 160
[2025-05-16 12:51:25.731][thread 60][,][info] : Get Data 0x7fac70002d20, Len=160



20250520
研究学习线上运维系统，下载fs、mrcp、kd-asr-proxy服务相关日志
分析徐工PRD环境fs日志
分析徐工PRD环境mrcp日志
分析徐工PRD环境kd-asr-proxy日志




{service_name="fs-ai"} |= `15161339666`

99680879-d396-4fb5-8186-dccef4f91ce9

2025-04-07 21:24:43.071367 98.70% [NOTICE] switch_channel.c:1142 New Channel sofia/external/+8615161339666@223.109.89.196 [99680879-d396-4fb5-8186-dccef4f91ce9]
2025-04-07 21:31:55.291393 99.00% [NOTICE] switch_core_session.c:1766 Close Channel sofia/external/+8615161339666@223.109.89.196 [CS_DESTROY]




搜索 "switch_channel.c:1142 New Channel sofia/external/+8615161339666@" （1个文件中匹配到5次，总计查找1次） [普通: 大小写]
  C:\Users\lit\Downloads\15161339666.txt （匹配5次）
	行    6: 1744032198449	2025-04-07 21:23:17.571364 99.17% [NOTICE] switch_channel.c:1142 New Channel sofia/external/+8615161339666@nowhere [0d4257c0-a2b2-48ca-a693-35180f225e47]
	行  109: 1744032216690	2025-04-07 21:23:36.671365 98.90% [NOTICE] switch_channel.c:1142 New Channel sofia/external/+8615161339666@223.109.89.196 [a4d506c8-f871-496b-8ec5-84e9b8cd6161]
	行 1617: 1744032267878	2025-04-07 21:24:20.711367 98.33% [NOTICE] switch_channel.c:1142 New Channel sofia/external/+8615161339666@nowhere [695c181d-78c6-4c6c-8540-de1151766b66]
	行 1665: 1744032283079	2025-04-07 21:24:43.071367 98.70% [NOTICE] switch_channel.c:1142 New Channel sofia/external/+8615161339666@223.109.89.196 [99680879-d396-4fb5-8186-dccef4f91ce9]
	行 2943: 1744032340657	2025-04-07 21:25:38.391370 98.20% [NOTICE] switch_channel.c:1142 New Channel sofia/external/+8615161339666@223.109.89.196 [7f52361b-9d51-432b-93ff-94ea585a5901]



	行 2176: 1744032314747	2025-04-07 21:25:05.951365 98.47% [INFO] mod_commands.c:4693 call process_close, ip:10.188.6.233 port:30098 sockfd:96
	行 2179: 1744032314747	2025-04-07 21:25:05.951365 98.47% [INFO] mod_commands.c:4693 call process_close, ip:10.188.6.233 port:30100 sockfd:122
	行 2306: 1744032318550	2025-04-07 21:25:18.491367 98.63% [INFO] mod_commands.c:4896 uuid::7fda866a-9202-4d89-a5e0-189189d85aec actual_sample_rate:8000
	行 2326: 1744032318550	2025-04-07 21:25:18.491367 98.63% [INFO] mod_commands.c:4896 uuid::ed7a8d9d-7213-461e-8be4-47d2127283de actual_sample_rate:8000
	行 2663: 1744032331801	2025-04-07 21:25:30.531365 98.70% [INFO] mod_commands.c:4693 call process_close, ip:10.188.6.233 port:30004 sockfd:123
	行 2666: 1744032331801	2025-04-07 21:25:30.551363 98.70% [INFO] mod_commands.c:4693 call process_close, ip:10.188.6.233 port:30006 sockfd:138
	行 2962: 1744032342202	2025-04-07 21:25:40.671365 98.20% [INFO] mod_commands.c:4896 uuid::714f1294-e1e6-4b02-8ffc-6d6724e40b63 actual_sample_rate:8000
	行 2964: 1744032342202	2025-04-07 21:25:40.691366 98.20% [INFO] mod_commands.c:4896 uuid::0063b2a7-2fab-407e-ae74-86cfa290ab6b actual_sample_rate:8000
	行 3863: 1744032419014	2025-04-07 21:26:54.551364 99.00% [INFO] mod_commands.c:4693 call process_close, ip:10.188.6.233 port:30008 sockfd:160
	行 3866: 1744032419014	2025-04-07 21:26:54.551364 99.00% [INFO] mod_commands.c:4693 call process_close, ip:10.188.6.233 port:30010 sockfd:174
	行 4083: 1744032515080	2025-04-07 21:27:29.451366 99.20% [INFO] mod_commands.c:4896 uuid::a7271e5f-db7e-41b5-a5e2-203e1b64d079 actual_sample_rate:8000
	行 4084: 1744032515080	2025-04-07 21:27:29.451366 99.20% [INFO] mod_commands.c:4896 uuid::48728339-adf4-451d-9592-235ebd88ae28 actual_sample_rate:8000
	行 4691: 1744032537634	2025-04-07 21:28:56.091363 98.87% [INFO] mod_commands.c:4693 call process_close, ip:10.188.6.233 port:30016 sockfd:109
	行 4749: 1744032541074	2025-04-07 21:28:58.011363 98.83% [INFO] mod_commands.c:4693 call process_close, ip:10.188.6.233 port:30018 sockfd:162
	行 5273: 1744032591956	2025-04-07 21:29:51.671365 99.10% [INFO] mod_commands.c:4693 call process_close, ip:10.188.6.233 port:30012 sockfd:136
	行 5300: 1744032592273	2025-04-07 21:29:51.971367 99.10% [INFO] mod_commands.c:4693 call process_close, ip:10.188.6.233 port:30014 sockfd:137
	行 5312: 1744032592273	2025-04-07 21:29:52.131375 99.10% [INFO] mod_commands.c:4896 uuid::d24c6a42-8148-4241-80a5-4848f58be85e actual_sample_rate:8000
	行 5313: 1744032592273	2025-04-07 21:29:52.131375 99.10% [INFO] mod_commands.c:4896 uuid::7f52361b-9d51-432b-93ff-94ea585a5901 actual_sample_rate:8000
	行 5358: 1744032659532	2025-04-07 21:29:55.331365 98.90% [INFO] mod_commands.c:4896 uuid::f65e8828-725d-439b-a39c-233d004071e5 actual_sample_rate:8000
	行 5359: 1744032659532	2025-04-07 21:29:55.331365 98.90% [INFO] mod_commands.c:4896 uuid::3d53690f-448e-479b-86ed-22ff1da86d5c actual_sample_rate:8000
	行 5376: 1744032659533	2025-04-07 21:30:30.051365 98.37% [INFO] mod_commands.c:4693 call process_close, ip:10.188.6.233 port:30024 sockfd:100
	行 5379: 1744032659533	2025-04-07 21:30:30.051365 98.37% [INFO] mod_commands.c:4693 call process_close, ip:10.188.6.233 port:30026 sockfd:127
	行 5654: 1744032678391	2025-04-07 21:31:16.531363 99.33% [INFO] mod_commands.c:4896 uuid::4553393c-251e-4e2e-b075-38b632efc8a3 actual_sample_rate:8000
	行 5655: 1744032678391	2025-04-07 21:31:16.531363 99.33% [INFO] mod_commands.c:4896 uuid::e30e82f3-e0a9-4641-ae03-1df64571774c actual_sample_rate:8000
	行 5899: 1744032699551	2025-04-07 21:31:38.871366 98.93% [INFO] mod_commands.c:4693 call process_close, ip:10.188.6.233 port:30028 sockfd:149
	行 5902: 1744032699551	2025-04-07 21:31:38.871366 98.93% [INFO] mod_commands.c:4693 call process_close, ip:10.188.6.233 port:30030 sockfd:66
	行 6052: 1744032724471	2025-04-07 21:31:55.291393 99.00% [INFO] mod_commands.c:4693 call process_close, ip:10.188.6.233 port:30020 sockfd:55
	行 6055: 1744032724471	2025-04-07 21:31:55.291393 99.00% [INFO] mod_commands.c:4693 call process_close, ip:10.188.6.233 port:30022 sockfd:120

apt_log(RECOG_LOG_MARK, APT_PRIO_INFO, "[kd-mrcp-asr] session[%s] choose render[%s][%d] language[%s] accent[%s]",
                                        sessionId, asrRender, asrOption._iAsrRenderId, asrLanguage, accent);

printf("[kd-mrcp-asr] recoProxy::recoProxy >>>>>> RECO_ASR_IFLYTEK SampleRatio = %d \n", _pVadOptions._iSampleRatio);


printf("get request parameter = %s\n", ret.c_str());







echo "core.%e.%p" > /proc/sys/kernel/core_pattern

[kd-mrcp-tts] iflytekTtsInst::speak >>>>>> in
Get file /tmp/9B3AFEEBD1DE923D71211CB07A0E4726
[kd-mrcp-tts] iflytekTtsInst::speak >>>>>> Using Cache tts = 请说出您要咨询的问题
[kd-mrcp-tts] ttsProxyMsg::recordTime _pAsrTime : null
[kd-mrcp-tts] ttsProxyMsg::recordTime Invalid argument: stod
[kd-mrcp-tts][tts end] sessionId = f366dcb9-feaf-4e69-a217-a5066cf8f07a, traceId = 959673b8-679a-451c-868e-f78d173d647a, tts_duration = 0.277984, asr_tts_duration = 0
2025-05-16 10:53:42:974712 [INFO]   [kd-mrcp-tts][tts cb close] sessionId = f366dcb9-feaf-4e69-a217-a5066cf8f07a, traceId = 959673b8-679a-451c-868e-f78d173d647a
[kd-mrcp-tts] iflytekTtsInst::speak >>>>>> out





mfeSetParam(_pVadObj, PARAM_VOICE_POINT, 80);
RECOPROXY_VAD_ENERGY_START=60
RECOPROXY_VAD_PAUSE=60
echo "RECOPROXY_VAD_ENERGY_START="${RECOPROXY_VAD_ENERGY_START}
echo "RECOPROXY_VAD_PAUSE="${RECOPROXY_VAD_PAUSE}

unimrcp5  | [kd-mrcp-asr] lenovoVadInst::init vad iVadEnergyStart = 60
unimrcp5  | [kd-mrcp-asr] lenovoVadInst::init iVadEnergeStop = 30
unimrcp5  | [kd-mrcp-asr] lenovoVadInst::init iVoicePoint = 100
unimrcp5  | [kd-mrcp-asr] lenovoVadInst::init iLRelax = 25
unimrcp5  | [kd-mrcp-asr] lenovoVadInst::init iRRelax = 30
unimrcp5  | [kd-mrcp-asr] lenovoVadInst::init iMinSpDuration = 15
unimrcp5  | [kd-mrcp-asr] lenovoVadInst::init iMaxSpDuration = 100000
unimrcp5  | [kd-mrcp-asr] lenovoVadInst::init iSleepTimeout = 6000
unimrcp5  | [kd-mrcp-asr] lenovoVadInst::init iMaxSpPause = 600 ms, iLRelax = 250 ms
unimrcp5  | [kd-mrcp-asr] recoProxy::recoProxy >>>>>> out
unimrcp5  | [kd-mrcp-asr] recoProxySetVadIntParam type = 0, value = 1

fs-ai:
EXECUTE
detect_speech




unimrcp5  | [kd-mrcp-asr] createVadCbUtil
unimrcp5  | [kd-mrcp-asr] recoProxyCreateVad >>>>>> RECO_VAD_LENOVO
unimrcp5  | [kd-mrcp-asr] recoProxyInitVad
unimrcp5  | [kd-mrcp-asr] lenovoVadInst::init vad iVadEnergyStart = 85
unimrcp5  | [kd-mrcp-asr] lenovoVadInst::init iVadEnergeStop = 30
unimrcp5  | [kd-mrcp-asr] lenovoVadInst::init iVoicePoint = 100
unimrcp5  | [kd-mrcp-asr] lenovoVadInst::init iLRelax = 25
unimrcp5  | [kd-mrcp-asr] lenovoVadInst::init iRRelax = 30
unimrcp5  | [kd-mrcp-asr] lenovoVadInst::init iMinSpDuration = 15
unimrcp5  | [kd-mrcp-asr] lenovoVadInst::init iMaxSpDuration = 100000
unimrcp5  | [kd-mrcp-asr] lenovoVadInst::init iSleepTimeout = 6000
unimrcp5  | [kd-mrcp-asr] lenovoVadInst::init iMaxSpPause = 750 ms, iLRelax = 250 ms
unimrcp5  | [kd-mrcp-asr] recoProxySetVadIntParam type = 0, value = 1
unimrcp5  | [kd-mrcp-asr] recoProxySetVadIntParam type = 1, value = 10000



fs-ai  | 2025-05-19 15:48:16,344 INFO /tmp/servicePool_test_appId/manual/2025-05-19/d9edc431-0f4f-4641-8779-a7769cf14066.wav
fs-ai  | 2025-05-19 15:48:16,348 INFO 172.26.0.11 - - [19/May/2025 15:48:16] "POST /audio HTTP/1.1" 200 -
fs-ai  | 2025-05-19 15:48:16,364 INFO /tmp/servicePool_test_appId/robot/2025-05-19/f7530f6e-9d48-444f-9507-1b03fd7e7ce3.wav
fs-ai  | 2025-05-19 15:48:16,366 INFO 172.26.0.9 - - [19/May/2025 15:48:16] "POST /audio HTTP/1.1" 200





fs-ai  | 2025-05-19 15:50:30.462344 97.73% [NOTICE] switch_channel.c:1142 New Channel sofia/external/1001@192.168.109.85:15080 [ec682b32-5a44-4a96-83ad-977c0efd20f9]
fs-ai  | 2025-05-19 15:50:30.462344 97.73% [INFO] sofia.c:10459 sofia/external/1001@192.168.109.85:15080 receiving invite from 172.70.100.1:2123 version: 1.10.11-release  64bit call-id: YWQ0OWJmMjhhNTliN2U2MThjMWMwZTVmOGUxNmI3MGU.
fs-ai  | 2025-05-19 15:50:30.462344 97.73% [INFO] mod_dialplan_xml.c:639 Processing 1001 <1001>->7000 in context public
fs-ai  | EXECUTE [depth=0] sofia/external/1001@192.168.109.85:15080 lua(gangtie_ivr.lua)
fs-ai  | 2025-05-19 15:50:30.482342 97.73% [NOTICE] sofia_media.c:90 Pre-Answer sofia/external/1001@192.168.109.85:15080!
fs-ai  | 2025-05-19 15:50:30.482342 97.73% [NOTICE] switch_cpp.cpp:704 Channel [sofia/external/1001@192.168.109.85:15080] has been answered
fs-ai  | 2025-05-19 15:50:30.762342 97.73% [INFO] switch_rtp.c:7655 Auto Changing audio port from 192.168.40.93:21572 to 172.70.100.1:2089
fs-ai  | 2025-05-19 15:50:39.062339 97.63% [INFO] switch_channel.c:528 RECV DTMF 1:640
fs-ai  | 2025-05-19 15:50:39.062339 97.63% [INFO] switch_cpp.cpp:1466 -----callerNumber=1001-----digit=1
fs-ai  | 2025-05-19 15:50:39.062339 97.63% [INFO] switch_cpp.cpp:1466 -------uuid=ec682b32-5a44-4a96-83ad-977c0efd20f9-------digit=1
fs-ai  | 2025-05-19 15:50:39.062339 97.63% [NOTICE] switch_channel.c:1142 New Channel sofia/external/50000001@0.0.0.0:15080 [cb5075f2-4e5c-43b3-bcdf-d3b4ac5b4709]
fs-ai  | 2025-05-19 15:50:39.062339 97.63% [INFO] sofia_glue.c:1659 sofia/external/50000001@0.0.0.0:15080 sending invite call-id: (null)
fs-ai  | 2025-05-19 15:50:39.062339 97.63% [NOTICE] switch_channel.c:1142 New Channel sofia/external/1001@192.168.109.85 [aab9f6ef-7ad3-445d-be0c-3a91eb95d3bb]
fs-ai  | 2025-05-19 15:50:39.062339 97.63% [INFO] sofia.c:10459 sofia/external/1001@192.168.109.85 receiving invite from 192.168.109.85:15080 version: 1.10.11-release  64bit call-id: cc2830b0-af28-123e-23b8-525400ef9789
fs-ai  | 2025-05-19 15:50:39.062339 97.63% [INFO] mod_dialplan_xml.c:639 Processing 1001 <1001>->50000001 in context public
fs-ai  | EXECUTE [depth=0] sofia/external/1001@192.168.109.85 set(sip_h_X-cc_tenant_id=1)
fs-ai  | EXECUTE [depth=0] sofia/external/1001@192.168.109.85 set(sip_h_X-cc_work_mode=robot)
fs-ai  | EXECUTE [depth=0] sofia/external/1001@192.168.109.85 socket(127.0.0.1:13002 async full)
fs-ai  | 2025-05-19 15:50:39.062339 97.63% [NOTICE] mod_event_socket.c:452 Trying host: 127.0.0.1:13002
fs-ai  | EXECUTE [depth=0] sofia/external/1001@192.168.109.85 answer()
fs-ai  | 2025-05-19 15:50:39.082351 97.63% [NOTICE] sofia_media.c:90 Pre-Answer sofia/external/1001@192.168.109.85!
fs-ai  | 2025-05-19 15:50:39.082351 97.63% [NOTICE] mod_dptools.c:1406 Channel [sofia/external/1001@192.168.109.85] has been answered
fs-ai  | 2025-05-19 15:50:39.082351 97.63% [INFO] sofia.c:1348 sofia/external/50000001@0.0.0.0:15080 Update Callee ID to "50000001" <sip:50000001@0.0.0.0>
fs-ai  | 2025-05-19 15:50:39.102335 97.63% [NOTICE] sofia.c:8680 Channel [sofia/external/50000001@0.0.0.0:15080] has been answered
fs-ai  | EXECUTE [depth=1] sofia/external/1001@192.168.109.85 set(tts_engine=unimrcp)
fs-ai  | EXECUTE [depth=1] sofia/external/1001@192.168.109.85 set(RECORD_STEREO=true)
fs-ai  | EXECUTE [depth=1] sofia/external/1001@192.168.109.85 set(RECORD_APPEND=false)
fs-ai  | EXECUTE [depth=1] sofia/external/1001@192.168.109.85 set(record_waste_resources=true)
fs-ai  | EXECUTE [depth=1] sofia/external/1001@192.168.109.85 record_session(/tmp/servicePool_test_appId/robot/2025-05-19/aab9f6ef-7ad3-445d-be0c-3a91eb95d3bb.wav)
fs-ai  | EXECUTE [depth=1] sofia/external/1001@192.168.109.85 break()
fs-ai  | EXECUTE [depth=1] sofia/external/1001@192.168.109.85 play_and_detect_speech(silence_stream://-1 detect:unimrcp {start-input-timers=false,no-input-timeout=10000,engine=Xunfei,language=zh_cn,accent=mandarin,sessionId=aab9f6ef-7ad3-445d-be0c-3a91eb95d3bb,Speech-Language=en}builtin:grammar/)
fs-ai  | 2025-05-19 15:50:39.142324 97.63% [INFO] mod_unimrcp.c:3139 asr_handle: name = unimrcp, codec = (null), rate = 8000, grammar = (null), param = (null)
fs-ai  | 2025-05-19 15:50:39.142324 97.63% [INFO] mod_unimrcp.c:3141 codec = L16, rate = 8000, dest = (null)
fs-ai  | 2025-05-19 15:50:39.142324 97.63% [NOTICE] mrcp_application.c:117 (ASR-2383) Create MRCP Handle 0x7f8f8821a4f8 [unimrcpserver-mrcp-v2]
fs-ai  | 2025-05-19 15:50:39.142324 97.63% [INFO] mrcp_client_session.c:131 (ASR-2383) Create Channel ASR-2383 <new>
fs-ai  | 2025-05-19 15:50:39.142324 97.63% [INFO] mrcp_client_session.c:385 (ASR-2383) Receive App Request ASR-2383 <new> [2]
fs-ai  | 2025-05-19 15:50:39.142324 97.63% [INFO] mrcp_client.c:697 (ASR-2383) Add MRCP Handle ASR-2383 <new>
fs-ai  | 2025-05-19 15:50:39.142324 97.63% [NOTICE] mrcp_client_session.c:717 (ASR-2383) Add Control Channel ASR-2383 <new@speechrecog>
fs-ai  | 2025-05-19 15:50:39.162328 97.63% [INFO] mrcp_client_session.c:409 (ASR-2383) Send Offer ASR-2383 <new> [c:1 a:1 v:0] to 192.168.109.85:6060
fs-ai  | 2025-05-19 15:50:39.162328 97.63% [INFO] mrcp_sofiasip_client_agent.c:359 (ASR-2383) Local SDP ASR-2383 <new>





fs-ai  | 2025-05-19 15:50:39.362350 97.63% [INFO] mpf_rtp_stream.c:331 () Enable RTP Session 192.168.109.85:3768
fs-ai  | 2025-05-19 15:50:39.362350 97.63% [INFO] mpf_rtp_stream.c:505 () Open RTP Receiver 192.168.109.85:3768 <- 192.168.109.85:15186 playout [0 ms] bounds [0 - 600 ms] adaptive [0] skew detection [1]
fs-ai  | 2025-05-19 15:50:39.362350 97.63% [INFO] mpf_bridge.c:111 () Media Path TTS-2384 Source->[PCMU/8000/1]->Decoder->[LPCM/8000/1]->Bridge->[LPCM/8000/1]->Sink
fs-ai  | 2025-05-19 15:50:39.362350 97.63% [INFO] mrcp_client_session.c:453 (TTS-2384) Raise App Response TTS-2384 <2aebfb9495ad4b4d> [2] SUCCESS [0]
fs-ai  | 2025-05-19 15:50:39.362350 97.63% [INFO] mrcp_client_session.c:390 (TTS-2384) Receive App MRCP Request TTS-2384 <2aebfb9495ad4b4d>
fs-ai  | 2025-05-19 15:50:39.362350 97.63% [INFO] mrcp_client_session.c:620 (TTS-2384) Send MRCP Request TTS-2384 <2aebfb9495ad4b4d@speechsynth> [1]
fs-ai  | 2025-05-19 15:50:39.362350 97.63% [INFO] mrcp_client_connection.c:551 (TTS-2384) Send MRCPv2 Data 192.168.109.85:53998 <-> 192.168.109.85:1644 [374 bytes]
fs-ai  | MRCP/2.0 374 SPEAK 1
fs-ai  | Channel-Identifier: 2aebfb9495ad4b4d@speechsynth
fs-ai  | Content-Type: text/plain
fs-ai  | Voice-Name: test
fs-ai  | Vendor-Specific-Parameters: engine=Xunfei;traceId=f73883cb-07f6-48f1-98bc-b3073f54c7b7;vadEndTime=null;volume=50;speed=55;voiceId=x4_lingxiaoying_en;pitch=50;sessionId=aab9f6ef-7ad3-445d-be0c-3a91eb95d3bb
fs-ai  | Content-Length: 30
fs-ai  |
fs-ai  | 请说出您要咨询的问题
fs-ai  | 2025-05-19 15:50:39.362350 97.63% [INFO] mrcp_client_connection.c:656 () Receive MRCPv2 Data 192.168.109.85:53998 <-> 192.168.109.85:1644 [83 bytes]
fs-ai  | MRCP/2.0 83 1 200 IN-PROGRESS
fs-ai  | Channel-Identifier: 2aebfb9495ad4b4d@speechsynth
fs-ai  |
fs-ai  |
fs-ai  | 2025-05-19 15:50:39.362350 97.63% [INFO] mrcp_client_session.c:498 (TTS-2384) Raise App MRCP Response TTS-2384 <2aebfb9495ad4b4d>
fs-ai  | EXECUTE [depth=3] sofia/external/1001@192.168.109.85 detect_speech(resume)
fs-ai  | 2025-05-19 15:50:43.882347 97.43% [INFO] switch_channel.c:528 RECV DTMF 1:640
fs-ai  | 2025-05-19 15:50:43.962363 97.43% [INFO] switch_channel.c:528 RECV DTMF 1:640
fs-ai  | 2025-05-19 15:50:49.762342 97.27% [INFO] mrcp_client_connection.c:656 () Receive MRCPv2 Data 192.168.109.85:53998 <-> 192.168.109.85:1644 [122 bytes]
fs-ai  | MRCP/2.0 122 SPEAK-COMPLETE 1 COMPLETE
fs-ai  | Channel-Identifier: 2aebfb9495ad4b4d@speechsynth
fs-ai  | Completion-Cause: 000 normal
fs-ai  |
fs-ai  |
fs-ai  | 2025-05-19 15:50:49.782336 97.27% [INFO] mrcp_client_session.c:514 (TTS-2384) Raise App MRCP Event TTS-2384 <2aebfb9495ad4b4d>
fs-ai  | 2025-05-19 15:50:49.802343 97.27% [INFO] mrcp_client_session.c:385 (TTS-2384) Receive App Request TTS-2384 <2aebfb9495ad4b4d> [1]
fs-ai  | 2025-05-19 15:50:49.802343 97.27% [INFO] mrcp_client_session.c:828 (TTS-2384) Terminate Session TTS-2384 <2aebfb9495ad4b4d>
fs-ai  | 2025-05-19 15:50:49.802343 97.27% [INFO] mrcp_client_connection.c:480 (TTS-2384) Remove Control Channel <2aebfb9495ad4b4d@speechsynth> [1]
fs-ai  | 2025-05-19 15:50:49.802343 97.27% [INFO] mrcp_sofiasip_client_agent.c:621 () Receive SIP Event [nua_r_bye] Status 200 OK [unimrcpserver-mrcp-v2]
fs-ai  | 2025-05-19 15:50:49.802343 97.27% [INFO] mrcp_sofiasip_client_agent.c:621 () Receive SIP Event [nua_i_state] Status 200 to BYE [unimrcpserver-mrcp-v2]
fs-ai  | 2025-05-19 15:50:49.802343 97.27% [NOTICE] mrcp_sofiasip_client_agent.c:558 (TTS-2384) SIP Call State TTS-2384 [terminated]
fs-ai  | 2025-05-19 15:50:49.802343 97.27% [INFO] mrcp_client_session.c:207 (TTS-2384) Session Terminated TTS-2384 <2aebfb9495ad4b4d>
fs-ai  | 2025-05-19 15:52:04,000 INFO /tmp/servicePool_test_appId/manual/2025-05-19/ec682b32-5a44-4a96-83ad-977c0efd20f9.wav
fs-ai  | 2025-05-19 15:52:04,005 INFO 172.26.0.11 - - [19/May/2025 15:52:04] "POST /audio HTTP/1.1" 200 -
fs-ai  | 2025-05-19 15:50:49.822350 97.27% [INFO] mpf_rtp_stream.c:537 () Close RTP Receiver 192.168.109.85:3768 <- 192.168.109.85:15186 [r:121 l:0 j:60 p:0 d:1 i:0]
fs-ai  | 2025-05-19 15:50:49.822350 97.27% [INFO] mpf_rtp_stream.c:418 () Remove RTP Session 192.168.109.85:3768
fs-ai  | 2025-05-19 15:50:49.822350 97.27% [INFO] mpf_rtp_stream.c:1231 () Generate RTCP RR [ssrc:1666739871 last_seq:121 j:60 lost:0 frac:0]
fs-ai  | 2025-05-19 15:50:49.822350 97.27% [INFO] mpf_rtp_stream.c:1405 () Send Compound RTCP Packet [BYE] [84 bytes] 192.168.109.85:3769 -> 192.168.109.85:15187
fs-ai  | 2025-05-19 15:50:49.822350 97.27% [INFO] mrcp_client.c:707 (TTS-2384) Remove MRCP Handle TTS-2384 <2aebfb9495ad4b4d>
fs-ai  | 2025-05-19 15:50:49.822350 97.27% [INFO] mrcp_client_session.c:453 (TTS-2384) Raise App Response TTS-2384 <2aebfb9495ad4b4d> [1] SUCCESS [0]
fs-ai  | 2025-05-19 15:50:49.822350 97.27% [NOTICE] mrcp_application.c:211 (TTS-2384) Destroy MRCP Handle TTS-2384
fs-ai  | EXECUTE [depth=2] sofia/external/1001@192.168.109.85 detect_speech(param start-input-timers true)
fs-ai  | 2025-05-19 15:51:13.902347 97.30% [WARNING] sofia_reg.c:3210 Can't find user [9898000670004699@192.168.109.85] from 172.70.100.1
fs-ai  | You must define a domain called '192.168.109.85' in your directory and add a user with the id="9898000670004699" attribute
fs-ai  | and you must configure your device to use the proper domain in its authentication credentials.
fs-ai  | 2025-05-19 15:52:03.962346 97.60% [NOTICE] sofia.c:1065 Hangup sofia/external/1001@192.168.109.85:15080 [CS_EXECUTE] [NORMAL_CLEARING]
fs-ai  | 2025-05-19 15:52:03.982348 97.60% [NOTICE] switch_ivr_bridge.c:1027 Hangup sofia/external/50000001@0.0.0.0:15080 [CS_EXCHANGE_MEDIA] [NORMAL_CLEARING]
fs-ai  | 2025-05-19 15:52:03.982348 97.60% [NOTICE] switch_core_session.c:1762 Session 1220 (sofia/external/50000001@0.0.0.0:15080) Ended
fs-ai  | 2025-05-19 15:52:03.982348 97.60% [NOTICE] switch_core_session.c:1766 Close Channel sofia/external/50000001@0.0.0.0:15080 [CS_DESTROY]
fs-ai  | 2025-05-19 15:52:03.982348 97.60% [NOTICE] switch_core_session.c:1762 Session 1219 (sofia/external/1001@192.168.109.85:15080) Ended
fs-ai  | 2025-05-19 15:52:03.982348 97.60% [NOTICE] switch_core_session.c:1766 Close Channel sofia/external/1001@192.168.109.85:15080 [CS_DESTROY]
fs-ai  | 2025-05-19 15:52:03.982348 97.60% [NOTICE] sofia.c:1065 Hangup sofia/external/1001@192.168.109.85 [CS_EXECUTE] [NORMAL_CLEARING]
fs-ai  | 2025-05-19 15:52:03.982348 97.60% [INFO] mrcp_client_session.c:390 (ASR-2383) Receive App MRCP Request ASR-2383 <93a9b16d80a04132>
fs-ai  | 2025-05-19 15:52:03.982348 97.60% [INFO] mrcp_client_session.c:620 (ASR-2383) Send MRCP Request ASR-2383 <93a9b16d80a04132@speechrecog> [3]
fs-ai  | 2025-05-19 15:52:03.982348 97.60% [INFO] mrcp_client_connection.c:551 (ASR-2383) Send MRCPv2 Data 192.168.109.85:53998 <-> 192.168.109.85:1644 [72 bytes]
fs-ai  | MRCP/2.0 72 STOP 3
fs-ai  | Channel-Identifier: 93a9b16d80a04132@speechrecog
fs-ai  |
fs-ai  |
fs-ai  | 2025-05-19 15:52:03.982348 97.60% [INFO] mrcp_client_connection.c:656 () Receive MRCPv2 Data 192.168.109.85:53998 <-> 192.168.109.85:1644 [108 bytes]
fs-ai  | MRCP/2.0 108 3 200 COMPLETE
fs-ai  | Channel-Identifier: 93a9b16d80a04132@speechrecog
fs-ai  | Active-Request-Id-List: 1
fs-ai  |
fs-ai  |
fs-ai  | 2025-05-19 15:52:03.982348 97.60% [INFO] mrcp_client_session.c:498 (ASR-2383) Raise App MRCP Response ASR-2383 <93a9b16d80a04132>
fs-ai  | 2025-05-19 15:52:04.002339 97.60% [INFO] mrcp_client_session.c:385 (ASR-2383) Receive App Request ASR-2383 <93a9b16d80a04132> [1]
fs-ai  | 2025-05-19 15:52:04.002339 97.60% [INFO] mrcp_client_session.c:828 (ASR-2383) Terminate Session ASR-2383 <93a9b16d80a04132>
fs-ai  | 2025-05-19 15:52:04.002339 97.60% [INFO] mrcp_client_connection.c:480 (ASR-2383) Remove Control Channel <93a9b16d80a04132@speechrecog> [0]
fs-ai  | 2025-05-19 15:52:04.002339 97.60% [INFO] mrcp_client_connection.c:407 () Close TCP/MRCPv2 Connection 192.168.109.85:53998 <-> 192.168.109.85:1644
fs-ai  | 2025-05-19 15:52:04.002339 97.60% [INFO] mrcp_sofiasip_client_agent.c:621 () Receive SIP Event [nua_r_bye] Status 200 OK [unimrcpserver-mrcp-v2]
fs-ai  | 2025-05-19 15:52:04.002339 97.60% [INFO] mrcp_sofiasip_client_agent.c:621 () Receive SIP Event [nua_i_state] Status 200 to BYE [unimrcpserver-mrcp-v2]
fs-ai  | 2025-05-19 15:52:04,030 INFO /tmp/servicePool_test_appId/robot/2025-05-19/aab9f6ef-7ad3-445d-be0c-3a91eb95d3bb.wav






20250519
准备和搭建徐工UAT和PRD环境的VPN等网络基础软件
分析徐工PRD环境fs日志，排查徐工asr无识别结果问题
修改港铁POC 切换vad为联想vad，调试打断和asr识别丢首字问题
定位和修复港铁POC 联想vad送数据时崩溃问题



定位港铁POC asr识别结果不准问题
定位港铁POC智能打断不灵敏问题


engine=Xunfei;sessionId=03ad9124-31cb-4cb9-ae5c-8d56775dee5c
服务ID：1909235891742773248
电话号码：+8615161339666
呼入时间：2025-04-07 21:24:43





宇宙: https://wiki.knowdee.com/bin/view/01%20%E7%AB%8B%E9%A1%B9%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86/02-%E4%BA%A4%E4%BB%98%E9%A1%B9%E7%9B%AE/2024/%E5%BE%90%E5%B7%A5400%E6%99%BA%E8%83%BD%E5%91%BC%E5%8F%AB%E4%B8%AD%E5%BF%83%E7%B3%BB%E7%BB%9F%E9%87%8D%E6%9E%84%E9%A1%B9%E7%9B%AE/
宇宙: [图片]
宇宙: vpn和服务器
宇宙: uat环境fs什么的都在 10.188.5.2
宇宙: /home/project/fs
/data/project/fs

私有ip:
10.188.5.2
root/XcmG#CRM@250205

生产环境：
10.188.6.233


运维监控系统日志：
http://10.188.6.61:3000  账号admin 密码knowdee


zstd -d core.zst -o core


var->_iPos:%d iTotal:%d iBeginPos:%d   iBeginTime:%d pOptions->_iSampleRatio:%d",
    __s=0x7f997a7fb8b0 "var->_iPos:80800 iTotal:8000 iBeginPos:72800   iBeginTime:4550




20250516
联调港铁POC mrcp支持多语种切换参数和功能
联调港铁POC asr-proxy支持多语种切换参数和功能
排查港铁POC tts调用异常问题


20250515
修复kd-unimrcp编译失败问题(libtool)
修复kd-unimrcp拉取submodule失败问题
构建kd-unimrcp联调docker镜像
调试新版kd-unimrcp docker镜像




chmod +x build/get-version.sh

git pull --recurse-submodules




lit_dev4_centos:
2025-05-15 07:54:51:976845 [NOTICE] Run as Daemon
2025-05-15 07:54:51:977097 [NOTICE] UniMRCP Server [1.7.0]
2025-05-15 07:54:51:977127 [INFO]   APR [1.5.2]
2025-05-15 07:54:51:977179 [NOTICE] Create MRCP Server
2025-05-15 07:54:51:977256 [NOTICE] Open Config File [/usr/local/unimrcp/conf/unimrcpserver.xml]



192.168.109.4:443/hoicee/unimrcp:waihu-prod-latest
unimrcp  | 2025-05-14 19:55:16:793475 src/unimrcp_server.c:092 139896783997056 [NOTICE] UniMRCP Server [1.7.0]
unimrcp  | 2025-05-14 19:55:16:793480 src/unimrcp_server.c:093 139896783997056 [INFO]   APR [1.2.8]
unimrcp  | 2025-05-14 19:55:16:793491 src/mrcp_server.c:195 139896783997056 [NOTICE] Create MRCP Server


20250515
[root@a5f218fa2c94 kd-unimrcp]# md5sum plugin/demorecog.*
d239ec8699da11c46195294cbd4c8b02  plugin/demorecog.a
f12a52b58bbf49df9bbf6f9e34aac97a  plugin/demorecog.la
06f81ae266199e0d166d38dc1cc2c169  plugin/demorecog.so
06f81ae266199e0d166d38dc1cc2c169  plugin/demorecog.so.0
06f81ae266199e0d166d38dc1cc2c169  plugin/demorecog.so.0.7.0
[root@a5f218fa2c94 kd-unimrcp]# md5sum lib/libkdm_*
d60676d28f9b31b2dc03fac44e96124b  lib/libkdm_asr_proxy.so
116e060407766fb595c32aa9e53e5373  lib/libkdm_tts_proxy.so



/usr/local/kd-unimrcp:
[root@a5f218fa2c94 lib]# md5sum libkdm_*
d60676d28f9b31b2dc03fac44e96124b  libkdm_asr_proxy.so
116e060407766fb595c32aa9e53e5373  libkdm_tts_proxy.so
[root@a5f218fa2c94 plugin]# md5sum demorecog.*
928ffa21c14f17f4c73f08a5fe35a801  demorecog.a
f12a52b58bbf49df9bbf6f9e34aac97a  demorecog.la
06f81ae266199e0d166d38dc1cc2c169  demorecog.so
06f81ae266199e0d166d38dc1cc2c169  demorecog.so.0
06f81ae266199e0d166d38dc1cc2c169  demorecog.so.0.7.0









[root@a5f218fa2c94 kd-unimrcp]# md5sum kd-unimrcp/lib/libkdm_*
c5eb62d9d779b51c547942fda4a2b81a  kd-unimrcp/lib/libkdm_asr_proxy.so
46fa4ac234d244a35164045cdcf0c5e9  kd-unimrcp/lib/libkdm_tts_proxy.so
[root@a5f218fa2c94 kd-unimrcp]# md5sum kd-unimrcp/plugin/demorecog.*
9ae05fcb4464194a3757919c20d3baa0  kd-unimrcp/plugin/demorecog.a
d4f79287eb3ed74edd393019effa7860  kd-unimrcp/plugin/demorecog.la
b3c725fed47535431945444f8890c0dd  kd-unimrcp/plugin/demorecog.so
b3c725fed47535431945444f8890c0dd  kd-unimrcp/plugin/demorecog.so.0
b3c725fed47535431945444f8890c0dd  kd-unimrcp/plugin/demorecog.so.0.7.0

20250514
[root@a5f218fa2c94 kd-unimrcp]# md5sum kd-unimrcp/lib/libkdm_*
b4e68fc8f71befa50dd0e0b07a992d76  kd-unimrcp/lib/libkdm_asr_proxy.so
46fa4ac234d244a35164045cdcf0c5e9  kd-unimrcp/lib/libkdm_tts_proxy.so
[root@a5f218fa2c94 kd-unimrcp]# md5sum kd-unimrcp/plugin/demorecog.*
25d8afbd5f9f9e8112f50be32c64a8ab  kd-unimrcp/plugin/demorecog.a
d4f79287eb3ed74edd393019effa7860  kd-unimrcp/plugin/demorecog.la
b3c725fed47535431945444f8890c0dd  kd-unimrcp/plugin/demorecog.so
b3c725fed47535431945444f8890c0dd  kd-unimrcp/plugin/demorecog.so.0
b3c725fed47535431945444f8890c0dd  kd-unimrcp/plugin/demorecog.so.0.7.0




- 20250514
调研讯飞asr同时支持粤语、英语、中文普通话三个语种功能；
修改讯飞asr API接口参数，调测支持粤语语音识别功能；
开发mrcp支持多语种切换参数和功能
开发asr-proxy支持多语种切换参数和功能



"business":{"domain": "iat", "language": "zh_cn", "accent": "cantonese", "ptt":0, "vinfo":0,"vad_eos":10000},


unimrcp  | Get request parameter = {"common":{"app_id":"5e815ba7"},"business":{"domain": "xfime-mianqie", "language": "zh_cn", "accent": "mandarin", "ptt":0, "vinfo":0,"vad_eos":10000},"data": {"status":0,"format": "audio/L16;rate=8000","audio":"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAgACAAIAAAAAAD4//j/+P/4/wAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAL==","encoding": "raw"}}




unimrcp  | Vendor-Specific-Parameters: accent=mandarin;engine=Xunfei;language=zh_cn;sessionId=dd78beba-341a-4403-a394-2e4fea1b3dd9
unimrcp  | Get request parameter = {"common":{"app_id":"5e815ba7"},"business":{"domain": "xfime-mianqie", "language": "zh_cn", "accent": "mandarin", "ptt":0, "vinfo":0,"vad_eos":10000},"data": {"status":0,"format": "audio/L16;rate=8000","audio":"8P/w//j/+P/4/+D/yP/o/wgA8P/A/8j/6P/o/+j/+P8QAAAAyP/Y/+j/4P/o/+j/6P/w//D/+P/4/wAAAAD4//j/+P/4//j/8P/w//j/6P/g/+D/+P8IAAgACAAAAAAAGAAgABgACAD4/xAAIAAgABAAAAAAABAAGAAAAPD/8P8AAAgACAAAAAgAGAAgABgAGAAgACgAIAAYACAAIAAYAL==","encoding": "raw"}}
unimrcp  | Vendor-Specific-Parameters: accent=mandarin;engine=Xunfei;language=zh_cn;sessionId=dd78beba-341a-4403-a394-2e4fea1b3dd9
unimrcp  | Vendor-Specific-Parameters: accent=mandarin;engine=Xunfei;language=zh_cn;sessionId=dd78beba-341a-4403-a394-2e4fea1b3dd9
unimrcp  | Vendor-Specific-Parameters: accent=mandarin;engine=Xunfei;language=zh_cn;sessionId=dd78beba-341a-4403-a394-2e4fea1b3dd9
unimrcp  | Get request parameter = {"common":{"app_id":"5e815ba7"},"business":{"domain": "xfime-mianqie", "language": "zh_cn", "accent": "mandarin", "ptt":0, "vinfo":0,"vad_eos":10000},"data": {"status":0,"format": "audio/L16;rate=8000","audio":"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAgACAAIAAAAAAD4//j/+P/4/wAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAL==","encoding": "raw"}}
unimrcp  | Get request parameter = {"common":{"app_id":"5e815ba7"},"business":{"domain": "xfime-mianqie", "language": "zh_cn", "accent": "mandarin", "ptt":0, "vinfo":0,"vad_eos":10000},"data": {"status":0,"format": "audio/L16;rate=8000","audio":"AAAAAAAACAAIAAAAAAAAAAAACAAIAAAAAAD4/wAAAAAAAAAAAAAIAAAAAAAAAAAAAAD4/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAD4/wAACAAIAAgAAAAAAAAAAAAAAAAACAAIAAAAAAD4/wAAAAAAAAgACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+P/4//j/AAAIAAgACAAAAL==","encoding": "raw"}}
unimrcp  | Get request parameter = {"common":{"app_id":"5e815ba7"},"business":{"domain": "xfime-mianqie", "language": "zh_cn", "accent": "mandarin", "ptt":0, "vinfo":0,"vad_eos":10000},"data": {"status":0,"format": "audio/L16;rate=8000","audio":"ZPlk+WT5RPhE90T35Pgk/Lz+zAFMA8wBTANcB7wJPA78E/wV/BX8FPwSPA88ClwENP6k+UT3RPdE+ET3RPQE8ATtBOwE7sTxxPd0/cwBnAU8CjwMvAy8CzwJXAacA8wBIAB0/rT8pPqk+ET3xPZE9kT2xPZE9sT2xPfk+OT6FP1s/5QAIACcAzwKPA78EfwW/Bf8FvwU/BE8DdwGrAFU/b==","encoding": "raw"}}
unimrcp  | Vendor-Specific-Parameters: accent=mandarin;engine=Xunfei;language=zh_cn;sessionId=dd78beba-341a-4403-a394-2e4fea1b3dd9
unimrcp  | Vendor-Specific-Parameters: accent=cantonese;engine=Xunfei;language=zh_cn;sessionId=67da0d60-f79e-40be-a74d-980bdbd506b2




unimrcp  | 2025-05-14 14:54:42:238128 src/apt_poller_task.c:259 140446814684928 [DEBUG]  Process Poller Wakeup [MRCPv2-Agent-1]
unimrcp  | 2025-05-14 14:54:42:238130 src/apt_task.c:335 140446814684928 [DEBUG]  Process Message [MRCPv2-Agent-1] [0x7fbc54002b90;1;0]
unimrcp  | 2025-05-14 14:54:42:238140 src/mrcp_server_connection.c:693 140446814684928 [INFO]   Send MRCPv2 Data 192.168.109.85:1644 <-> 192.168.109.85:46310 [548 bytes]
unimrcp  | MRCP/2.0 548 RECOGNITION-COMPLETE 1 COMPLETE
unimrcp  | Channel-Identifier: 46ba803fdef74a3c@speechrecog
unimrcp  | Completion-Cause: 000 success
unimrcp  | Content-Type: application/x-nlsml
unimrcp  | Content-Length: 363
unimrcp  |
unimrcp  | <?xml version="1.0"?>
unimrcp  | <result>
unimrcp  |   <interpretation confidence="99" index="1">
unimrcp  |     <session_id>58e0152b-8471-496c-9236-865afa99ca47</session_id>
unimrcp  |     <trace_id>a4a57e32-f919-4285-a7b9-d4dafc0b1b93</trace_id>
unimrcp  |     <vad_end_time>1747205682.237936</vad_end_time>
unimrcp  |     <instance>係基地</instance>
unimrcp  |     <input mode="speech">係基地</input>
unimrcp  |   </interpretation>
unimrcp  | </result>
unimrcp  |









"business":{"domain": "iat", "language": "zh_cn", "accent": "cantonese", "ptt":0, "vinfo":0,"vad_eos":10000},







on_message called with hdl

unimrcp  | [kd-mrcp-asr] rreporter::createCon wsConnection ot _allCons.size = 1, url = ws://ws-api.xfyun.cn/v2/iat?date=Wed%2C+14+May+2025+13%3A22%3A26+GMT&host=ws-api.xfyun.cn&authorization=YXBpX2tleT0iMThiZjNhZDQxOGY3MmIxZWUzMzVlYjFlYzVjMWMwYmYiLCBhbGdvcml0aG09ImhtYWMtc2hhMjU2IiwgaGVhZGVycz0iaG9zdCBkYXRlIHJlcXVlc3QtbGluZSIsIHNpZ25hdHVyZT0iRElQLzU0Z2hZNlBrWGRUeW1KWG9JcWV3d0NzQkdrYkJNYmdNRk5aZTZJcD0i
unimrcp  | [kd-mrcp-asr] iflytekAsrRequestParam::getCommonArgs appid = 5e815ba7
unimrcp  | [kd-mrcp-asr][try to connect] _bClientOpen = Get request parameter = {"common":{"app_id":"5e815ba7"},"business":{"domain": "xfime-mianqie", "language": "zh_cn", "accent": "mandarin", "ptt":0, "vinfo":0,"vad_eos":10000},"data": {"status":0,"format": "audio/L16;rate=8000","audio":"8P8IABgAGAD4/+j/6P/w/+D/yP/I/8j/wP/g/+j/6P/w/wAA+P/g//j/IAAoACgAOAAoABAAGAAoAEAAQAA4ACAAEAAAAPD/4P/Y/+D/8P/w/+j/6P/4//D/2P/g/+D/2P/4//D/2P/Y//D/CAAAACAAKAAQACgAMAAwADAAMAAgABgAIAAQAPj/AAAAAPD/AAAQABgAIAAIAPj/AADw/9j/4P/w/+j/6P8AAPD/8P/4/+j/4P/o/+j/2P/Y/9j/4P/w//D/8P8IAAgA+P8IACAAIAAoAEAAOABAAEgAMAAgABgAEAAAAAAA8P/w//D/+P/4//j/+P/w//j/6P/Y/wAAEAAIAPj/+P/4//D/+P/4//j/CAAQAAAA4P/Y/9j/4P/w//j/EAAgACAAGAAQABAAGAAYACgAGAAQAAgACAA=","encoding": "raw"}}
unimrcp  | 0, _iMaxTry = 1, Uri = ws://ws-api.xfyun.cn/v2/iat?date=Wed%2C+14+May+2025+13%3A22%3A26+GMT&host=ws-api.xfyun.cn&authorization=YXBpX2tleT0iMThiZjNhZDQxOGY3MmIxZWUzMzVlYjFlYzVjMWMwYmYiLCBhbGdvcml0aG09ImhtYWMtc2hhMjU2IiwgaGVhZGVycz0iaG9zdCBkYXRlIHJlcXVlc3QtbGluZSIsIHNpZ25hdHVyZT0iRElQLzU0Z2hZNlBrWGRUeW1KWG9JcWV3d0NzQkdrYkJNYmdNRk5aZTZJcD0i
unimrcp  | [kd-mrcp-asr] wsConnection::on_socket_init >>> hdl = 0x7fe1d0003360
unimrcp  | [kd-mrcp-asr][try to connect] create connection success, connect ... hdl = 0x7fe1d0003360
unimrcp  | ================query tcp v4
unimrcp  | [2025-05-14 13:22:28] [connect] [kd-mrcp-asr] Successful connection
unimrcp  | [2025-05-14 13:22:28] [connect] WebSocket Connection 123.56.17.44:80 v-2 "WebSocket++/0.8.2" /v2/iat?date=Wed%2C+14+May+2025+13%3A22%3A26+GMT&host=ws-api.xfyun.cn&authorization=YXBpX2tleT0iMThiZjNhZDQxOGY3MmIxZWUzMzVlYjFlYzVjMWMwYmYiLCBhbGdvcml0aG09ImhtYWMtc2hhMjU2IiwgaGVhZGVycz0iaG9zdCBkYXRlIHJlcXVlc3QtbGluZSIsIHNpZ25hdHVyZT0iRElQLzU0Z2hZNlBrWGRUeW1KWG9JcWV3d0NzQkdrYkJNYmdNRk5aZTZJcD0i 101
unimrcp  | [kd-mrcp-asr] wsConnection::on_open >>> hdl = 0x7fe1d0003360
unimrcp  | [kd-mrcp-asr] recoProxy::openDbgFile filename: /tmp/vad//c05c1bd0-7642-432f-8993-740ccc612f6c_0002.wav






unimrcp  | [kd-mrcp-asr] iflytekAsrRequestParam::getCommonArgs appid = 5e815ba7
unimrcp  | Get request parameter = {"common":{"app_id":"5e815ba7"},"business":{"domain": "xfime-mianqie", "language": "zh_cn", "accent": "mandarin", "ptt":0, "vinfo":0,"vad_eos":10000},"data": {"status":0,"format": "audio/L16;rate=8000","audio":"tPxwAJwEJPncBNT9JPscBsT3DAOc/uT7jAJM/3T9EAAkAeT6XAT0/fj/ZAGU/RwEdP6kAPQAxACw/8wBrAK0/RwEFP6kAOwBlPwsAvT96P9M/zz/aACM/lgAjP4UAWT8jAF0/awBfP+0/RwHJPpcBvT87AKU/ez+bAKk+twGxPW8CUT4mP+cBkT3PAm0/WQB3ANc/yT8HAdE93z/HARE9bwJ5Pr0/LwJJPqMAbwIJPkcBqQAdP1cBaT4BAHU/JT8lAB0/sj/LAL0/EwDaADk+bwIRPfsAZwGRPa8Cjz/NP68CmT87AJcBOT67ALU/ST6zAGk+hT+nAOU/JwDFAEAAJwFJPncBhz/pPg8CuT5SADcBOT6DAJEAST6jAF0/qT4VAFk+tT99AAU/dwDjAKcA1wFHAVcBcQAnARsAmT7LAN=","encoding": "raw"}}
unimrcp  | [kd-mrcp-asr][try to connect] _bClientOpen = 0, _iMaxTry = 1, Uri = ws://ws-api.xfyun.cn/v2/iat?date=Wed%2C+14+May+2025+11%3A08%3A53+GMT&host=ws-api.xfyun.cn&authorization=YXBpX2tleT0iMThiZjNhZDQxOGY3MmIxZWUzMzVlYjFlYzVjMWMwYmYiLCBhbGdvcml0aG09ImhtYWMtc2hhMjU2IiwgaGVhZGVycz0iaG9zdCBkYXRlIHJlcXVlc3QtbGluZSIsIHNpZ25hdHVyZT0iaTErcUlxNFpjczFha0dCbGpQOGxGT0RaRHkyRTZPU3RHdHRzRHErbnRsTj0i
unimrcp  | [kd-mrcp-asr] wsConnection::on_socket_init >>> hdl = 0x7fe1d0003360
unimrcp  | [kd-mrcp-asr][try to connect] create connection success, connect ... hdl = 0x7fe1d0003360
unimrcp  | ================query tcp v4
unimrcp  | [2025-05-14 11:08:53] [connect] [kd-mrcp-asr] Successful connection
unimrcp  | [2025-05-14 11:08:53] [connect] WebSocket Connection 39.105.54.181:80 v-2 "WebSocket++/0.8.2" /v2/iat?date=Wed%2C+14+May+2025+11%3A08%3A53+GMT&host=ws-api.xfyun.cn&authorization=YXBpX2tleT0iMThiZjNhZDQxOGY3MmIxZWUzMzVlYjFlYzVjMWMwYmYiLCBhbGdvcml0aG09ImhtYWMtc2hhMjU2IiwgaGVhZGVycz0iaG9zdCBkYXRlIHJlcXVlc3QtbGluZSIsIHNpZ25hdHVyZT0iaTErcUlxNFpjczFha0dCbGpQOGxGT0RaRHkyRTZPU3RHdHRzRHErbnRsTj0i 101
unimrcp  | [kd-mrcp-asr] wsConnection::on_open >>> hdl = 0x7fe1d0003360
unimrcp  | [kd-mrcp-asr] recoProxy::openDbgFile filename: /tmp/vad//ff0fed76-e021-4a84-9305-15f819607e63_0000.wav
unimrcp  | [kd-mrcp-asr] on_message called with hdl = 0x7fe1d0003360 and message = {"code":11200,"message":"licc failed","sid":"iat000d81ec@dx196ccc436eaa11f802"}
unimrcp  | code is11200err is licc failed[2025-05-14 11:08:53] [control] Control frame received with opcode 8
unimrcp  | [kd-mrcp-asr] wsConnection::sendMsg message send error, msg: {"data": {"status":1,"format": "audio/L16;rate=8000","audio":"RPbE8MTzFP08CvwU/Bf8D9wE5PrE9cT3pPpk+cTzBOqE3YTZBONE9rwOfCB8JvwbvAus/sT1xPaU/VQB7AE0/mT6JPss/1wHPA/8D7wJVP3E8cTw5Pq8CvwW/Bj8EVwF5PtE+ET4ZPy8/sT3BOqE24TVhNsE71wH/Bp8JPwe/A/0AET2xPRk+2wCHAbMApT8RPhk+twF/A/8EDwLqP9E9Q==","encoding": "raw"}}unimrcp  | [kd-mrcp-asr] iflytekAsrRequestParam::getCommonArgs appid = 5e815ba7
unimrcp  | Get request parameter = {"common":{"app_id":"5e815ba7"},"business":{"domain": "xfime-mianqie", "language": "zh_cn", "accent": "mandarin", "ptt":0, "vinfo":0,"vad_eos":10000},"data": {"status":0,"format": "audio/L16;rate=8000","audio":"tPxwAJwEJPncBNT9JPscBsT3DAOc/uT7jAJM/3T9EAAkAeT6XAT0/fj/ZAGU/RwEdP6kAPQAxACw/8wBrAK0/RwEFP6kAOwBlPwsAvT96P9M/zz/aACM/lgAjP4UAWT8jAF0/awBfP+0/RwHJPpcBvT87AKU/ez+bAKk+twGxPW8CUT4mP+cBkT3PAm0/WQB3ANc/yT8HAdE93z/HARE9bwJ5Pr0/LwJJPqMAbwIJPkcBqQAdP1cBaT4BAHU/JT8lAB0/sj/LAL0/EwDaADk+bwIRPfsAZwGRPa8Cjz/NP68CmT87AJcBOT67ALU/ST6zAGk+hT+nAOU/JwDFAEAAJwFJPncBhz/pPg8CuT5SADcBOT6DAJEAST6jAF0/qT4VAFk+tT99AAU/dwDjAKcA1wFHAVcBcQAnARsAmT7LAN=","encoding": "raw"}}
unimrcp  | [kd-mrcp-asr][try to connect] _bClientOpen = 0, _iMaxTry = 1, Uri = ws://ws-api.xfyun.cn/v2/iat?date=Wed%2C+14+May+2025+11%3A08%3A53+GMT&host=ws-api.xfyun.cn&authorization=YXBpX2tleT0iMThiZjNhZDQxOGY3MmIxZWUzMzVlYjFlYzVjMWMwYmYiLCBhbGdvcml0aG09ImhtYWMtc2hhMjU2IiwgaGVhZGVycz0iaG9zdCBkYXRlIHJlcXVlc3QtbGluZSIsIHNpZ25hdHVyZT0iaTErcUlxNFpjczFha0dCbGpQOGxGT0RaRHkyRTZPU3RHdHRzRHErbnRsTj0i
unimrcp  | [kd-mrcp-asr] wsConnection::on_socket_init >>> hdl = 0x7fe1d0003360
unimrcp  | [kd-mrcp-asr][try to connect] create connection success, connect ... hdl = 0x7fe1d0003360
unimrcp  | ================query tcp v4
unimrcp  | [2025-05-14 11:08:53] [connect] [kd-mrcp-asr] Successful connection
unimrcp  | [2025-05-14 11:08:53] [connect] WebSocket Connection 39.105.54.181:80 v-2 "WebSocket++/0.8.2" /v2/iat?date=Wed%2C+14+May+2025+11%3A08%3A53+GMT&host=ws-api.xfyun.cn&authorization=YXBpX2tleT0iMThiZjNhZDQxOGY3MmIxZWUzMzVlYjFlYzVjMWMwYmYiLCBhbGdvcml0aG09ImhtYWMtc2hhMjU2IiwgaGVhZGVycz0iaG9zdCBkYXRlIHJlcXVlc3QtbGluZSIsIHNpZ25hdHVyZT0iaTErcUlxNFpjczFha0dCbGpQOGxGT0RaRHkyRTZPU3RHdHRzRHErbnRsTj0i 101
unimrcp  | [kd-mrcp-asr] wsConnection::on_open >>> hdl = 0x7fe1d0003360
unimrcp  | [kd-mrcp-asr] recoProxy::openDbgFile filename: /tmp/vad//ff0fed76-e021-4a84-9305-15f819607e63_0000.wav
unimrcp  | [kd-mrcp-asr] on_message called with hdl = 0x7fe1d0003360 and message = {"code":11200,"message":"licc failed","sid":"iat000d81ec@dx196ccc436eaa11f802"}
unimrcp  | code is11200err is licc failed[2025-05-14 11:08:53] [control] Control frame received with opcode 8
unimrcp  | [kd-mrcp-asr] wsConnection::sendMsg message send error, msg: {"data": {"status":1,"format": "audio/L16;rate=8000","audio":"RPbE8MTzFP08CvwU/Bf8D9wE5PrE9cT3pPpk+cTzBOqE3YTZBONE9rwOfCB8JvwbvAus/sT1xPaU/VQB7AE0/mT6JPss/1wHPA/8D7wJVP3E8cTw5Pq8CvwW/Bj8EVwF5PtE+ET4ZPy8/sT3BOqE24TVhNsE71wH/Bp8JPwe/A/0AET2xPRk+2wCHAbMApT8RPhk+twF/A/8EDwLqP9E9Q==","encoding": "raw"}}




- 20250513
调试并构建基于centos7 mrcp镜像
测试mrcp运行加载tts-proxy和asr-proxy报错及其调用tts时崩溃问题
调研核实线上在用mrcp镜像构建流程
联调讯飞tts英文单词按照字母发音问题，协助强强解决中文空格异常转换为sss问题
联调联想tts英文单词按照字母发音问题，协助高宇解决英文单词之间空格丢失问题





unimrcp  | Vendor-Specific-Parameters: engine=Xunfei;traceId=cea624c6-5847-4693-9b70-c0836f46c996;vadEndTime=null;volume=50;speed=55;voiceId=x4_EnUs_Lindsay_assist;pitch=50;sessionId=a9e2fcb7-00af-4651-af38-703006f43abe
unimrcp  | Content-Length: 28
unimrcp  |
unimrcp  | Pleasesexpresssyoursquestion
unimrcp  | 2025-05-13 14:32:34:753373 src/mrcp_server_connection.c:412 139818558285568 [INFO]   Assign Control Channel <40f3f183068249c0@speechsynth> to Connection 192.168.109.85:1644 <-> 192.168.109.85:34082 [0] -> [2]
unimrcp  | 2025-05-13 14:32:34:753379 src/apt_task.c:263 139818558285568 [DEBUG]  Signal Message to [MRCP Server] [0x7f29fc0049b0;2;3]
--
unimrcp  | 2025-05-13 14:32:34:753509 src/demo_synth_engine.c:392 139818665518848 [INFO]   [kd-mrcp-tts] parse tts param: engine = Xunfei, speed = 55, voiceId1 = , voiceId2 = x4_EnUs_Lindsay_assist, pitch = 50, volume = 50, sessionId = a9e2fcb7-00af-4651-af38-703006f43abe, traceId = cea624c6-5847-4693-9b70-c0836f46c996, vadEndTime = null
unimrcp  | 2025-05-13 14:32:34:753516 src/demo_synth_engine.c:421 139818665518848 [INFO]   TTS engine Xunfei
unimrcp  | 2025-05-13 14:32:34:753516 src/apt_task.c:335 139818682304256 [DEBUG]  Process Message [MRCP Server] [0x7f29e800aee0;3;4]
unimrcp  | 2025-05-13 14:32:34:753522 src/demo_synth_engine.c:439 139818665518848 [INFO]   ttsOptions RenderId set to 2, RenderIdGiver set to 1
unimrcp  | 2025-05-13 14:32:34:753525 src/mrcp_synth_state_machine.c:521 139818682304256 [INFO]   Process SPEAK Response <40f3f183068249c0@speechsynth> [1]
unimrcp  | 2025-05-13 14:32:34:753527 src/demo_synth_engine.c:471 139818665518848 [INFO]   TTS voiceId = x4_EnUs_Lindsay_assist, voice-name = test
unimrcp  | 2025-05-13 14:32:34:753530 src/mrcp_synth_state_machine.c:088 139818682304256 [NOTICE] State Transition IDLE -> SPEAKING <40f3f183068249c0@speechsynth>
unimrcp  | 2025-05-13 14:32:34:753531 src/demo_synth_engine.c:360 139818665518848 [INFO]   [kd-mrcp-tts][tts init] sessionId = a9e2fcb7-00af-4651-af38-703006f43abe, traceId = cea624c6-5847-4693-9b70-c0836f46c996, rederId = 2, voiceId = x4_EnUs_Lindsay_assist
unimrcp  | -----------ttsParam pCreateTtsProxy pOptions renderID:2, voiceID:x4_EnUs_Lindsay_assist Speed:55, Pitch:50, Volume:50
unimrcp  | [kd-mrcp-tts] ttsManager TtsMgrSingleton::Instance
unimrcp  | [kd-mrcp-tts] ttsManager TtsMgrSingleton::CreateTtsManager
unimrcp  | 2025-05-13 14:32:34:753535 src/apt_task.c:263 139818682304256 [DEBUG]  Signal Message to [MRCPv2-Agent-1] [0x7f2a0c011d80;1;0]
unimrcp  | [kd-mrcp-tts] create sessionId = a9e2fcb7-00af-4651-af38-703006f43abe, traceId = cea624c6-5847-4693-9b70-c0836f46c996, time = 2025-05-13 14:32:34:753584 src/apt_consumer_task.c:139 139818682304256 [DEBUG]  Wait for Messages [MRCP Server]
unimrcp  | 2025-05-13 14:32:34:753588
--
unimrcp  | Vendor-Specific-Parameters: engine=Xunfei;traceId=4ff47641-5a52-4a67-ab26-b1890960caa3;vadEndTime=1747117971.834434;volume=50;speed=55;voiceId=x4_EnUs_Lindsay_assist;pitch=50;sessionId=a9e2fcb7-00af-4651-af38-703006f43abe
unimrcp  | Content-Length: 247
unimrcp  |
unimrcp  | Itsseemssyousaresexpressingsasstreamsofsthoughtssaboutsyourshometown,strainslines,sandstakingsphotos.sCouldsyouspleasesclarifysyoursspecificsquestionsorsrequestsregardingsthesestopics?sThisswillshelpsmesprovidesasmoresfocusedsandshelpfulsresponse.
unimrcp  | 2025-05-13 14:32:53:754314 src/mrcp_server_connection.c:412 139818558285568 [INFO]   Assign Control Channel <8c9c574d9b6148a8@speechsynth> to Connection 192.168.109.85:1644 <-> 192.168.109.85:34082 [0] -> [2]
unimrcp  | 2025-05-13 14:32:53:754316 src/apt_task.c:263 139818558285568 [DEBUG]  Signal Message to [MRCP Server] [0x7f29fc0069c0;2;3]
--
unimrcp  | 2025-05-13 14:32:53:754395 src/demo_synth_engine.c:392 139818665518848 [INFO]   [kd-mrcp-tts] parse tts param: engine = Xunfei, speed = 55, voiceId1 = , voiceId2 = x4_EnUs_Lindsay_assist, pitch = 50, volume = 50, sessionId = a9e2fcb7-00af-4651-af38-703006f43abe, traceId = 4ff47641-5a52-4a67-ab26-b1890960caa3, vadEndTime = 1747117971.834434
unimrcp  | 2025-05-13 14:32:53:754403 src/demo_synth_engine.c:421 139818665518848 [INFO]   TTS engine Xunfei
unimrcp  | 2025-05-13 14:32:53:754407 src/demo_synth_engine.c:439 139818665518848 [INFO]   ttsOptions RenderId set to 2, RenderIdGiver set to 1
unimrcp  | 2025-05-13 14:32:53:754412 src/demo_synth_engine.c:471 139818665518848 [INFO]   TTS voiceId = x4_EnUs_Lindsay_assist, voice-name = test
unimrcp  | 2025-05-13 14:32:53:754416 src/demo_synth_engine.c:360 139818665518848 [INFO]   [kd-mrcp-tts][tts init] sessionId = a9e2fcb7-00af-4651-af38-703006f43abe, traceId = 4ff47641-5a52-4a67-ab26-b1890960caa3, rederId = 2, voiceId = x4_EnUs_Lindsay_assist
unimrcp  | -----------ttsParam pCreateTtsProxy pOptions renderID:2, voiceID:x4_EnUs_Lindsay_assist Speed:55, Pitch:50, Volume:50
unimrcp  | [kd-mrcp-tts] ttsManager TtsMgrSingleton::Instance
unimrcp  | [kd-mrcp-tts] ttsManager TtsMgrSingleton::CreateTtsManager
unimrcp  | [kd-mrcp-tts] create sessionId = a9e2fcb7-00af-4651-af38-703006f43abe, traceId = 4ff47641-5a52-4a67-ab26-b1890960caa3, time = 2025-05-13 14:32:53:754446
unimrcp  | [kd-mrcp-tts] iFlyTek Create
unimrcp  | [kd-mrcp-tts] iflytekTtsInst::iflytekTtsInst create
--
unimrcp  | =====getFirstFrame ttsParam voiceId:x4_EnUs_Lindsay_assist, speed:55, voiceId:x4_EnUs_Lindsay_assist, pitch:50, volume:50
unimrcp  | [kd-mrcp-tts] iflytekRequestParam::getCommonArgs appid = 65f4da90
unimrcp  | =====getFirstFrame:{"common":{"app_id":"65f4da90"},"business":{"aue": "raw","tte":"UTF8","vcn":"x4_EnUs_Lindsay_assist","speed": 55,"volume": 50,"pitch": 50,"auf":"audio/L16;rate=8000"},"data": {"status": 2,"text":"SXRzc2VlbXNzeW91c2FyZXNleHByZXNzaW5nc2Fzc3RyZWFtc29mc3Rob3VnaHRzc2Fib3V0c3lvdXJzaG9tZXRvd24sc3RyYWluc2xpbmVzLHNhbmRzdGFraW5nc3Bob3Rvcy5zQ291bGRzeW91c3BsZWFzZXNjbGFyaWZ5c3lvdXJzc3BlY2lmaWNzcXVlc3Rpb25zb3JzcmVxdWVzdHNyZWdhcmRpbmdzdGhlc2VzdG9waWNzP3NUaGlzc3dpbGxzaGVscHNtZXNwcm92aWRlc2FzbW9yZXNmb2N1c2Vkc2FuZHNoZWxwZnVsc3Jlc3BvbnNlLg=="}}
unimrcp  | [kd-mrcp-tts][try to connect] Uri = ws://tts-api.xfyun.cn/v2/tts?date=Tue%2C+13+May+2025+14%3A32%3A53+GMT&host=tts-api.xfyun.cn&authorization=YXBpX2tleT0iYzQ2YmE5YWIxZjc5MzgzOWE2YzFiYmZkZTYxYjgxODQiLCBhbGdvcml0aG09ImhtYWMtc2hhMjU2IiwgaGVhZGVycz0iaG9zdCBkYXRlIHJlcXVlc3QtbGluZSIsIHNpZ25hdHVyZT0iczhvVTlSajhyQ2FTZWp5MkNRZTNkRjZCWHJ4bmZ2ZHNHK29CUmpzYnFjMT0i
unimrcp  | Uri is ws://tts-api.xfyun.cn/v2/tts?date=Tue%2C+13+May+2025+14%3A32%3A53+GMT&host=tts-api.xfyun.cn&authorization=YXBpX2tleT0iYzQ2YmE5YWIxZjc5MzgzOWE2YzFiYmZkZTYxYjgxODQiLCBhbGdvcml0aG09ImhtYWMtc2hhMjU2IiwgaGVhZGVycz0iaG9zdCBkYXRlIHJlcXVlc3QtbGluZSIsIHNpZ25hdHVyZT0iczhvVTlSajhyQ2FTZWp5MkNRZTNkRjZCWHJ4bmZ2ZHNHK29CUmpzYnFjMT0i
unimrcp  | [kd-mrcp-tts] wsConnection::on_socket_init >>> hdl = 0x7f29dc01feb0





unimrcp  | Vendor-Specific-Parameters: engine=Lenovo_HTTP;traceId=57536c5c-ae97-4ba9-9320-5f9686fb5873;vadEndTime=1747129414.558103;volume=50;speed=55;voiceId=x4_EnUs_Lindsay_assist;pitch=50;sessionId=5df07351-d064-4188-a2c9-00bd2f6a0bbc
unimrcp  | Content-Length: 1199
unimrcp  |
unimrcp  | Step 1: Analyze the User's Question 1. The user expresses a desire to upgrade subway facilities. 2. The core theme is related to transportation infrastructure enhancement. 3. The user likely seeks information or guidance on how to proceed with this upgrade. Step 2: Evaluate Existing Answers 1. No existing answer provided. 2. Relevant to infrastructure development and urban planning. Step 3: Optimize Answer Quality 1. Content Refinement: The response should directly address the user's intent to upgrade subway facilities. 2. Accuracy: Ensure the information is precise regarding potential steps or considerations for upgrading. 3. Logical Structure:






20250513_build
[root@SC-pre-vm-gangtie-demo2 bin]# md5sum unimrcpserver
5eafccc280ad2b76948f722ecd005c59  unimrcpserver


online:
[root@SC-pre-vm-gangtie-demo2 lib]# md5sum ../bin/unimrcpserver
156d597bdfdf620b0c4e4e3fcb82ebc0  ../bin/unimrcpserver



Commit: a26807c01b33bd7e6790d3dc390d662fd2f8d7b5
Parents: 3767ba0a896aac165566c3985a4be5b8e12d051a
Author: wangwh <wangwh@knowdee.com>
Committer: wangwh <wangwh@knowdee.com>
Date: Thu May 12 2022 15:40:33 GMT+0800 (中国标准时间)

feat:1.add deployment for moli 2,update microsoft cont mode

$ md5sum.exe unimrcpserver
156d597bdfdf620b0c4e4e3fcb82ebc0 *unimrcpserver




- 20250512
开会同步港铁POC进度，探讨asr/tts同时支持三个语种方案
同讯飞技术支持沟通tts同时支持中英粤三个语种的技术实现方案
调试讯飞tts支持粤语、英语播报功能，排查调用英语播报无声问题
添加讯飞tts业务参数英文发音方式reg，编译调试asr-proxy、tts-proxy、mrcp，手动构建mrcp镜像





docker compose logs -f unimrcp|grep -B5 -A5 "parse tts param"
docker compose logs -f unimrcp|grep -B5 -A5 "getFirstFrame"
docker compose logs -f unimrcp|grep -B5 -A5 "Not Using Cache tts"
docker compose logs -f unimrcp|grep -B5 -A5 "message send error"

docker compose logs -f unimrcp|grep "catch exception when send message error is"

docker compose logs -f unimrcp|grep -B5 -A5 "err is "



docker compose logs -f unimrcp|grep -B5 -A5 "tts end"
docker compose logs -f unimrcp|grep -B5 -A5 "tts cb close"





unimrcp  | [kd-mrcp-tts] iflytekTtsInst::speak >>>>>> in
unimrcp  | Get file /tmp/BADC6F150977A87ABFDD57DB520B42B6
unimrcp  | [kd-mrcp-tts] iflytekTtsInst::speak >>>>>> Using Cache tts = Pleases expresss yours question
unimrcp  | [kd-mrcp-tts][tts end] sessionId = ef005930-18eb-4e7e-80c8-ecc9b9e0b789, traceId = e22804bf-278d-48cc-a57e-f6cf70bbd11f, tts_duration = 0.104906, asr_tts_duration = 0
unimrcp  | [kd-mrcp-tts] ttsProxyMsg::recordTime Invalid argument: stod
unimrcp  | 2025-05-12 14:53:36:923394 src/demo_synth_engine.c:162 140634171709184 [INFO]   [kd-mrcp-tts][tts cb close] sessionId = ef005930-18eb-4e7e-80c8-ecc9b9e0b789, traceId = e22804bf-278d-48cc-a57e-f6cf70bbd11f
unimrcp  | [kd-mrcp-tts] iflytekTtsInst::speak >>>>>> out
unimrcp  | 2025-05-12 14:53:36:923398 src/apt_consumer_task.c:139 140634171709184 [DEBUG]  Wait for Messages [Demo Synth Engine]
unimrcp  | 2025-05-12 14:53:36:923406 src/apt_poller_task.c:259 140634065200896 [DEBUG]  Process Poller Wakeup [MRCPv2-Agent-1]
unimrcp  | 2025-05-12 14:53:36:923407 src/apt_task.c:335 140634065200896 [DEBUG]  Process Message [MRCPv2-Agent-1] [0x7fe7ec002b90;1;0]
unimrcp  | 2025-05-12 14:53:36:923411 src/mrcp_server_connection.c:693 140634065200896 [INFO]   Send MRCPv2 Data 192.168.109.85:1644 <-> 192.168.109.85:51774 [83 bytes]
--
unimrcp  | 2025-05-12 14:54:22:397622 src/apt_task.c:335 140634188494592 [DEBUG]  Process Message [MRCP Server] [0x7fe7e4006640;1;2]
unimrcp  | 2025-05-12 14:54:22:397624 src/mrcp_server_session.c:326 140634188494592 [DEBUG]  Push Request to Queue 0x7fe7e4001b80 <10416111cacc4883>
unimrcp  | 2025-05-12 14:54:22:397626 src/apt_consumer_task.c:139 140634188494592 [DEBUG]  Wait for Messages [MRCP Server]
unimrcp  | [kd-mrcp-tts] ttsProxyMsg::recordTime _pAsrTime : 1747032830.319358
unimrcp  | [kd-mrcp-tts][tts end] sessionId = ef005930-18eb-4e7e-80c8-ecc9b9e0b789, traceId = 64ebc7f7-81b1-4ca9-a4e1-a329af49a7b1, tts_duration = 45891.5, asr_tts_duration = 56536.1
unimrcp  | 2025-05-12 14:54:46:855508 src/demo_synth_engine.c:162 140633368934144 [INFO]   [kd-mrcp-tts][tts cb close] sessionId = ef005930-18eb-4e7e-80c8-ecc9b9e0b789, traceId = 64ebc7f7-81b1-4ca9-a4e1-a329af49a7b1
unimrcp  | [2025-05-12 14:54:46] [frame_header] Dispatching write containing 1 message(s) containing 6 header bytes and 2 payload bytes
unimrcp  | [2025-05-12 14:54:46] [frame_header] Header Bytes:
unimrcp  | [0] (6) 88 82 17 ED B2 C3
unimrcp  |
unimrcp  | [2025-05-12 14:54:46] [control] Control frame received with opcode 8





unimrcp  | 2025-05-12 14:50:35:043572 src/demo_synth_engine.c:392 140634171709184 [INFO]   [kd-mrcp-tts] parse tts param: engine = Xunfei, speed = 50, voiceId1 = , voiceId2 = x3_xiaoyue, pitch = 50, volume = 50, sessionId = 8620b69a-9d28-42f9-b0f6-fa006eaae88e, traceId = be2be657-8894-49a1-8a82-da500af7f8d6, vadEndTime = 1747032633.516202
unimrcp  | 2025-05-12 14:50:35:043580 src/demo_synth_engine.c:439 140634171709184 [INFO]   ttsOptions RenderId set to 2, RenderIdGiver set to 1
unimrcp  | 2025-05-12 14:50:35:043586 src/demo_synth_engine.c:360 140634171709184 [INFO]   [kd-mrcp-tts][tts init] sessionId = 8620b69a-9d28-42f9-b0f6-fa006eaae88e, traceId = be2be657-8894-49a1-8a82-da500af7f8d6, rederId = 2, voiceId = x3_xiaoyue
unimrcp  | -----------ttsParam pCreateTtsProxy pOptions renderID:2, voiceID:x3_xiaoyue Speed:50, Pitch:50, Volume:50
unimrcp  | [kd-mrcp-tts] ttsManager TtsMgrSingleton::Instance
unimrcp  | [kd-mrcp-tts] ttsManager TtsMgrSingleton::CreateTtsManager
unimrcp  | [kd-mrcp-tts] create sessionId = 8620b69a-9d28-42f9-b0f6-fa006eaae88e, traceId = be2be657-8894-49a1-8a82-da500af7f8d6, time = 2025-05-12 14:50:35:043605 src/mrcp_synth_state_machine.c:088 140634188494592 [NOTICE] State Transition IDLE -> SPEAKING <3c54796d91754743@speechsynth>
unimrcp  | [kd-mrcp-tts] iFlyTek Create
unimrcp  | [kd-mrcp-tts] iflytekTtsInst::iflytekTtsInst create
unimrcp  | 2025-05-12 14:50:35:043698 src/demo_synth_engine.c:367 140634171709184 [INFO]   [kd-mrcp-tts][tts speak] content = 抱歉，我是粤语智能助手，无法使用普通话回答您的问题。如果您有任何粤语的问题，请随时问我！
unimrcp  | [kd-mrcp-tts] ttsManager speak
unimrcp  | [kd-mrcp-tts] speek, sessionId = 8620b69a-9d28-42f9-b0f6-fa006eaae88e, traceId = be2be657-8894-49a1-8a82-da500af7f8d6, time = 2025-05-12 14:50:35:043704
unimrcp  | [kd-mrcp-tts] iflytekTtsInst::speak >>>>>> in
unimrcp  | [kd-mrcp-tts] iflytekTtsInst::speak >>>>>> Not Using Cache tts = 抱歉，我是粤语智能助手，无法使用普通话回答您的问题。如果您有任何粤语的问题，请随时问我！
unimrcp  | [kd-mrcp-tts] iflytekRequestParam::createUrl reg_url = ws://tts-api.xfyun.cn/v2/tts
unimrcp  | [kd-mrcp-tts] iflytekRequestParam::createUrl api_key = c46ba9ab1f793839a6c1bbfde61b8184
unimrcp  | [kd-mrcp-tts] iflytekRequestParam::createUrl api_secret = ZTA5NTM0YTRhOTVlMjMxODA5MzRiMDQz
unimrcp  | [kd-mrcp-tts] iflytekRequestParam::createUrl host = tts-api.xfyun.cn, path = /v2/tts
unimrcp  | [kd-mrcp-tts] iflytekRequestParam::createUrl signature_origin = host: tts-api.xfyun.cn
unimrcp  | GET /v2/tts HTTP/1.1
unimrcp  | [kd-mrcp-tts] iflytekRequestParam::createUrl authorization_origin = api_key="c46ba9ab1f793839a6c1bbfde61b8184", algorithm="hmac-sha256", headers="host date request-line", signature="R8kRw8CHIbOPpXebxy3GqnziQXbklVZXMfxhydj/x1l="
unimrcp  | [kd-mrcp-tts] iflytekRequestParam::createUrl _finalUrl = ws://tts-api.xfyun.cn/v2/tts?date=Mon%2C+12+May+2025+14%3A50%3A35+GMT&host=tts-api.xfyun.cn&authorization=YXBpX2tleT0iYzQ2YmE5YWIxZjc5MzgzOWE2YzFiYmZkZTYxYjgxODQiLCBhbGdvcml0aG09ImhtYWMtc2hhMjU2IiwgaGVhZGVycz0iaG9zdCBkYXRlIHJlcXVlc3QtbGluZSIsIHNpZ25hdHVyZT0iUjhrUnc4Q0hJYk9QcFhlYnh5M0dxbnppUVhia2xWWlhNZnhoeWRqL3gxbD0i
unimrcp  | =====getFirstFrame ttsParam voiceId:x3_xiaoyue, speed:50, voiceId:x3_xiaoyue, pitch:50, volume:50
unimrcp  | [kd-mrcp-tts][try to connect] Uri = ws://tts-api.xfyun.cn/v2/tts?date=Mon%2C+12+May+2025+14%3A50%3A35+GMT&host=tts-api.xfyun.cn&authorization=YXBpX2tleT0iYzQ2YmE5YWIxZjc5MzgzOWE2YzFiYmZkZTYxYjgxODQiLCBhbGdvcml0aG09ImhtYWMtc2hhMjU2IiwgaGVhZGVycz0iaG9zdCBkYXRlIHJlcXVlc3QtbGluZSIsIHNpZ25hdHVyZT0iUjhrUnc4Q0hJYk9QcFhlYnh5M0dxbnppUVhia2xWWlhNZnhoeWRqL3gxbD0i
unimrcp  | Uri is ws://tts-api.xfyun.cn/v2/tts?date=Mon%2C+12+May+2025+14%3A50%3A35+GMT&host=tts-api.xfyun.cn&authorization=YXBpX2tleT0iYzQ2YmE5YWIxZjc5MzgzOWE2YzFiYmZkZTYxYjgxODQiLCBhbGdvcml0aG09ImhtYWMtc2hhMjU2IiwgaGVhZGVycz0iaG9zdCBkYXRlIHJlcXVlc3QtbGluZSIsIHNpZ25hdHVyZT0iUjhrUnc4Q0hJYk9QcFhlYnh5M0dxbnppUVhia2xWWlhNZnhoeWRqL3gxbD0i
unimrcp  | [kd-mrcp-tts] wsConnection::on_socket_init >>> hdl = 0x7fe7c8070cd0
unimrcp  | ================query tcp v4 tts-api.xfyun.cn:80
unimrcp  | [kd-mrcp-tts] iflytekRequestParam::getCommonArgs appid = 65f4da90
unimrcp  | [2025-05-12 14:50:35] [connect] [kd-mrcp-tts] Successful connection
unimrcp  | [2025-05-12 14:50:35] [connect] WebSocket Connection 124.172.152.234:80 v-2 "WebSocket++/0.8.2" /v2/tts?date=Mon%2C+12+May+2025+14%3A50%3A35+GMT&host=tts-api.xfyun.cn&authorization=YXBpX2tleT0iYzQ2YmE5YWIxZjc5MzgzOWE2YzFiYmZkZTYxYjgxODQiLCBhbGdvcml0aG09ImhtYWMtc2hhMjU2IiwgaGVhZGVycz0iaG9zdCBkYXRlIHJlcXVlc3QtbGluZSIsIHNpZ25hdHVyZT0iUjhrUnc4Q0hJYk9QcFhlYnh5M0dxbnppUVhia2xWWlhNZnhoeWRqL3gxbD0i 101
unimrcp  | [kd-mrcp-tts] wsConnection::on_open >>> hdl = 0x7fe7c8070cd0
unimrcp  | [kd-mrcp-tts] iflytekTtsInst::speak >>>>>> out
unimrcp  | [kd-mrcp-tts] ttsProxyMsg::recordTime _pAsrTime : 1747032633.516202
unimrcp  | [kd-mrcp-tts][tts end] sessionId = 8620b69a-9d28-42f9-b0f6-fa006eaae88e, traceId = be2be657-8894-49a1-8a82-da500af7f8d6, tts_duration = 869.911, asr_tts_duration = 2397.4
unimrcp  | 2025-05-12 14:50:35:913677 src/demo_synth_engine.c:162 140634040022784 [INFO]   [kd-mrcp-tts][tts cb close] sessionId = 8620b69a-9d28-42f9-b0f6-fa006eaae88e, traceId = be2be657-8894-49a1-8a82-da500af7f8d6
unimrcp  | [kd-mrcp-tts] wsConnection::on_close >>> hdl = 0x7fe7c8070cd0





[root@SC-pre-vm-gangtie-demo2 freeswitch]# docker compose logs -f unimrcp|grep -B5 -A5 "iat000d610b@dx196c317cc34a182802"
unimrcp  | [kd-mrcp-asr] wsConnection::sendMsg 2 vad end, sessionId = 468e6046-06a0-4e8e-805c-1694087fb16a, traceId = c2f7b172-6a74-4eb8-b861-6fbfa3cc6cba, time = 2025-05-12 14:04:10:837794
unimrcp  | [2025-05-12 14:04:10] [frame_header] Dispatching write containing 1 message(s) containing 6 header bytes and 22 payload bytes
unimrcp  | [2025-05-12 14:04:10] [frame_header] Header Bytes:
unimrcp  | [0] (6) 81 96 EE 14 49 21
unimrcp  |
unimrcp  | [kd-mrcp-asr] on_message called with hdl = 0x7fe7a000ea20 and message = {"code":10008,"message":"service instance invalid","sid":"iat000d610b@dx196c317cc34a182802"}
unimrcp  | code is10008err is service instance invalid[kd-mrcp-asr] on_message called with hdl = 0x7fe7a000ea20 and message = {"code":10008,"message":"service instance invalid","sid":"iat000d610b@dx196c317cc34a182802"}
unimrcp  | code is10008err is service instance invalid[kd-mrcp-asr] on_message called with hdl = 0x7fe7a000ea20 and message = {"code":10008,"message":"service instance invalid","sid":"iat000d610b@dx196c317cc34a182802"}
unimrcp  | code is10008err is service instance invalid[kd-mrcp-asr] on_message called with hdl = 0x7fe7a000ea20 and message = {"code":10008,"message":"service instance invalid","sid":"iat000d610b@dx196c317cc34a182802"}
unimrcp  | code is10008err is service instance invalidCatch noinput at 40561440 ms, elapsed 10010 ms
unimrcp  | [kd-mrcp-asr] recoProxy::processVadRes Get data len 8000
unimrcp  | [kd-mrcp-asr][warning] iflytekAsrInst::sendFirstMsg iMsgType = 0, recreate_connection_if_timeout = 0
unimrcp  | CreateMsg Index = 36, point = 0x7fe79c018470
unimrcp  | [kd-mrcp-asr] iflytekAsrRequestParam::createUrl reg_url = ws://ws-api.xfyun.cn/v2/iat
--
unimrcp  | [2025-05-12 14:04:21] [frame_header] Dispatching write containing 1 message(s) containing 6 header bytes and 87 payload bytes
unimrcp  | [2025-05-12 14:04:21] [frame_header] Header Bytes:
unimrcp  | [0] (6) 88 D7 CB E3 BA 07
unimrcp  |
unimrcp  | [kd-mrcp-asr] wsConnection::on_close >>> hdl = 0x7fe7a000ea20
unimrcp  | [2025-05-12 14:04:21] [disconnect] Disconnect close local:[1000,Websocket closed!,sid=iat000d610b@dx196c317cc34a182802!reason=server read msg timeout] remote:[1000,Websocket closed!,sid=iat000d610b@dx196c317cc34a182802!reason=server read msg timeout]
unimrcp  | [kd-mrcp-asr] wsConnection::wsConnection >>> uri = ws://ws-api.xfyun.cn/v2/iat?date=Mon%2C+12+May+2025+14%3A04%3A19+GMT&host=ws-api.xfyun.cn&authorization=YXBpX2tleT0iMThiZjNhZDQxOGY3MmIxZWUzMzVlYjFlYzVjMWMwYmYiLCBhbGdvcml0aG09ImhtYWMtc2hhMjU2IiwgaGVhZGVycz0iaG9zdCBkYXRlIHJlcXVlc3QtbGluZSIsIHNpZ25hdHVyZT0iQXM0eDFPMENybkUzMkRzOXhDLzFDY2grR1A2djZWTEk3M0hIZlVBR3R5OT0i
unimrcp  | [kd-mrcp-asr] wsConnection::init >>> uri = ws://ws-api.xfyun.cn/v2/iat?date=Mon%2C+12+May+2025+14%3A04%3A19+GMT&host=ws-api.xfyun.cn&authorization=YXBpX2tleT0iMThiZjNhZDQxOGY3MmIxZWUzMzVlYjFlYzVjMWMwYmYiLCBhbGdvcml0aG09ImhtYWMtc2hhMjU2IiwgaGVhZGVycz0iaG9zdCBkYXRlIHJlcXVlc3QtbGluZSIsIHNpZ25hdHVyZT0iQXM0eDFPMENybkUzMkRzOXhDLzFDY2grR1A2djZWTEk3M0hIZlVBR3R5OT0i
unimrcp  | [kd-mrcp-asr] rreporter::createCon wsConnection ot _allCons.size = 2, url = ws://ws-api.xfyun.cn/v2/iat?date=Mon%2C+12+May+2025+14%3A04%3A19+GMT&host=ws-api.xfyun.cn&authorization=YXBpX2tleT0iMThiZjNhZDQxOGY3MmIxZWUzMzVlYjFlYzVjMWMwYmYiLCBhbGdvcml0aG09ImhtYWMtc2hhMjU2IiwgaGVhZGVycz0iaG9zdCBkYXRlIHJlcXVlc3QtbGluZSIsIHNpZ25hdHVyZT0iQXM0eDFPMENybkUzMkRzOXhDLzFDY2grR1A2djZWTEk3M0hIZlVBR3R5OT0i
unimrcp  | [kd-mrcp-asr] iflytekAsrRequestParam::getCommonArgs appid = 5e815ba7
unimrcp  | [kd-mrcp-asr][try to connect] _bClientOpen = 0, _iMaxTry = Get request parameter = {"common":{"app_id":"5e815ba7"},"business":{"domain": "iat", "language": "zh_cn", "accent": "mandarin", "ptt":0, "vinfo":0,"vad_eos":10000},"data": {"status":0,"format": "audio/L16;rate=8000","audio":"AAD4//j/+P/4/wAAAAAAAPj/8P/w//j/+P/w//D/+P8AAAAACAAAAAAAAADw//D/+P8IAAAAAAAIABAAEAAIAAAAAAAAAPj/AAAAAAAAAAAAAAgACAAIAAgACAAQABAACAAYABgAEAAIAAgAAAAAAAAA8P/4//D/+P8AAPj/+P/w//D/+P8AAAAA+P8AAAAAAAAIAAAA+P/4//j/AAAAAAAAAAAIAAgAAAAAAPj/+P/4//j/CAAIAAgAAAAAAAgAAAAAAAAACAAQAAgAEAAQAAgAAAAAAAAAAADw//j/+P8AAAAACAAAAPj/AAD4/wAAAAAAAAAAAADw//D/AAAAAAgAAAD4/wAA+P8AAAAA+P8AAAgAAAAAAAgAAAAIABAAEAAQABAACAAIABAAEAAYAAgACAAIAAAACAAIAAAA+P8=","encoding": "raw"}}



unimrcp  | [2025-05-12 14:04:10] [frame_header] Dispatching write containing 1 message(s) containing 6 header bytes and 22 payload bytes
unimrcp  | [2025-05-12 14:04:10] [frame_header] Header Bytes:
unimrcp  | [0] (6) 81 96 EE 14 49 21
unimrcp  |
unimrcp  | [kd-mrcp-asr] on_message called with hdl = 0x7fe7a000ea20 and message = {"code":10008,"message":"service instance invalid","sid":"iat000d610b@dx196c317cc34a182802"}
unimrcp  | code is10008err is service instance invalid

[kd-mrcp-asr] on_message called with hdl = 0x7fe7a000ea20 and message = {"code":10008,"message":"service instance invalid","sid":"iat000d610b@dx196c317cc34a182802"}

unimrcp  | code is10008err is service instance invalid[kd-mrcp-asr] on_message called with hdl = 0x7fe7a000ea20 and message = {"code":10008,"message":"service instance invalid","sid":"iat000d610b@dx196c317cc34a182802"}
unimrcp  | code is10008err is service instance invalid[kd-mrcp-asr] on_message called with hdl = 0x7fe7a000ea20 and message = {"code":10008,"message":"service instance invalid","sid":"iat000d610b@dx196c317cc34a182802"}
unimrcp  | code is10008err is service instance invalid



Catch noinput at 40561440 ms, elapsed 10010 ms
unimrcp  | [kd-mrcp-asr] recoProxy::processVadRes Get data len 8000
unimrcp  | [kd-mrcp-asr][warning] iflytekAsrInst::sendFirstMsg iMsgType = 0, recreate_connection_if_timeout = 0
unimrcp  | CreateMsg Index = 36, point = 0x7fe79c018470
unimrcp  | [kd-mrcp-asr] iflytekAsrRequestParam::createUrl reg_url = ws://ws-api.xfyun.cn/v2/iat
unimrcp  | [kd-mrcp-asr] iflytekAsrRequestParam::createUrl api_key = 18bf3ad418f72b1ee335eb1ec5c1c0bf





std::string ret = std::string("{\"common\":") + getCommonArgs() + std::string(",\"business\":") + std::string("{\"aue\": \"raw\",\"tte\":\"UTF8\",\"ttp\":\"" + ttp + "\",\"vcn\":\"" + vcn + "\",\"speed\": " + speed + ",\"volume\": " + volume + ",\"pitch\": " + pitch + ",\"auf\":\"audio/L16;rate=8000\"}") + std::string(",") + getCommonFrame(iType, pBuf, iBufLen) + "}";
std::cout << "=====getFirstFrame:" << ret.c_str() << std::endl;

unimrcp  | =====getFirstFrame ttsParam voiceId:x4_lingxiaoying_en, speed:55, voiceId:x4_lingxiaoying_en, pitch:50, volume:50
unimrcp  | =====getFirstFrame:{"common":{"app_id":"65f4da90"},"business":{"aue": "raw","tte":"UTF8","vcn":"x4_lingxiaoying_en","speed": 55,"volume": 50,"pitch": 50,"auf":"audio/L16;rate=8000"},"data": {"status": 2,"text":"MTk5N+W5tOWPr+S7peeUqOS4jeWQjOeahOaXtuaAgeadpeaPj+i/sO+8jOagueaNruWPpeWtkOeahOmcgOimgeOAguS7peS4i+aYr+S4gOS6m+W4uOingeeahOaXtuaAgeWPiuWFtuS9v+eUqOekuuS+i++8mjEuc3N0YXJzdGFy6L+H5Y675pe2c3RhcnN0YXLvvJrnlKjkuo7mj4/ov7AxOTk35bm05Y+R55Sf55qE5LqL5Lu244CCc3NzLXPnpLrkvovvvJpJbnMxOTk3LHN0aGVzbW92aWVzIlRpdGFuaWMic3dhc3NyZWxlYXNlZC4yLnNzdGFyc3RhcueOsOWcqOWujOaIkOaXtnN0YXJzdGFy77ya55So5LqO5o+P6L+w5LuOMTk5N+W5tOWIsOeOsOWcqOeahOW9seWTjeaIlue7k+aenOOAgnNzcy1z56S65L6L77yaU2luY2VzMTk5NyxzdGVjaG5vbG9neXNoYXNzYWR2YW5jZWRzc2lnbmlmaWNhbnRseS4zLnNzdGFyc3RhcuWwhuadpeaXtnN0YXJzdGFy77ya55So5LqO5o+P6L+w5a+5MTk5N+W5tOS5i+WQjueahOmihOa1i+aIluiuoeWIkuOAgnNzcy1z56S65L6L77yaSW5zMTk5OCxzbWFueXNwZW9wbGVzd2lsbHNyZW1lbWJlcnN0aGVzZXZlbnRzc29mczE5OTcu6YCJ5oup5ZCI6YCC55qE5pe25oCB5Y+W5Yaz5LqO5L2g5biM5pyb6KGo6L6+55qE5pe26Ze05qGG5p625ZKM6K+t5aKD44CC"}}
unimrcp  | =====getFirstFrame ttsParam voiceId:x3_xiaoyue, speed:55, voiceId:x3_xiaoyue, pitch:50, volume:50
unimrcp  | =====getFirstFrame:{"common":{"app_id":"65f4da90"},"business":{"aue": "raw","tte":"UTF8","vcn":"x3_xiaoyue","speed": 55,"volume": 50,"pitch": 50,"auf":"audio/L16;rate=8000"},"data": {"status": 2,"text":"6aaZ5riv6ZOB6Lev5qyi6L+O5oKo77yM5pmu6YCa6K+d6K+35oyJMe+8jOW5v+S4nOivneivt+aMiTLvvIzoi7Hor63or7fmjIkz"}}
unimrcp  | =====getFirstFrame ttsParam voiceId:x4_enus_luna_assist, speed:55, voiceId:x4_enus_luna_assist, pitch:50, volume:50
unimrcp  | =====getFirstFrame:{"common":{"app_id":"65f4da90"},"business":{"aue": "raw","tte":"UTF8","vcn":"x4_enus_luna_assist","speed": 55,"volume": 50,"pitch": 50,"auf":"audio/L16;rate=8000"},"data": {"status": 2,"text":"6aaZ5riv6ZOB6Lev5qyi6L+O5oKo77yM5pmu6YCa6K+d6K+35oyJMe+8jOW5v+S4nOivneivt+aMiTLvvIzoi7Hor63or7fmjIkz"}}
unimrcp  | =====getFirstFrame ttsParam voiceId:x4_enus_luna_assist, speed:55, voiceId:x4_enus_luna_assist, pitch:50, volume:50
unimrcp  | =====getFirstFrame:{"common":{"app_id":"65f4da90"},"business":{"aue": "raw","tte":"UTF8","vcn":"x4_enus_luna_assist","speed": 55,"volume": 50,"pitch": 50,"auf":"audio/L16;rate=8000"},"data": {"status": 2,"text":"6aaZ5riv6ZOB6Lev5qyi6L+O5oKo77yM5pmu6YCa6K+d6K+35oyJMe+8jOW5v+S4nOivneivt+aMiTLvvIzoi7Hor63or7fmjIkz"}}

unimrcp  | [kd-mrcp-tts] iflytekTtsInst::speak >>>>>> Not Using Cache tts = 香港铁路欢迎您，普通话请按1，广东话请按2，英语请按3
unimrcp  | [kd-mrcp-tts] iflytekTtsInst::speak >>>>>> Not Using Cache tts = 香港铁路欢迎您，普通话请按1，广东话请按2，英语请按3
unimrcp  | [kd-mrcp-tts] iflytekTtsInst::speak >>>>>> Not Using Cache tts = 香港铁路欢迎您，普通话请按1，广东话请按2，英语请按3




unimrcp  | 2025-05-12 10:52:59:574365 src/demo_synth_engine.c:392 140634171709184 [INFO]   [kd-mrcp-tts] parse tts param: engine = Xunfei, speed = 55, voiceId1 = , voiceId2 = x4_lingxiaoying_en, pitch = 50, volume = 50, sessionId = 3e8d5e6a-0637-4bb4-8d11-5cd631831f27, traceId = fa475828-fb0e-4b35-99d3-bd8159190f4e, vadEndTime = 1747018377.488813
unimrcp  | 2025-05-12 11:10:36:964401 src/demo_synth_engine.c:392 140634171709184 [INFO]   [kd-mrcp-tts] parse tts param: engine = Xunfei, speed = 55, voiceId1 = , voiceId2 = x4_lingxiaoying_en, pitch = 50, volume = 50, sessionId = 1b69519f-083d-4b27-909c-5f8e8329da83, traceId = c95c161d-74c8-4842-936c-ef930d69ede7, vadEndTime = null
unimrcp  | 2025-05-12 11:10:51:843979 src/demo_synth_engine.c:392 140634171709184 [INFO]   [kd-mrcp-tts] parse tts param: engine = Xunfei, speed = 55, voiceId1 = , voiceId2 = x4_lingxiaoying_en, pitch = 50, volume = 50, sessionId = 1b69519f-083d-4b27-909c-5f8e8329da83, traceId = bfa2ddd7-be26-483a-a793-f21b883ff783, vadEndTime = 1747019449.317773



unimrcp  | =====getFirstFrame ttsParam voiceId:x4_lingxiaoying_en, speed:55, voiceId:x4_lingxiaoying_en, pitch:50, volume:50
unimrcp  | =====getFirstFrame:{"common":{"app_id":"65f4da90"},"business":{"aue": "raw","tte":"UTF8","vcn":"x4_lingxiaoying_en","speed": 55,"volume": 50,"pitch": 50,"auf":"audio/L16;rate=8000"},"data": {"status": 2,"text":"5L2g5rKh5pyJ5oyH5a6a6L6T5Ye66K+t6KiA77yM6K+36Zeu5L2g5biM5pyb5oiR55So5ZOq56eN6K+t6KiA5Zue562U5ZGi77yf77yI5Lit5paHL+iLseaWhy/nsqTor63vvIk="}}
unimrcp  | =====getFirstFrame ttsParam voiceId:x4_lingxiaoying_en, speed:55, voiceId:x4_lingxiaoying_en, pitch:50, volume:50
unimrcp  | =====getFirstFrame:{"common":{"app_id":"65f4da90"},"business":{"aue": "raw","tte":"UTF8","vcn":"x4_lingxiaoying_en","speed": 55,"volume": 50,"pitch": 50,"auf":"audio/L16;rate=8000"},"data": {"status": 2,"text":"6K+36Zeu5oKo5biM5pyb55So5ZOq56eN6K+t6KiA5Zue562U5ZGi77yf77yI5Lit5paH44CB6Iux5paH5oiW57Kk6K+t77yJ"}}
unimrcp  | =====getFirstFrame ttsParam voiceId:x4_lingxiaoying_en, speed:55, voiceId:x4_lingxiaoying_en, pitch:50, volume:50
unimrcp  | =====getFirstFrame:{"common":{"app_id":"65f4da90"},"business":{"aue": "raw","tte":"UTF8","vcn":"x4_lingxiaoying_en","speed": 55,"volume": 50,"pitch": 50,"auf":"audio/L16;rate=8000"},"data": {"status": 2,"text":"6L6T5YWl5paH5qGj77ya5YOP5LuA5LmI5Y2h6YO96IO96Kej5Yazc3PmjIflrprovpPlh7ror63oqIDvvJrnsqTor61zc+i+k+WHuu+8muS/guWRgO+8jOWUlOWQjOWYheWVj+mhjOmAmuW4uOmDveacieWUlOWQjOWYheino+axuuaWueazle+8jOWwseWlveS8vOacieWVsuWNoeWPr+S7peW5q+S9oOino+axuuWUlOWQjOWYhemcgOaxguWSgeOAguS9oOacieWSqeWFt+mrlOWYheWVj+mhjOaDs+ino+axuu+8nw=="}}




- 20250510
编译tts-proxy工程，定位解决sudo报错问题；
编译kd-unimrcp工程，排查解决libtool: link:报错问题；
定位mrcp服务启动加载tts-proxy和asr-proxy插件报错问题
基于ubuntu搭建asr-proxy开发环境



Making all in plugins
make[1]: Entering directory `/test_asr_proxy/.kd-unimrcp/unimrcp/plugins'
Making all in demo-synth
make[2]: Entering directory `/test_asr_proxy/.kd-unimrcp/unimrcp/plugins/demo-synth'
  CCLD     demosynth.la
libtool: link: CURRENT `-L../../../third_party/tts-proxy/install/lib' must be a nonnegative integer
libtool: link: `-L../../../third_party/tts-proxy/install/lib' is not valid version information
make[2]: *** [demosynth.la] Error 1
make[2]: Leaving directory `/test_asr_proxy/.kd-unimrcp/unimrcp/plugins/demo-synth'
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/test_asr_proxy/.kd-unimrcp/unimrcp/plugins'


agent:
TEN



2025-05-10 07:28:13:455023 [NOTICE] Create RTP Termination Factory 192.168.65.3:[5000,6000]
2025-05-10 07:28:13:455025 [INFO]   Register RTP Termination Factory [RTP-Factory-1]
2025-05-10 07:28:13:455028 [INFO]   Load Plugin [Demo-Synth-1] [/work/knowdee/projects/kds/kd-unimrcp/kd-unimrcp/plugin/demosynth.so]
2025-05-10 07:28:13:639446 [WARN]   Failed to Load DSO: /lib64/libstdc++.so.6: version `GLIBCXX_3.4.22' not found (required by ../lib/libMicrosoft.CognitiveServices.Speech.core.so)
2025-05-10 07:28:13:639477 [INFO]   Load Plugin [Demo-Recog-1] [/work/knowdee/projects/kds/kd-unimrcp/kd-unimrcp/plugin/demorecog.so]
2025-05-10 07:28:13:796863 [WARN]   Failed to Load DSO: /lib64/libstdc++.so.6: version `GLIBCXX_3.4.22' not found (required by ../lib/libMicrosoft.CognitiveServices.Speech.core.so)
2025-05-10 07:28:13:796893 [INFO]   Load Plugin [Demo-Verifier-1] [/work/knowdee/projects/kds/kd-unimrcp/kd-unimrcp/plugin/demoverifier.so]
2025-05-10 07:28:13:797437 [WARN]   Failed to Load DSO: /work/knowdee/projects/kds/kd-unimrcp/kd-unimrcp/plugin/demoverifier.so: cannot open shared object file: No such file or directory
2025-05-10 07:28:13:797452 [INFO]   Load Plugin [Recorder-1] [/work/knowdee/projects/kds/kd-unimrcp/kd-unimrcp/plugin/mrcprecorder.so]
2025-05-10 07:28:13:798867 [WARN]   Failed to Load DSO: /work/knowdee/projects/kds/kd-unimrcp/kd-unimrcp/plugin/mrcprecorder.so: cannot open shared object file: No such file or directory
2025-05-10 07:28:13:798905 [INFO]   Register RTP Settings [RTP-Settings-1]
2025-05-10 07:28:13:798922 [NOTICE] Create MRCPv2 Profile [uni2]
2025-05-10 07:28:13:798936 [INFO]   Register Profile [uni2]
2025-05-10 07:28:13:798945 [NOTICE] Create MRCPv1 Profile [uni1]
2025-05-10 07:28:13:798947 [INFO]   Register Profile [uni1]
2025-05-10 07:28:13:798950 [INFO]   Start Task [MRCP Server]
2025-05-10 07:28:13:799162 [INFO]   Start Task [SIP-Agent-1]
>2025-05-10 07:28:13:799851 [INFO]   Start Task [RTSP-Agent-1]
2025-05-10 07:28:13:799888 [INFO]   Start Task [MRCPv2-Agent-1]
2025-05-10 07:28:13:799921 [INFO]   Start Task [Media-Engine-1]
2025-05-10 07:28:13:802238 [NOTICE] MRCP Server Started


libtool: link: CURRENT `-L../../../third_party/tts-proxy/install/lib' must be a nonnegative integer
libtool: link: `-L../../../third_party/tts-proxy/install/lib' is not valid version information


- 20250509
修改asr-proxy代码，增加微软asr接口模块
修正优化asr-proxy cmake构建流程
调试解决asr-proxy微软asr模块编译报错问题
参会讨论颐和园PRE环境压测结论


- 20250508
调研微软asr集成方案(CLI、SDK、REST)
研究微软asr SDK集成方法
梳理asr-proxy中azureAsrInst和azureContAsrInst模块
编译调试asr-proxy微软asr模块




说明===诺谛微软azure，tts/asrkey1 :a5b7c31380b642f59a2ac7323e88ca7ckey2 :(0cp-Apim-Subscription-Key)
ASR(stt):流式websocket: wss://eastasia.stt.speech.microsoft.com/speech/universal/v2https:TTS:httos:https://eastasia,tts,speech,microsoft.com/coanitiveservices/yl或者使用 Azure的相关sdk:cognitive-services-speech-sdk
httos://eastasia,stt,speech, microsoft,com/speech/recoanition/conversation/coonitiveservices/y1?lanquade-zh-cNafommat detailed
相关文档:htos: /learn,microsoft .com/en- us/azure/ai-services/spech-service get-started-text-to-spech?tabs windows820temminalspivots=orogramning-lanouade-pvthonhtps:/learn,microsoft .com/en us/azure/ai-servicas/speech-service/get-started speech-to-text?tabs windows2ctemminal&pivots proaraming-lanoage pythor




172.70.10.210:
(base) [root@centos7 ~]# docker images|grep asr
865677308458.dkr.ecr.cn-north-1.amazonaws.com.cn/knodi_asr_proxy            xugong-uat-latest                     016884d3434c   2 months ago    391MB
kd-asr-proxy                                                                latest                                016884d3434c   2 months ago    391MB
kd-asr-proxy                                                                product3.0                            623ac0e6273d   2 months ago    391MB
kds_asr_dev                                                                 6.0                                   e7887c475204   4 months ago    2.41GB
kds_asr_dev                                                                 1.0                                   20c84e7b2bd6   4 months ago    2.23GB
harbor.knowdee.com/chatbot/knodi_asr_proxy                                  v1.0.0                                422f9bd2050d   6 months ago    297MB
865677308458.dkr.ecr.cn-north-1.amazonaws.com.cn/knodi_asr_proxy            v1.0.0                                422f9bd2050d   6 months ago    297MB
(base) [root@centos7 ~]# docker images|grep lit
lit_dev                                                                     1.10.12                               69a33fbd9725   21 hours ago    1.73GB
lit_dev                                                                     3.0                                   86e72910d7e2   7 weeks ago     14.3GB
(base) [root@centos7 ~]# docker images|grep freeswitch
freeswitch                                                                  0.1.0                                 15b27a114024   23 hours ago    811MB



- 20250507
调试新版FS运行时加载mod_unimrcp、mod_say_zh等模块
排查解决新版FS启动报错问题
手动构建新版FS docker镜像
测试新版FS 镜像启动容器运行


- 20250506
调研新版FS集成mod_unimrcp方式
搭建开发环境，源码编译安装mod_unimrcp依赖
源码编译mod_unimrcp
编写mod_unimrcp配置文件


构建unimrcp-deps-1.6.0


<configuration name="xml_curl.conf" description="cURL XML Gateway">
  <bindings>
    <binding name="example">
      <!-- Allow to bind on a particular IP for requests sent -->
      <!--<param name="bind-local" value="$${local_ip_v4}" />-->
      <!-- The url to a gateway cgi that can generate xml similar to
           what's in this file only on-the-fly (leave it commented if you dont
           need it) -->
      <!-- one or more |-delim of configuration|directory|dialplan -->
      <param name="gateway-url" value="http://192.168.6.151:20207/acl/directory/xml" bindings="directory"/>
    </binding>
  </bindings>
</configuration>


originate sofia/internal/1001@172.70.10.210 &park()

fs_cli -x "originate {caller_id_name=Test,caller_id_number=12345}sofia/internal/1010@172.70.10.210 &park()"

fs_cli -x "originate {caller_id_name=Test,caller_id_number=12345}sofia/internal/1001@172.70.10.210 &park()"

fs_cli -x "originate {caller_id_name=Test,caller_id_number=12345}sofia/internal/1001@192.168.1.100 &park()"

### freeswitch 1.10.12 run
freeswitch@centos7> sofia status
                     Name	   Type	                                      Data	State
=================================================================================================
            external-ipv6	profile	                  sip:mod_sofia@[::1]:5080	RUNNING (0)
            172.70.10.210	  alias	                                  internal	ALIASED
                 external	profile	         sip:mod_sofia@210.14.142.130:5080	RUNNING (0)
    external::example.com	gateway	                   sip:joeuser@example.com	NOREG
            internal-ipv6	profile	                  sip:mod_sofia@[::1]:5060	RUNNING (0)
                 internal	profile	         sip:mod_sofia@210.14.142.130:5060	RUNNING (0)
=================================================================================================
4 profiles 1 alias




freeswitch@7f9b168d1065> sofia status
                     Name	   Type	                                      Data	State
=================================================================================================
            external-ipv6	profile	                  sip:mod_sofia@[::1]:5080	RUNNING (0)
               172.17.0.2	  alias	                                  internal	ALIASED
                 external	profile	         sip:mod_sofia@210.14.142.130:5080	RUNNING (0)
    external::example.com	gateway	                   sip:joeuser@example.com	NOREG
            internal-ipv6	profile	                  sip:mod_sofia@[::1]:5060	RUNNING (0)
                 internal	profile	         sip:mod_sofia@210.14.142.130:5060	RUNNING (0)
=================================================================================================
freeswitch@7f9b168d1065> sofia status
                     Name	   Type	                                      Data	State
=================================================================================================
            external-ipv6	profile	                  sip:mod_sofia@[::1]:5080	RUNNING (0)
               172.17.0.2	  alias	                                  internal	ALIASED
                 external	profile	         sip:mod_sofia@210.14.142.130:5080	RUNNING (0)
    external::example.com	gateway	                   sip:joeuser@example.com	NOREG
            internal-ipv6	profile	                  sip:mod_sofia@[::1]:5060	RUNNING (0)
                 internal	profile	         sip:mod_sofia@210.14.142.130:5060	RUNNING (0)
=================================================================================================
4 profiles 1 alias



root@7f9b168d1065:/usr/local/freeswitch/bin# grep "210.14.142.130" ../log/freeswitch.log
2025-05-07 03:11:01.065807 0.00% [DEBUG] sofia.c:4727 ext-rtp-ip [210.14.142.130]
2025-05-07 03:11:01.065811 0.00% [DEBUG] sofia.c:4727 ext-sip-ip [210.14.142.130]
2025-05-07 03:11:01.066888 0.00% [DEBUG] sofia.c:4727 ext-rtp-ip [210.14.142.130]
2025-05-07 03:11:01.066894 0.00% [DEBUG] sofia.c:4727 ext-sip-ip [210.14.142.130]


root@7f9b168d1065:/usr/local/freeswitch/bin# grep "172.17.0.2" ../log/freeswitch.log
2025-05-07 03:11:01.065799 0.00% [DEBUG] sofia.c:4727 rtp-ip [172.17.0.2]
2025-05-07 03:11:01.065803 0.00% [DEBUG] sofia.c:4727 sip-ip [172.17.0.2]
2025-05-07 03:11:01.066341 0.00% [DEBUG] sofia.c:4727 force-register-domain [172.17.0.2]
2025-05-07 03:11:01.066346 0.00% [DEBUG] sofia.c:4727 force-register-db-domain [172.17.0.2]
2025-05-07 03:11:01.066664 0.00% [DEBUG] sofia.c:4727 rtp-ip [172.17.0.2]
2025-05-07 03:11:01.066669 0.00% [DEBUG] sofia.c:4727 sip-ip [172.17.0.2]
2025-05-07 03:11:01.066755 0.00% [DEBUG] sofia.c:4727 presence-hosts [172.17.0.2,172.17.0.2]
2025-05-07 03:11:01.066956 0.00% [DEBUG] sofia.c:4727 force-register-domain [172.17.0.2]
2025-05-07 03:11:01.066972 0.00% [DEBUG] sofia.c:4727 force-subscription-domain [172.17.0.2]
2025-05-07 03:11:01.066976 0.00% [DEBUG] sofia.c:4727 force-register-db-domain [172.17.0.2]
2025-05-07 03:11:01.093059 0.00% [NOTICE] sofia.c:4235 Adding Alias [172.17.0.2] for profile [internal]
2025-05-07 03:11:02.575493 0.00% [DEBUG] mod_verto.c:5345 default-v4 Bound to 172.17.0.2:8081
2025-05-07 03:11:02.575500 0.00% [DEBUG] mod_verto.c:5345 default-v4 Bound to 172.17.0.2:8082
2025-05-07 03:11:03.111348 0.00% [INFO] mod_fifo.c:4647 cool_fifo@172.17.0.2 configured
2025-05-07 03:11:03.266997 0.00% [DEBUG] mod_unimrcp.c:4394 Loading Param server-ip:172.17.0.2
2025-05-07 03:11:03.267068 0.00% [NOTICE] mrcp_sofiasip_client_agent.c:107 () Create SofiaSIP Agent [unimrcpserver-mrcp-v2] [1.12.11-239-g54ef3e2] sip:172.17.0.2:5090;transport=udp
2025-05-07 03:11:03.267084 0.00% [NOTICE] mpf_rtp_termination_factory.c:197 () Create RTP Termination Factory 172.17.0.2:[3000,5000]
2025-05-07 03:11:03.270083 100.00% [DEBUG] mod_event_socket.c:2982 Socket up listening on 172.17.0.2:8021
2025-05-07 03:11:03.270539 100.00% [NOTICE] switch_core.c:1546 Adding 172.17.0.2/255.255.0.0 (deny) to list nat.auto
2025-05-07 03:11:03.270565 100.00% [NOTICE] switch_core.c:1566 Adding 172.17.0.2/255.255.0.0 (allow) to list localnet.auto
2025-05-07 03:11:03.270629 100.00% [NOTICE] switch_utils.c:665 Adding 192.0.2.0/24 (allow) [brian@172.17.0.2] to list domains



### freeswitch 1.10.5
[root@SC-prod-vm-yhy151 bin]# ldd freeswitch
	linux-vdso.so.1 =>  (0x00007ffcd3163000)
	libodbc.so.2 => /usr/local/freeswitch/lib/libodbc.so.2 (0x00007f298ed8a000)
	libfreeswitch.so.1 => /usr/local/freeswitch/lib/libfreeswitch.so.1 (0x00007f298e714000)
	libpq.so.5 => /usr/local/freeswitch/lib/libpq.so.5 (0x00007f298e4e5000)
	libsqlite3.so.0 => /lib64/libsqlite3.so.0 (0x00007f298e230000)
	libcurl.so.4 => /lib64/libcurl.so.4 (0x00007f298dfc6000)
	libpcre.so.1 => /lib64/libpcre.so.1 (0x00007f298dd64000)
	libspeex.so.1 => /usr/local/freeswitch/lib/libspeex.so.1 (0x00007f298db4b000)
	libspeexdsp.so.1 => /usr/local/freeswitch/lib/libspeexdsp.so.1 (0x00007f298d938000)
	libedit.so.0 => /usr/local/freeswitch/lib/libedit.so.0 (0x00007f298d6fb000)
	libtinfo.so.5 => /lib64/libtinfo.so.5 (0x00007f298d4d1000)
	libspandsp.so.3 => /usr/local/freeswitch/lib/libspandsp.so.3 (0x00007f298d1c1000)
	libm.so.6 => /lib64/libm.so.6 (0x00007f298cebf000)
	libtiff.so.5 => /usr/local/freeswitch/lib/libtiff.so.5 (0x00007f298cc4b000)
	libjpeg.so.62 => /usr/local/freeswitch/lib/libjpeg.so.62 (0x00007f298c9f6000)
	libsofia-sip-ua.so.0 => /usr/local/freeswitch/lib/libsofia-sip-ua.so.0 (0x00007f298c619000)
	libz.so.1 => /lib64/libz.so.1 (0x00007f298c403000)
	libuuid.so.1 => /lib64/libuuid.so.1 (0x00007f298c1fe000)
	librt.so.1 => /lib64/librt.so.1 (0x00007f298bff6000)
	libdl.so.2 => /lib64/libdl.so.2 (0x00007f298bdf2000)
	libcrypt.so.1 => /lib64/libcrypt.so.1 (0x00007f298bbbb000)
	libpthread.so.0 => /lib64/libpthread.so.0 (0x00007f298b99f000)
	libssl.so.10 => /lib64/libssl.so.10 (0x00007f298b72d000)
	libcrypto.so.10 => /lib64/libcrypto.so.10 (0x00007f298b2ca000)
	libc.so.6 => /lib64/libc.so.6 (0x00007f298aefc000)
	libltdl.so.7 => /usr/local/freeswitch/lib/libltdl.so.7 (0x00007f298acf2000)
	libstdc++.so.6 => /lib64/libstdc++.so.6 (0x00007f298a9ea000)
	libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00007f298a7d4000)
	libkrb5.so.3 => /lib64/libkrb5.so.3 (0x00007f298a4eb000)
	libcom_err.so.2 => /lib64/libcom_err.so.2 (0x00007f298a2e7000)
	libgssapi_krb5.so.2 => /lib64/libgssapi_krb5.so.2 (0x00007f298a09a000)
	libldap_r-2.4.so.2 => /lib64/libldap_r-2.4.so.2 (0x00007f2989e3b000)
	libidn.so.11 => /lib64/libidn.so.11 (0x00007f2989c08000)
	libssh2.so.1 => /lib64/libssh2.so.1 (0x00007f29899db000)
	libssl3.so => /lib64/libssl3.so (0x00007f298977e000)
	libsmime3.so => /lib64/libsmime3.so (0x00007f2989556000)
	libnss3.so => /lib64/libnss3.so (0x00007f2989222000)
	libnssutil3.so => /lib64/libnssutil3.so (0x00007f2988ff2000)
	libplds4.so => /lib64/libplds4.so (0x00007f2988dee000)
	libplc4.so => /lib64/libplc4.so (0x00007f2988be9000)
	libnspr4.so => /lib64/libnspr4.so (0x00007f29889ab000)
	libk5crypto.so.3 => /lib64/libk5crypto.so.3 (0x00007f2988778000)
	liblber-2.4.so.2 => /lib64/liblber-2.4.so.2 (0x00007f2988569000)
	libldap-2.4.so.2 => /lib64/libldap-2.4.so.2 (0x00007f2988314000)
	/lib64/ld-linux-x86-64.so.2 (0x00007f298eff2000)
	libjbig.so.2.0 => /usr/local/freeswitch/lib/libjbig.so.2.0 (0x00007f2988108000)
	libfreebl3.so => /lib64/libfreebl3.so (0x00007f2987f05000)
	libkrb5support.so.0 => /lib64/libkrb5support.so.0 (0x00007f2987cf5000)
	libkeyutils.so.1 => /lib64/libkeyutils.so.1 (0x00007f2987af1000)
	libresolv.so.2 => /lib64/libresolv.so.2 (0x00007f29878d7000)
	libsasl2.so.3 => /lib64/libsasl2.so.3 (0x00007f29876ba000)
	libselinux.so.1 => /lib64/libselinux.so.1 (0x00007f2987493000)
[root@SC-prod-vm-yhy151 freeswitch]# ll lib/lib*.so
-rwxr-xr-x 1 root root  235064 Oct 13  2023 lib/libedit.so
lrwxrwxrwx 1 root root      22 Oct 13  2023 lib/libfreeswitch.so -> libfreeswitch.so.1.0.0
-rwxr-xr-x 1 root root  285328 Oct 13  2023 lib/libjpeg.so
-rwxr-xr-x 1 root root  429736 Oct 13  2023 lib/libodbc.so
-rwxr-xr-x 1 root root   44816 Oct 13  2023 lib/libodbccr.so
-rwxr-xr-x 1 root root    7032 Oct 13  2023 lib/libodbcdrvcfg1S.so
-rwxr-xr-x 1 root root    6944 Oct 13  2023 lib/libodbcdrvcfg2S.so
-rwxr-xr-x 1 root root   74640 Oct 13  2023 lib/libodbcinst.so
-rwxr-xr-x 1 root root    7040 Oct 13  2023 lib/libodbcminiS.so
-rwxr-xr-x 1 root root   11168 Oct 13  2023 lib/libodbcmyS.so
-rwxr-xr-x 1 root root    7040 Oct 13  2023 lib/libodbcnnS.so
-rwxr-xr-x 1 root root   11216 Oct 13  2023 lib/libodbcpsqlS.so
-rwxr-xr-x 1 root root   11176 Oct 13  2023 lib/libodbctxtS.so
-rwxr-xr-x 1 root root   28360 Oct 13  2023 lib/libogg.so
-rwxr-xr-x 1 root root  197552 Oct 13  2023 lib/libpq.so
-rwxr-xr-x 1 root root  378880 Oct 13  2023 lib/libsndfile.so
-rwxr-xr-x 1 root root 1224600 Oct 13  2023 lib/libspandsp.so
-rwxr-xr-x 1 root root  102832 Oct 13  2023 lib/libspeex.so
-rwxr-xr-x 1 root root   79192 Oct 13  2023 lib/libspeexdsp.so
-rwxr-xr-x 1 root root  479456 Oct 13  2023 lib/libtiff.so
-rwxr-xr-x 1 root root   11424 Oct 13  2023 lib/libtiffxx.so
-rwxr-xr-x 1 root root  185280 Oct 13  2023 lib/libvorbis.so
-rwxr-xr-x 1 root root 2944200 Oct 13  2023 lib/libvorbisenc.so
[root@SC-prod-vm-yhy151 freeswitch]# ll mod/mod_*
-rwxr-xr-x 1 root root    1291 Oct 13  2023 mod/mod_amr.la
-rwxr-xr-x 1 root root   62272 Oct 13  2023 mod/mod_amr.so
-rwxr-xr-x 1 root root    1291 Oct 13  2023 mod/mod_b64.la
-rwxr-xr-x 1 root root   63000 Oct 13  2023 mod/mod_b64.so
-rwxr-xr-x 1 root root    1315 Oct 13  2023 mod/mod_cdr_csv.la
-rwxr-xr-x 1 root root   89032 Oct 13  2023 mod/mod_cdr_csv.so
-rwxr-xr-x 1 root root    1333 Oct 13  2023 mod/mod_cdr_sqlite.la
-rwxr-xr-x 1 root root   71768 Oct 13  2023 mod/mod_cdr_sqlite.so
-rwxr-xr-x 1 root root    1321 Oct 13  2023 mod/mod_commands.la
-rwxr-xr-x 1 root root  598584 Oct 13  2023 mod/mod_commands.so
-rwxr-xr-x 1 root root  599440 Oct 13  2023 mod/mod_commands.so.old
-rwxr-xr-x 1 root root  597760 Oct 13  2023 mod/mod_commands.so_bak
-rwxr-xr-x 1 root root    1333 Oct 13  2023 mod/mod_conference.la
-rwxr-xr-x 1 root root 1536528 Oct 13  2023 mod/mod_conference.so
-rwxr-xr-x 1 root root    1315 Oct 13  2023 mod/mod_console.la
-rwxr-xr-x 1 root root   85984 Oct 13  2023 mod/mod_console.so
-rwxr-xr-x 1 root root    1285 Oct 13  2023 mod/mod_db.la
-rwxr-xr-x 1 root root   95384 Oct 13  2023 mod/mod_db.so
-rwxr-xr-x 1 root root    1375 Oct 13  2023 mod/mod_dialplan_asterisk.la
-rwxr-xr-x 1 root root   77792 Oct 13  2023 mod/mod_dialplan_asterisk.so
-rwxr-xr-x 1 root root    1345 Oct 13  2023 mod/mod_dialplan_xml.la
-rwxr-xr-x 1 root root  115328 Oct 13  2023 mod/mod_dialplan_xml.so
-rwxr-xr-x 1 root root    1315 Oct 13  2023 mod/mod_dptools.la
-rwxr-xr-x 1 root root  526776 Oct 13  2023 mod/mod_dptools.so
-rwxr-xr-x 1 root root    1304 Oct 13  2023 mod/mod_enum.la
-rwxr-xr-x 1 root root  118744 Oct 13  2023 mod/mod_enum.so
-rwxr-xr-x 1 root root    1291 Oct 13  2023 mod/mod_esf.la
-rwxr-xr-x 1 root root   84208 Oct 13  2023 mod/mod_esf.so
-rwxr-xr-x 1 root root    1345 Oct 13  2023 mod/mod_event_socket.la
-rwxr-xr-x 1 root root  225792 Oct 13  2023 mod/mod_event_socket.so
-rwxr-xr-x 1 root root    1297 Oct 13  2023 mod/mod_expr.la
-rwxr-xr-x 1 root root  163480 Oct 13  2023 mod/mod_expr.so
-rwxr-xr-x 1 root root    1297 Oct 13  2023 mod/mod_fifo.la
-rwxr-xr-x 1 root root  342928 Oct 13  2023 mod/mod_fifo.so
-rwxr-xr-x 1 root root    1291 Oct 13  2023 mod/mod_fsv.la
-rwxr-xr-x 1 root root  115368 Oct 13  2023 mod/mod_fsv.so
-rwxr-xr-x 1 root root    1309 Oct 13  2023 mod/mod_g723_1.la
-rwxr-xr-x 1 root root   60448 Oct 13  2023 mod/mod_g723_1.so
-rwxr-xr-x 1 root root    1297 Oct 13  2023 mod/mod_g729.la
-rwxr-xr-x 1 root root   59960 Oct 13  2023 mod/mod_g729.so
-rwxr-xr-x 1 root root    1297 Oct 13  2023 mod/mod_h26x.la
-rwxr-xr-x 1 root root   63560 Oct 13  2023 mod/mod_h26x.so
-rwxr-xr-x 1 root root    1297 Oct 13  2023 mod/mod_hash.la
-rwxr-xr-x 1 root root  262232 Oct 13  2023 mod/mod_hash.so
-rwxr-xr-x 1 root root    1309 Oct 13  2023 mod/mod_httapi.la
-rwxr-xr-x 1 root root  307984 Oct 13  2023 mod/mod_httapi.so
-rwxr-xr-x 1 root root    1293 Oct 13  2023 mod/mod_java.la
-rwxr-xr-x 1 root root  524936 Oct 13  2023 mod/mod_java.so
-rwxr-xr-x 1 root root    1345 Oct 13  2023 mod/mod_local_stream.la
-rwxr-xr-x 1 root root  136816 Oct 13  2023 mod/mod_local_stream.so
-rwxr-xr-x 1 root root    1315 Oct 13  2023 mod/mod_logfile.la
-rwxr-xr-x 1 root root   87848 Oct 13  2023 mod/mod_logfile.so
-rwxr-xr-x 1 root root    1321 Oct 13  2023 mod/mod_loopback.la
-rwxr-xr-x 1 root root  177680 Oct 13  2023 mod/mod_loopback.so
-rwxr-xr-x 1 root root    1293 Oct 13  2023 mod/mod_lua.la
-rwxr-xr-x 1 root root  798768 Oct 13  2023 mod/mod_lua.so
-rwxr-xr-x 1 root root    1339 Oct 13  2023 mod/mod_native_file.la
-rwxr-xr-x 1 root root   61200 Oct 13  2023 mod/mod_native_file.so
-rwxr-xr-x 1 root root    1316 Oct 13  2023 mod/mod_pgsql.la
-rwxr-xr-x 1 root root  100864 Oct 13  2023 mod/mod_pgsql.so
-rwxr-xr-x 1 root root    1291 Oct 13  2023 mod/mod_png.la
-rwxr-xr-x 1 root root   82144 Oct 13  2023 mod/mod_png.so
-rwxr-xr-x 1 root root    1291 Oct 13  2023 mod/mod_rtc.la
-rwxr-xr-x 1 root root   85728 Oct 13  2023 mod/mod_rtc.so
-rwxr-xr-x 1 root root    1309 Oct 13  2023 mod/mod_say_en.la
-rwxr-xr-x 1 root root   95984 Oct 13  2023 mod/mod_say_en.so
-rwxr-xr-x 1 root root    1309 Oct 13  2023 mod/mod_skinny.la
-rwxr-xr-x 1 root root  677720 Oct 13  2023 mod/mod_skinny.so
-rwxr-xr-x 1 root root    1291 Oct 13  2023 mod/mod_sms.la
-rwxr-xr-x 1 root root  103664 Oct 13  2023 mod/mod_sms.so
-rwxr-xr-x 1 root root    1325 Oct 13  2023 mod/mod_sndfile.la
-rwxr-xr-x 1 root root   97720 Oct 13  2023 mod/mod_sndfile.so
-rwxr-xr-x 1 root root    1303 Oct 13  2023 mod/mod_sofia.la
-rwxr-xr-x 1 root root 2481248 Oct 13  2023 mod/mod_sofia.so
-rwxr-xr-x 1 root root    1315 Oct 13  2023 mod/mod_spandsp.la
-rwxr-xr-x 1 root root  631520 Oct 13  2023 mod/mod_spandsp.so
-rwxr-xr-x 1 root root    1309 Oct 13  2023 mod/mod_syslog.la
-rwxr-xr-x 1 root root   63816 Oct 13  2023 mod/mod_syslog.so
-rwxr-xr-x 1 root root    1339 Oct 13  2023 mod/mod_tone_stream.la
-rwxr-xr-x 1 root root   64136 Oct 13  2023 mod/mod_tone_stream.so
lrwxrwxrwx 1 root root      17 Oct 13  2023 mod/mod_unimrcp.la -> ../mod_unimrcp.la
-rw-r--r-- 1 root root    1400 Oct 13  2023 mod/mod_unimrcp.lai
-rwxr-xr-x 1 root root 2074136 Oct 13  2023 mod/mod_unimrcp.so
-rw-r--r-- 1 root root  482016 Oct 13  2023 mod/mod_unimrcp_la-mod_unimrcp.o
-rwxr-xr-x 1 root root    1351 Oct 13  2023 mod/mod_valet_parking.la
-rwxr-xr-x 1 root root  116000 Oct 13  2023 mod/mod_valet_parking.so
-rwxr-xr-x 1 root root    1303 Oct 13  2023 mod/mod_verto.la
-rwxr-xr-x 1 root root  529272 Oct 13  2023 mod/mod_verto.so
-rwxr-xr-x 1 root root    1327 Oct 13  2023 mod/mod_voicemail.la
-rwxr-xr-x 1 root root  464632 Oct 13  2023 mod/mod_voicemail.so
-rwxr-xr-x 1 root root    1315 Oct 13  2023 mod/mod_xml_cdr.la
-rwxr-xr-x 1 root root  115832 Oct 13  2023 mod/mod_xml_cdr.so
-rwxr-xr-x 1 root root    1321 Oct 13  2023 mod/mod_xml_curl.la
-rwxr-xr-x 1 root root  106744 Oct 13  2023 mod/mod_xml_curl.so
-rwxr-xr-x 1 root root    1315 Oct 13  2023 mod/mod_xml_rpc.la
-rwxr-xr-x 1 root root 1642536 Oct 13  2023 mod/mod_xml_rpc.so
-rwxr-xr-x 1 root root    1321 Oct 13  2023 mod/mod_xml_scgi.la
-rwxr-xr-x 1 root root  108944 Oct 13  2023 mod/mod_xml_scgi.so

### mod_unimrcp:
Makefile:847: *** You must install libunimrcp and libunimrcp-dev to build this module.  Stop.
----------------------------------------------------------------------
Libraries have been installed in:
   /usr/local/freeswitch/mod

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
make[1]: Leaving directory '/usr/src/freeswitch/src/mod/asr_tts/mod_unimrcp'






###　unimrcp and it`s deps:
****************************** REPORT ******************************

UniMRCP version............... : 1.8.0

APR version................... : 1.5.2
APR-util version.............. : 1.5.4
Sofia-SIP version............. : 1.12.11-239-g54ef3e2

Compiler...................... : gcc
Compiler flags................ : -g -O2 -pthread
Preprocessor definitions...... : -DLINUX -D_REENTRANT -D_GNU_SOURCE
Linker flags.................. :

UniMRCP client lib............ : no
Sample UniMRCP client app..... : no
Sample UMC C++ client app..... : no
Misc ASR client lib and app... : yes

UniMRCP server lib............ : yes
UniMRCP server app............ : yes

Demo synthesizer plugin....... : yes
Demo recognizer plugin........ : yes
Demo verifier plugin.......... : no
Recorder plugin............... : no

Installation layout........... : classic
Installation directory........ : /usr/local/unimrcp

********************************************************************

****************************** REPORT ******************************

UniMRCP version............... : 1.8.0

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
Demo verifier plugin.......... : no
Recorder plugin............... : no

Installation layout........... : classic
Installation directory........ : /usr/local/unimrcp

********************************************************************


----------------------------------------------------------------------
Libraries have been installed in:
   /usr/local/unimrcp/plugin

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
make[3]: Leaving directory '/usr/src/unimrcp/plugins/demo-synth'
make[2]: Leaving directory '/usr/src/unimrcp/plugins/demo-synth'
Making install in demo-recog
make[2]: Entering directory '/usr/src/unimrcp/plugins/demo-recog'
make[3]: Entering directory '/usr/src/unimrcp/plugins/demo-recog'
make[3]: Nothing to be done for 'install-exec-am'.
 /bin/mkdir -p '/usr/local/unimrcp/plugin'
 /bin/bash ../../libtool   --mode=install /usr/bin/install -c   demorecog.la '/usr/local/unimrcp/plugin'
libtool: install: /usr/bin/install -c .libs/demorecog.so.0.8.0 /usr/local/unimrcp/plugin/demorecog.so.0.8.0
libtool: install: (cd /usr/local/unimrcp/plugin && { ln -s -f demorecog.so.0.8.0 demorecog.so.0 || { rm -f demorecog.so.0 && ln -s demorecog.so.0.8.0 demorecog.so.0; }; })
libtool: install: (cd /usr/local/unimrcp/plugin && { ln -s -f demorecog.so.0.8.0 demorecog.so || { rm -f demorecog.so && ln -s demorecog.so.0.8.0 demorecog.so; }; })
libtool: install: /usr/bin/install -c .libs/demorecog.lai /usr/local/unimrcp/plugin/demorecog.la
libtool: install: /usr/bin/install -c .libs/demorecog.a /usr/local/unimrcp/plugin/demorecog.a
libtool: install: chmod 644 /usr/local/unimrcp/plugin/demorecog.a
libtool: install: ranlib /usr/local/unimrcp/plugin/demorecog.a
libtool: finish: PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/sbin" ldconfig -n /usr/local/unimrcp/plugin
----------------------------------------------------------------------
Libraries have been installed in:
   /usr/local/unimrcp/plugin

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
make[3]: Leaving directory '/usr/src/unimrcp/plugins/demo-recog'
make[2]: Leaving directory '/usr/src/unimrcp/plugins/demo-recog'
make[2]: Entering directory '/usr/src/unimrcp/plugins'
make[3]: Entering directory '/usr/src/unimrcp/plugins'
make[3]: Nothing to be done for 'install-exec-am'.
make[3]: Nothing to be done for 'install-data-am'.
make[3]: Leaving directory '/usr/src/unimrcp/plugins'
make[2]: Leaving directory '/usr/src/unimrcp/plugins'
make[1]: Leaving directory '/usr/src/unimrcp/plugins'
Making install in platforms
make[1]: Entering directory '/usr/src/unimrcp/platforms'
Making install in libunimrcp-server
make[2]: Entering directory '/usr/src/unimrcp/platforms/libunimrcp-server'
make[3]: Entering directory '/usr/src/unimrcp/platforms/libunimrcp-server'
 /bin/mkdir -p '/usr/local/unimrcp/lib'
 /bin/bash ../../libtool   --mode=install /usr/bin/install -c   libunimrcpserver.la '/usr/local/unimrcp/lib'
libtool: install: /usr/bin/install -c .libs/libunimrcpserver.so.0.8.0 /usr/local/unimrcp/lib/libunimrcpserver.so.0.8.0
libtool: install: (cd /usr/local/unimrcp/lib && { ln -s -f libunimrcpserver.so.0.8.0 libunimrcpserver.so.0 || { rm -f libunimrcpserver.so.0 && ln -s libunimrcpserver.so.0.8.0 libunimrcpserver.so.0; }; })
libtool: install: (cd /usr/local/unimrcp/lib && { ln -s -f libunimrcpserver.so.0.8.0 libunimrcpserver.so || { rm -f libunimrcpserver.so && ln -s libunimrcpserver.so.0.8.0 libunimrcpserver.so; }; })
libtool: install: /usr/bin/install -c .libs/libunimrcpserver.lai /usr/local/unimrcp/lib/libunimrcpserver.la
libtool: install: /usr/bin/install -c .libs/libunimrcpserver.a /usr/local/unimrcp/lib/libunimrcpserver.a
libtool: install: chmod 644 /usr/local/unimrcp/lib/libunimrcpserver.a
libtool: install: ranlib /usr/local/unimrcp/lib/libunimrcpserver.a
libtool: finish: PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/sbin" ldconfig -n /usr/local/unimrcp/lib
----------------------------------------------------------------------
Libraries have been installed in:
   /usr/local/unimrcp/lib

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
 /bin/mkdir -p '/usr/local/unimrcp/include'
 /usr/bin/install -c -m 644 include/unimrcp_server.h '/usr/local/unimrcp/include'
make[3]: Leaving directory '/usr/src/unimrcp/platforms/libunimrcp-server'
make[2]: Leaving directory '/usr/src/unimrcp/platforms/libunimrcp-server'
Making install in unimrcp-server
make[2]: Entering directory '/usr/src/unimrcp/platforms/unimrcp-server'
make[3]: Entering directory '/usr/src/unimrcp/platforms/unimrcp-server'
 /bin/mkdir -p '/usr/local/unimrcp/bin'
  /bin/bash ../../libtool   --mode=install /usr/bin/install -c unimrcpserver '/usr/local/unimrcp/bin'
libtool: install: /usr/bin/install -c .libs/unimrcpserver /usr/local/unimrcp/bin/unimrcpserver
make[3]: Nothing to be done for 'install-data-am'.
make[3]: Leaving directory '/usr/src/unimrcp/platforms/unimrcp-server'
make[2]: Leaving directory '/usr/src/unimrcp/platforms/unimrcp-server'
make[2]: Entering directory '/usr/src/unimrcp/platforms'
make[3]: Entering directory '/usr/src/unimrcp/platforms'
make[3]: Nothing to be done for 'install-exec-am'.
make[3]: Nothing to be done for 'install-data-am'.
make[3]: Leaving directory '/usr/src/unimrcp/platforms'
make[2]: Leaving directory '/usr/src/unimrcp/platforms'
make[1]: Leaving directory '/usr/src/unimrcp/platforms'
make[1]: Entering directory '/usr/src/unimrcp'
make[2]: Entering directory '/usr/src/unimrcp'
make[2]: Nothing to be done for 'install-exec-am'.
test -d /usr/local/unimrcp/log || /bin/bash /usr/src/unimrcp/build/install-sh -d /usr/local/unimrcp/log
test -d /usr/local/unimrcp/var || /bin/bash /usr/src/unimrcp/build/install-sh -d /usr/local/unimrcp/var
make[2]: Leaving directory '/usr/src/unimrcp'
make[1]: Leaving directory '/usr/src/unimrcp'



### unimrcp-deps-1.6.0 install：

----------------------------------------------------------------------
Libraries have been installed in:
   /usr/local/unimrcp-deps/lib

If you ever happen to want to link against installed libraries
in a given directory, LIBDIR, you must either use libtool, and
specify the full pathname of the library, or use the `-LLIBDIR'
flag during linking and do at least one of the following:
   - add LIBDIR to the `LD_LIBRARY_PATH' environment variable
     during execution
   - add LIBDIR to the `LD_RUN_PATH' environment variable
     during linking
   - use the `-Wl,-rpath -Wl,LIBDIR' linker flag
   - have your system administrator add LIBDIR to `/etc/ld.so.conf'

See any operating system documentation about shared libraries for
more information, such as the ld(1) and ld.so(8) manual pages.
----------------------------------------------------------------------
make[3]: Nothing to be done for 'install-data-am'.
make[3]: Leaving directory '/usr/src/libs/unimrcp-deps-1.6.0/libs/sofia-sip/libsofia-sip-ua'
make[2]: Leaving directory '/usr/src/libs/unimrcp-deps-1.6.0/libs/sofia-sip/libsofia-sip-ua'
make[1]: Leaving directory '/usr/src/libs/unimrcp-deps-1.6.0/libs/sofia-sip/libsofia-sip-ua'
Making install in utils
make[1]: Entering directory '/usr/src/libs/unimrcp-deps-1.6.0/libs/sofia-sip/utils'
make[2]: Entering directory '/usr/src/libs/unimrcp-deps-1.6.0/libs/sofia-sip/utils'
test -z "/usr/local/unimrcp-deps/bin" || /bin/mkdir -p "/usr/local/unimrcp-deps/bin"
  /bin/bash ../libtool   --mode=install /usr/bin/install -c sip-options sip-date sip-dig '/usr/local/unimrcp-deps/bin'
libtool: install: /usr/bin/install -c .libs/sip-options /usr/local/unimrcp-deps/bin/sip-options
libtool: install: /usr/bin/install -c .libs/sip-date /usr/local/unimrcp-deps/bin/sip-date
libtool: install: /usr/bin/install -c .libs/sip-dig /usr/local/unimrcp-deps/bin/sip-dig
make[2]: Nothing to be done for 'install-data-am'.
make[2]: Leaving directory '/usr/src/libs/unimrcp-deps-1.6.0/libs/sofia-sip/utils'
make[1]: Leaving directory '/usr/src/libs/unimrcp-deps-1.6.0/libs/sofia-sip/utils'
Making install in packages
make[1]: Entering directory '/usr/src/libs/unimrcp-deps-1.6.0/libs/sofia-sip/packages'
make[2]: Entering directory '/usr/src/libs/unimrcp-deps-1.6.0/libs/sofia-sip/packages'
make[2]: Nothing to be done for 'install-exec-am'.
test -z "/usr/local/unimrcp-deps/lib/pkgconfig" || /bin/mkdir -p "/usr/local/unimrcp-deps/lib/pkgconfig"
 /usr/bin/install -c -m 644 sofia-sip-ua.pc '/usr/local/unimrcp-deps/lib/pkgconfig'
make[2]: Leaving directory '/usr/src/libs/unimrcp-deps-1.6.0/libs/sofia-sip/packages'
make[1]: Leaving directory '/usr/src/libs/unimrcp-deps-1.6.0/libs/sofia-sip/packages'
Making install in tests
make[1]: Entering directory '/usr/src/libs/unimrcp-deps-1.6.0/libs/sofia-sip/tests'
make[2]: Entering directory '/usr/src/libs/unimrcp-deps-1.6.0/libs/sofia-sip/tests'
make[2]: Nothing to be done for 'install-exec-am'.
make[2]: Nothing to be done for 'install-data-am'.
make[2]: Leaving directory '/usr/src/libs/unimrcp-deps-1.6.0/libs/sofia-sip/tests'
make[1]: Leaving directory '/usr/src/libs/unimrcp-deps-1.6.0/libs/sofia-sip/tests'
make[1]: Entering directory '/usr/src/libs/unimrcp-deps-1.6.0/libs/sofia-sip'
mkdir -p man man/man1 2> /dev/null
touch man/man1/sip-date.1 man/man1/sip-options.1 man/man1/localinfo.1 man/man1/addrinfo.1 man/man1/stunc.1 man/man1/sip-dig.1
make[2]: Entering directory '/usr/src/libs/unimrcp-deps-1.6.0/libs/sofia-sip'
make[2]: Nothing to be done for 'install-exec-am'.
mkdir -p man man/man1 2> /dev/null
touch man/man1/sip-date.1 man/man1/sip-options.1 man/man1/localinfo.1 man/man1/addrinfo.1 man/man1/stunc.1 man/man1/sip-dig.1
test -z "/usr/local/unimrcp-deps/share/man/man1" || /bin/mkdir -p "/usr/local/unimrcp-deps/share/man/man1"
 /usr/bin/install -c -m 644 man/man1/sip-date.1 man/man1/sip-options.1 man/man1/localinfo.1 man/man1/addrinfo.1 man/man1/stunc.1 man/man1/sip-dig.1 '/usr/local/unimrcp-deps/share/man/man1'
make[2]: Leaving directory '/usr/src/libs/unimrcp-deps-1.6.0/libs/sofia-sip'
make[1]: Leaving directory '/usr/src/libs/unimrcp-deps-1.6.0/libs/sofia-sip'




- 20250430
开发sysfunc设置主音量、背景图片功能
开发sysfunc设置透明度、字体大小功能
开发sysfunc设置屏保等待时间、打开本地类应用功能
编译调试action模块和ukui manager模块


- 20250429
开发sysfunc打开我的电脑、我的文档、我的图片功能
开发sysfunc打开我的音乐、我的视频、我的下载功能
开发sysfunc设置显示器关闭时间功能
开发sysfunc设置系统进入睡眠时间功能


- 20250428
开发sysfunc修改用户密码、用户头像、密码时效、免密自动登录、查询配置信息功能
开发sysfunc同步网络时间、设置手动更改时间、设置手动更改时区功能
开发sysfunc设置自定义时间服务器、添加其它时区时间、货币格式功能
开发sysfunc切换农历或公历、切换一周的第一天、修改日期格式、切换12或24时制度功能




查看并分析颐和园线上环境今天上午播报无声问题(20分钟内fs崩溃2次，手动重启2次)
- 20250427
开发sysfunc设置提示音开关、音效主题、特效模式功能
开发sysfunc切换系统主题、窗口外观、系统图标、系统光标功能
开发sysfunc设置打印机、锁屏壁纸、字体类型、屏保、锁屏功能
开发sysfunc设置有线网络、显示可用网络、WIFI开关功能


- 20250425
开发sysfunc设置开机自启动、快捷键、休眠唤醒提示音功能
开发sysfunc设置开/关机音乐、输入、输出设备功能




- 20250424
开发sysfunc设置分辨率、亮度、屏幕方向功能
开发sysfunc设置主屏幕、镜像屏幕、刷新率功能
开发sysfunc设置打开或关闭显示器屏幕功能
开发sysfunc设置屏幕缩放、夜间模式功能


- 20250423
参会需求工程会议
排查解决编译时declare无效和运行时sqlite3依赖缺失问题
编写语义路由流程的测试程序
搭建流程测试环境，调试语义路由功能


undefined symbol: sqlite3_open
调用以下代码时报错"sysfunc.cc:826:18: error: declaration does not declare anything [-fpermissive]
  826 | std::unordered_map<std::string, std::string> slots;"
            std::string intent_code;
            std::unordered_map<std::string, std::string> slots;
            kdm_sysfunc::SemanticRouter::GetInstance().Route(intent_code, slots);



- 20250422
开发sysfunc语义路由模块
开发sysfunc动作执行模块
修改sysfunc语义与动作执行映射表和意图语义结构
编译调试语义路由和动作执行模块


- 20250421
设计sysfunc语义路由模块
设计sysfunc意图语义结构
设计sysfunc动作执行模块
设计sysfunc语义与动作执行映射表


## SED ASSM

## UCIL (I:incremental)

### continual learning
 - task increased learning: task IL
 - class increased learning: class IL
 - domain increased learning: domain IL

### model archtecture for sound event detection
** independent learning
** knowledge distillation
** 无监督学习 with sample selection
** balanced memory update

### loss function: 损失函数

### evaluation metric
 - resample to 16k
 - max clip numbers



kdm_intent

sudo dpkg --remove kt-ktbrowser-stable


dpkg -s browser360-cn-stable xmind-vana
apt search browser360-cn-stable xmind-vana


deb包文件名package_name 和 .desktop文件中Name 不对应, 导致ukui search不到应用信息

KDM文档补充：Readme、design、kds.json、API文档

CacheRecorder


sysfunc.app.install 安装应用到本地接口
sysfunc.app.install_list 获取应用安装列表接口
sysfunc.app.install_clear 清除所有已完成的应用安装任务接口


feat: add recommended_install_app to sysfunc.syscall.intent

image: 865677308458.dkr.ecr.cn-north-1.amazonaws.com.cn/unimrcp:waihu-prod-latest


chunk_size = [0, 10, 5] #[0, 10, 5] 600ms, [0, 8, 4] 480ms
15  600ms
12  480ms
3  120ms
1  40ms
encoder_chunk_look_back = 4 #number of chunks to lookback for encoder self-attention
decoder_chunk_look_back = 1 #number of encoder chunks to lookback for decoder cross-attention

wss://172.70.10.210:10096

wss://127.0.0.1:10095
wss://192.168.40.93:10095
wss://172.20.224.1:10095
wss://192.168.176.1:10095




部署联调sysfunc应用管理模块installable/install
跟进沟通麒麟应用中心查询结果逻辑


编写意图体系Excel表格必要数据解析的工具程序
构建系统调用所用意图资源sqlite数据库
调研sqlite数据库三方开发框架(sqlite_orm、sqlite3pp、sqlitecpp、easysqlite、sqlSQLite++、sqlite3cc)
搭建并测试数据库开发框架sqlite_orm环境



## 设计语义功能路由
以下是一个基于 C++ 的智能交互流程接口系统的设计，涵盖了 **意图识别**、**槽位抽取**、**语义路由**、**动作执行** 和 **系统调用** 等环节。每个模块都设计为独立的类或接口，便于扩展和维护。

---

### **系统架构设计**
1. **意图识别模块**：识别用户输入的意图。
2. **槽位抽取模块**：从用户输入中提取关键参数（槽位）。
3. **语义路由模块**：根据意图和槽位信息，路由到对应的动作。
4. **动作执行模块**：执行具体的业务逻辑。
5. **系统调用模块**：与外部系统交互（如数据库、API 调用等）。

---

### **代码实现**

以下是各模块的具体实现：

#### **1. 意图识别模块**
意图识别模块负责分析用户输入并确定用户的意图。

```cpp
#pragma once
#include <string>
#include <unordered_map>

class IntentRecognizer {
public:
    // 初始化意图模型（可以加载训练好的模型或规则）
    void loadModel(const std::string& modelPath);

    // 根据用户输入识别意图
    std::string recognizeIntent(const std::string& userInput);

private:
    std::unordered_map<std::string, std::string> intentRules; // 简单规则映射
};
```

```cpp
#include "intent_recognizer.h"
#include <sstream>

void IntentRecognizer::loadModel(const std::string& modelPath) {
    // 模拟加载规则模型
    intentRules["play music"] = "PlayMusic";
    intentRules["set alarm"] = "SetAlarm";
    intentRules["weather"] = "GetWeather";
}

std::string IntentRecognizer::recognizeIntent(const std::string& userInput) {
    for (const auto& rule : intentRules) {
        if (userInput.find(rule.first) != std::string::npos) {
            return rule.second;
        }
    }
    return "UnknownIntent";
}
```

---

#### **2. 槽位抽取模块**
槽位抽取模块负责从用户输入中提取参数（如时间、地点、对象等）。

```cpp
#pragma once
#include <string>
#include <unordered_map>

class SlotExtractor {
public:
    // 抽取槽位信息
    std::unordered_map<std::string, std::string> extractSlots(const std::string& userInput);
};
```

```cpp
#include "slot_extractor.h"
#include <regex>

std::unordered_map<std::string, std::string> SlotExtractor::extractSlots(const std::string& userInput) {
    std::unordered_map<std::string, std::string> slots;

    // 示例：提取时间槽位
    std::regex timeRegex(R"((\d{1,2}:\d{2}))");
    std::smatch match;
    if (std::regex_search(userInput, match, timeRegex)) {
        slots["time"] = match.str(1);
    }

    // 示例：提取地点槽位
    std::regex locationRegex(R"(in (\w+))");
    if (std::regex_search(userInput, match, locationRegex)) {
        slots["location"] = match.str(1);
    }

    return slots;
}
```

---

#### **3. 语义路由模块**
语义路由模块根据意图和槽位信息，路由到对应的动作。

```cpp
#pragma once
#include <string>
#include <unordered_map>
#include <functional>

class SemanticRouter {
public:
    // 注册动作
    void registerAction(const std::string& intent, const std::function<void(const std::unordered_map<std::string, std::string>&)>& action);

    // 路由到对应的动作
    void route(const std::string& intent, const std::unordered_map<std::string, std::string>& slots);

private:
    std::unordered_map<std::string, std::function<void(const std::unordered_map<std::string, std::string>&)>> actionMap;
};
```

```cpp
#include "semantic_router.h"
#include <iostream>

void SemanticRouter::registerAction(const std::string& intent, const std::function<void(const std::unordered_map<std::string, std::string>&)>& action) {
    actionMap[intent] = action;
}

void SemanticRouter::route(const std::string& intent, const std::unordered_map<std::string, std::string>& slots) {
    if (actionMap.find(intent) != actionMap.end()) {
        actionMap[intent](slots);
    } else {
        std::cerr << "No action registered for intent: " << intent << std::endl;
    }
}
```

---

#### **4. 动作执行模块**
动作执行模块实现具体的业务逻辑。

```cpp
#pragma once
#include <unordered_map>
#include <string>
#include <iostream>

class Actions {
public:
    static void playMusic(const std::unordered_map<std::string, std::string>& slots);
    static void setAlarm(const std::unordered_map<std::string, std::string>& slots);
    static void getWeather(const std::unordered_map<std::string, std::string>& slots);
};
```

```cpp
#include "actions.h"

void Actions::playMusic(const std::unordered_map<std::string, std::string>& slots) {
    std::cout << "Playing music..." << std::endl;
}

void Actions::setAlarm(const std::unordered_map<std::string, std::string>& slots) {
    std::cout << "Setting alarm at " << slots.at("time") << std::endl;
}

void Actions::getWeather(const std::unordered_map<std::string, std::string>& slots) {
    std::cout << "Fetching weather for location: " << slots.at("location") << std::endl;
}
```

---

#### **5. 系统调用模块**
系统调用模块负责与外部系统交互（如 API 调用、数据库查询等）。这里可以根据具体需求扩展。

---

### **主程序**
将所有模块整合在一起，形成完整的交互流程。

```cpp
#include "intent_recognizer.h"
#include "slot_extractor.h"
#include "semantic_router.h"
#include "actions.h"

int main() {
    // 初始化模块
    IntentRecognizer intentRecognizer;
    intentRecognizer.loadModel("");

    SlotExtractor slotExtractor;
    SemanticRouter router;

    // 注册动作
    router.registerAction("PlayMusic", Actions::playMusic);
    router.registerAction("SetAlarm", Actions::setAlarm);
    router.registerAction("GetWeather", Actions::getWeather);

    // 用户输入
    std::string userInput = "set alarm at 7:30";

    // 意图识别
    std::string intent = intentRecognizer.recognizeIntent(userInput);

    // 槽位抽取
    auto slots = slotExtractor.extractSlots(userInput);

    // 语义路由
    router.route(intent, slots);

    return 0;
}
```

---

### **运行示例**
输入：`set alarm at 7:30`
输出：
```
Setting alarm at 7:30
```

输入：`get weather in London`
输出：
```
Fetching weather for location: London
```

---

### **总结**

- **模块化设计**：每个功能模块独立实现，便于扩展和维护。
- **灵活性**：通过注册动作，可以轻松扩展新的意图和功能。
- **可扩展性**：可以进一步集成外部 API 调用、数据库查询等功能，增强系统能力。






build path:
/home/.local/lit/kds-freeswitch/freeswitch/docker/examples/ubuntu18





- 20250418
源码编译signalwire依赖
源码编译mod_unimrcp模块
源码编译freeswitch服务
安装freeswitch及其所需的声音资源文件


## 个税排名城市

上海
北京
深圳
杭州
广州

苏州
宁波
成都
南京
天津


## yhy无声故障问题排查
lua(va.lua)
Enter va.lua



Cannot park channels that are under control already

Null MRCPv2 Connection


提供主备用服务切换、压测环境复现、日志导出定位等方法深入排查问题
bot和转人工流程


- ulimit -c
- netstat/ss/lsop
awk '{print $2}' /proc/net/tcp | cut -d':' -f2 | xargs -I{} printf "%d\n" 0x{}



[root@SC-prod-vm-yhy151 bin]# cat /proc/43/net/sockstat
sockets: used 376
TCP: inuse 67 orphan 0 tw 6 alloc 200 mem 0
UDP: inuse 15 mem 1088
UDPLITE: inuse 0
RAW: inuse 0
FRAG: inuse 0 memory 0

[root@SC-prod-vm-yhy151 bin]# cat /proc/43/net/sockstat
sockets: used 374
TCP: inuse 67 orphan 0 tw 4 alloc 202 mem 0
UDP: inuse 11 mem 967
UDPLITE: inuse 0
RAW: inuse 0
FRAG: inuse 0 memory 0
[root@SC-prod-vm-yhy151 bin]# date
Wed Apr 16 14:25:02 CST 2025


[root@SC-prod-vm-yhy151 bin]# cat /proc/43/status
Name:	freeswitch
Umask:	0022
State:	S (sleeping)
Tgid:	43
Ngid:	0
Pid:	43
PPid:	1
TracerPid:	0
Uid:	0	0	0	0
Gid:	0	0	0	0
FDSize:	256
Groups:	0
NStgid:	43
NSpid:	43
NSpgid:	1
NSsid:	1
VmPeak:	 4639464 kB
VmSize:	 4633204 kB
VmLck:	       0 kB
VmPin:	       0 kB
VmHWM:	  230628 kB
VmRSS:	  230020 kB
RssAnon:	  217288 kB
RssFile:	   12732 kB
RssShmem:	       0 kB
VmData:	  349308 kB
VmStk:	     132 kB
VmExe:	      24 kB
VmLib:	   30072 kB
VmPTE:	    1292 kB
VmSwap:	       0 kB
HugetlbPages:	       0 kB
CoreDumping:	0
THP_enabled:	1
Threads:	48
SigQ:	1/128228
SigPnd:	0000000000000000
ShdPnd:	0000000000000000
SigBlk:	0000000000000000
SigIgn:	0000000010003006
SigCgt:	0000000180004209
CapInh:	0000000000000000
CapPrm:	00000000a80425fb
CapEff:	00000000a80425fb
CapBnd:	00000000a80425fb
CapAmb:	0000000000000000
NoNewPrivs:	0
Seccomp:	2
Seccomp_filters:	1
Speculation_Store_Bypass:	thread vulnerable
SpeculationIndirectBranch:	conditional enabled
Cpus_allowed:	ff
Cpus_allowed_list:	0-7
Mems_allowed:	00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000001
Mems_allowed_list:	0
voluntary_ctxt_switches:	52553
nonvoluntary_ctxt_switches:	344

[root@SC-prod-vm-yhy151 bin]# ll /proc/43/fdinfo/|wc -l
79
92


socket connect status time_wait:
[root@SC-prod-vm-yhy151 freeswitch]# cat /proc/net/tcp|grep " 06 "|wc -l
17

freeswitch.log*
12

echo "core.%e.%p" > /proc/sys/kernel/core_pattern

[kd-mrcp-tts] iflytekTtsInst::speak >>>>>> in
Get file /tmp/9B3AFEEBD1DE923D71211CB07A0E4726
[kd-mrcp-tts] iflytekTtsInst::speak >>>>>> Using Cache tts = 请说出您要咨询的问题
[kd-mrcp-tts] ttsProxyMsg::recordTime _pAsrTime : null
[kd-mrcp-tts] ttsProxyMsg::recordTime Invalid argument: stod
[kd-mrcp-tts][tts end] sessionId = f366dcb9-feaf-4e69-a217-a5066cf8f07a, traceId = 959673b8-679a-451c-868e-f78d173d647a, tts_duration = 0.277984, asr_tts_duration = 0
2025-05-16 10:53:42:974712 [INFO]   [kd-mrcp-tts][tts cb close] sessionId = f366dcb9-feaf-4e69-a217-a5066cf8f07a, traceId = 959673b8-679a-451c-868e-f78d173d647a
[kd-mrcp-tts] iflytekTtsInst::speak >>>>>> out


## Ubuntu 上从源码编译 FreeSWITCH，可以按照以下步骤操作：

- reference: https://developer.signalwire.com/freeswitch/FreeSWITCH-Explained/Installation/Linux/Debian_67240088/

### 1. 安装基础开发环境依赖

#### base devel componet
运行以下命令安装 FreeSWITCH 所需的基础依赖项：
```bash
# base
sudo apt update && apt install -y vim git build-essential cmake automake \
    autoconf 'libtool-bin|libtool' pkg-config \
    libssl-dev zlib1g-dev libdb-dev unixodbc-dev libncurses5-dev libexpat1-dev \
    libgdbm-dev bison erlang-dev libtpl-dev libtiff5-dev uuid-dev \
    libpcre3-dev libedit-dev libsqlite3-dev libcurl4-openssl-dev nasm \
    libogg-dev libspeex-dev libspeexdsp-dev libldns-dev python3-dev \
    libavformat-dev libswscale-dev 'libswresample-dev|libavresample-dev' \
    liblua5.2-dev libopus-dev libpq-dev libsndfile1-dev libflac-dev libvorbis-dev

# libavformat-dev failed to build
# priv_data_size
# ticks_per_frame


# # sofia-sip.git
# git clone https://github.com/freeswitch/sofia-sip.git
# ./bootstrap.sh -j
# ./configure
# make -j
# sudo make install

# # spandsp
# git clone https://github.com/freeswitch/spandsp.git
# ./bootstrap.sh -j
# ./configure
# make -j
# sudo make install
```

#### 3rd dependence componet

```bash
git clone https://github.com/signalwire/libks
git clone https://github.com/freeswitch/sofia-sip
git clone https://github.com/freeswitch/spandsp
git clone https://github.com/signalwire/signalwire-c

cd libks
cmake . -DCMAKE_INSTALL_PREFIX=/usr -DWITH_LIBBACKTRACE=1
sudo make install
cd ..

cd sofia-sip
./bootstrap.sh
# ./configure CFLAGS="-g -ggdb" --with-pic --with-glib=no --without-doxygen --disable-stun --prefix=/usr
./configure
make -j`nproc --all`
sudo make install
cd ..

cd spandsp
./bootstrap.sh
./configure CFLAGS="-g -ggdb" --with-pic --prefix=/usr
make -j`nproc --all`
sudo make install
cd ..

cd signalwire-c
PKG_CONFIG_PATH=/usr/lib/pkgconfig cmake . -DCMAKE_INSTALL_PREFIX=/usr
sudo make install
cd ..
```

#### unimrcp(option)

```bash
sudo apt-get install wget tar
wget https://www.unimrcp.org/project/component-view/unimrcp-deps-1-6-0-tar-gz/download -O unimrcp-deps-1.6.0.tar.gz
tar xvzf unimrcp-deps-1.6.0.tar.gz
cd unimrcp-deps-1.6.0
cd libs/apr
./configure --prefix=/usr/local/apr
make
sudo make install
cd ..
cd apr-util
./configure --prefix=/usr/local/apr
make
sudo make install
cd ..
git clone https://github.com/unispeech/unimrcp.git
cd unimrcp
./bootstrap
./configure
make
sudo make install
cd ..
```


### 2. 克隆源码
从官方仓库克隆 FreeSWITCH 源码：

```bash
git clone -b v1.10 https://github.com/signalwire/freeswitch.git
cd freeswitch

# Because we're in a branch that will go through many rebases, it's
# better to set this one, or you'll get CONFLICTS when pulling (update).
git config pull.rebase true

#### mod_unimrcp
cd src/mod/asr_tts
git clone https://github.com/freeswitch/mod_unimrcp.git
# cd mod_unimrcp
# export PKG_CONFIG_PATH=/usr/local/freeswitch/lib/pkgconfig:/usr/local/unimrcp/lib/pkgconfig
# ./bootstrap.sh
# ./configure
# make
# sudo make install
# cd ..
```

#### Building

Add asr_tts/mod_unimrcp to build/modules.conf.in
Build FreeSWITCH with 'make install'

#### Configuration

Edit conf/autoload_config/unimrcp.conf.xml
Add MRCP profiles to conf/mrcp_profiles/
Add <load module="mod_unimrcp"/> to autoload_configs/modules.conf.xml

- [reference](https://developer.signalwire.com/freeswitch/FreeSWITCH-Explained/Modules/mod_unimrcp_6586728/)


### 3. 运行引导脚本
运行 bootstrap.sh 脚本以生成配置文件：
```bash
./bootstrap.sh -j
```

### 4. 配置编译选项
运行 `configure` 脚本以配置编译选项：
```bash
./configure
```

如果需要自定义安装路径，可以使用 `--prefix` 参数，例如：
```bash
./configure --prefix=/usr/local/freeswitch
```
<!--
v1.10.12
-------------------------- FreeSWITCH configuration --------------------------

  Locations:

      prefix:          /usr/local/freeswitch
      exec_prefix:     /usr/local/freeswitch
      bindir:          ${exec_prefix}/bin
      confdir:         /usr/local/freeswitch/conf
      libdir:          ${exec_prefix}/lib
      datadir:         /usr/local/freeswitch
      localstatedir:   /usr/local/freeswitch
      includedir:      /usr/local/freeswitch/include/freeswitch

      certsdir:        /usr/local/freeswitch/certs
      dbdir:           /usr/local/freeswitch/db
      grammardir:      /usr/local/freeswitch/grammar
      htdocsdir:       /usr/local/freeswitch/htdocs
      fontsdir:        /usr/local/freeswitch/fonts
      logfiledir:      /usr/local/freeswitch/log
      modulesdir:      /usr/local/freeswitch/mod
      pkgconfigdir:    ${exec_prefix}/lib/pkgconfig
      recordingsdir:   /usr/local/freeswitch/recordings
      imagesdir:       /usr/local/freeswitch/images
      runtimedir:      /usr/local/freeswitch/run
      scriptdir:       /usr/local/freeswitch/scripts
      soundsdir:       /usr/local/freeswitch/sounds
      storagedir:      /usr/local/freeswitch/storage
      cachedir:        /usr/local/freeswitch/cache

------------------------------------------------------------------------------
master
-------------------------- FreeSWITCH configuration --------------------------

  Locations:

      prefix:          /usr/local/freeswitch
      exec_prefix:     /usr/local/freeswitch
      bindir:          ${exec_prefix}/bin
      confdir:         /usr/local/freeswitch/conf
      libdir:          ${exec_prefix}/lib
      datadir:         /usr/local/freeswitch
      localstatedir:   /usr/local/freeswitch
      includedir:      /usr/local/freeswitch/include/freeswitch

      certsdir:        /usr/local/freeswitch/certs
      dbdir:           /usr/local/freeswitch/db
      grammardir:      /usr/local/freeswitch/grammar
      htdocsdir:       /usr/local/freeswitch/htdocs
      fontsdir:        /usr/local/freeswitch/fonts
      logfiledir:      /usr/local/freeswitch/log
      modulesdir:      /usr/local/freeswitch/mod
      pkgconfigdir:    ${exec_prefix}/lib/pkgconfig
      recordingsdir:   /usr/local/freeswitch/recordings
      imagesdir:       /usr/local/freeswitch/images
      runtimedir:      /usr/local/freeswitch/run
      scriptdir:       /usr/local/freeswitch/scripts
      soundsdir:       /usr/local/freeswitch/sounds
      storagedir:      /usr/local/freeswitch/storage
      cachedir:        /usr/local/freeswitch/cache

------------------------------------------------------------------------------
 -->


### 5. 编译源码
使用 `make` 命令编译源码：
```bash
make -j$(nproc)
```

### 6. 安装 FreeSWITCH
运行以下命令安装 FreeSWITCH：
```bash
sudo make install
```

### 7. 安装声音文件
安装 FreeSWITCH 所需的声音文件：
```bash
sudo make sounds-install
sudo make moh-install
```

### 8. 验证安装
运行以下命令启动 FreeSWITCH：
```bash
/usr/local/freeswitch/bin/freeswitch
```

### 9. 可选：配置服务
如果需要将 FreeSWITCH 配置为系统服务，可以参考官方文档或使用 `systemd` 配置文件。

完成后，您可以通过 `fs_cli` 连接到 FreeSWITCH 控制台：
```bash
/usr/local/freeswitch/bin/fs_cli
```

### 参考
您可以查看源码中的 `README` 或 INSTALL 文件获取更多详细信息。



- 20250417
搭建freeswitch编译开发环境
源码编译libk依赖
源码编译sofia-sip依赖
源码编译spandsp依赖


- 20250416
分析颐和园预发环境fs网络资源占用情况
熟悉并配置跳板机访问颐和园线上环境
分析颐和园线上环境fs所用网络资源及其配置
分析颐和园线上环境fs所用内存和磁盘资源及配置


- 20250415
筛查fs无tts播报或无asr识别的通话录音详情
分析fs无声tts的控制通道交互流程
分析fs无asr识别的控制通道交互流程
分析fs执行park失败报错问题(413)

5i9rdUgHPitakzkG


- 20250414
分析颐和园线上fs bot交互流程(5 segmentation fault)
分析颐和园线上fs 人工坐席转接流程
定位颐和园线上fs 呼入电话tts无声音播报的问题语音(126 null connection)
支持排查徐工测试环境媒体数据加密问题




- 20250411
分析tts-proxy代码，定位session id为空问题
分析mrcp代码，定位session id为空问题
定位freeswitch转人工前调用mrcp时未传session id字段
源码编译安装gm工具



- 20250410
分析颐和园线上mrcp日志asr交互流程
排查颐和园线上mrcp日志asr中ws连接逾期问题
分析颐和园线上mrcp日志tts交互流程(用的联想tts)
排查颐和园线上tts session id为空问题



- 20250409
新增kt-lib/intent意图规则的截图匹配逻辑
修复kt-lib/sysfunc.syscall打开截图失败case
分析颐和园线上mrcp日志sip交互
分析颐和园线上mrcp日志rtp交互




sysfunc reply: {"cmd":"sysfunc.syscall","data":{"result":"槽值不存在"},"eot":true,"private":null,"sessionId":"28817cac-65f6-4697-bf29-eeaee6f9c46f","state":{"code":0,"extend":"","info":"success"},"status":400}


首先，感谢马凯帮导出freeswitch和mrcp日志文件!
根据线上日志的初步排查，现需要结合颐和园线上runtime环境部署方案及其相关网络配置进行综合分析，烦请相关知情同学帮补充如下信息，以便定位其具体原因，谢谢。
1、关于颐和园线上runtime环境整体部署方案说明(包含freeswitch服务、mrcp服务、与freeswitch有网络通信的其他服务)
2、关于颐和园语音网关的网络配置(开放的通信方式tcp/udp、ip、port范围)
3、freeswtich容器的外网相关网络配置(开放的通信方式tcp/udp、ip、port范围)
4、freeswtich容器的内网相关网络配置(开放的通信方式tcp/udp、ip、port范围)
5、与freeswitch有网络通信的其他服务的网络配置(开放的通信方式tcp/udp、ip、port范围)
6、mrcp容器的网络配置(开放的通信方式tcp/udp、ip、port范围)



- 20250408
分析颐和园线上freeswitch日志sip交互
分析颐和园线上freeswitch日志rtp交互
分析颐和园线上freeswitch日志mrcp-client交互
分析颐和园线上mrcp日志mrcp-server交互


排查项目线上freeswitch无法连接mrcp无声音问题

FreeSWITCH Version 1.10.5-release+git~20201013T151219Z~2b79ac2f75~64bit (-releasegit 2b79ac2 2020-10-13 15:12:19Z 64bit)
FreeSWITCH Started


Run as Daemon
UniMRCP Server [1.7.0]
Open Config File



fs：
20次  Starting task thread
0403: 3(1 restart)
0404: 10(2 restart)
0405: 6
0406: 1

17次  Segmentation fault



0403:
414 tts/asr mrcp connet failed NULL
0404:
197 tts/asr mrcp connet failed NULL



sip:
fs clinet m=application 9 TCP/MRCPv2
mrcp server m=application 1644 TCP/MRCPv2


tts mrcp connect(normal):

Add Control Channel \u003c568d287e33c34b8f@speechsynth\u003e 192.168.6.151:35592 \u003c-\u003e 192.168.6.151:1644 [3]
...
Send MRCP Request TTS-123 \u003c568d287e33c34b8f@speechsynth\u003e [1]
Send MRCPv2 Data 192.168.6.151:35592 \u003c-\u003e 192.168.6.151:1644 [916 bytes]
MRCP/2.0 916 SPEAK 1



/usr/local/freeswitch/start.sh: line 100:    44 Segmentation fault      (core dumped) /usr/local/freeswitch/bin/freeswitch -nonat


Successfully Loaded



tts mrcp connect(un-normal):
Add Control Channel \u003ca409d64e2b444700@speechsynth\u003e 192.168.6.151:46624 \u003c-\u003e 192.168.6.151:1644 [2]
...

Send MRCP Request TTS-220 \u003ca409d64e2b444700@speechsynth\u003e [1]

Null MRCPv2 Connection \u003ca409d64e2b444700@speechsynth\u003e
Cancel MRCP Request \u003ca409d64e2b444700@speechsynth\u003e [1]

Raise App MRCP Response TTS-220 \u003ca409d64e2b444700\u003e\n


asr mrcp connect:
Send MRCPv2 Data 192.168.6.151:60486 \u003c-\u003e 192.168.6.151:1644
Receive MRCPv2 Data 192.168.6.151:60486 \u003c-\u003e 192.168.6.151:1644


tts audio:
fs client recv m=audio 3440 RTP/AVP
mrcp server send m=audio 45262 RTP/AVP

Open RTP Receiver 192.168.6.151:3440 \u003c- 192.168.6.151:45262


asr audio:


- 20250407
更新creator_zone_multi/DimExtract工程代码，适配arm64平台调试编译
更新creator_zone_multi/PoPipelineTest工程依赖，适配arm64平台编译调试运行
整理creator_zone_multi环境，并打包提供元月arm64版本安装包


- 20250403
更新creator_zone_multi/Classification工程代码，适配arm64平台调试编译
更新creator_zone_multi/DimSearch工程代码，适配arm64平台调试编译
更新creator_zone_multi/DimRec工程代码，适配arm64平台调试编译
更新creator_zone_multi/PoPipeline工程代码，适配arm64平台调试编译


- 20250402
调试意图体系Excel表格必要数据解析的工具程序
测试意图槽位体系数据库kt.db
设计sysfunc语义路由模块semantic_router
修改sysfunc.app.exec打开应用时以后台的方式运行


- 20250401
添加sysfunc.syscall.intent老接口支持recommended_install_app字段逻辑
合并sysfunc/app_manager代码，提交git仓库
定位解决太原热力项目线上mrcp中asr识别结果为空问题(配置多余按键监听事件)
排查徐工项目测试asr-proxy服务推送识别结果时kafka报错(网络端口不通导致)




https://github.com/modelscope/FunASR/blob/main/docs/tutorial/README_zh.md


使用国内特定python源安装(清华源：-i https://pypi.tuna.tsinghua.edu.cn/simple):

pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple



## onnxruntime memory leak
- 使用vargrind查看内存泄漏
- 使用Massif 查看堆分配
- 分析发现prepack消耗内存
- 设置kOrtSessionOptionsConfigDisablePrepacking,减少内存
- 跟踪到onnxsession内存释放不彻底问题
- glibc分配缓存未释放机制(系统底层内存管理策略)
- 尝试使用malloc_trim释放内存()



- 20250331
设计前后端交互的清除应用安装任务接口
设计应用安装任务的删、查的功能接口
开发清除已完成的应用安装任务功能及其接口
开发查询当前所有的应用安装任务功能及其接口


- 20250328
设计应用安装任务实例对象结构、历史任务缓存数据结构
设计开发新增应用安装任务功能接口、应用安装异步处理流程
转换并更新意图索引向量库
沟通跟进实时降噪评估效果



实现一个自定义的数据结构，能同时满足以下要求：
1、支持缓存自始至终所有历史元素
2、支持删除所有历史元素的某个元素
3、支持阻塞队列一样的入队和出队功能
4、支持遍历当前所有元素


- 20250327
review 标准kdm_intent意图理解模块
修改优化kdm_intent文档kds.json和README.md
优化kdm_intent文档design.json
梳理sysfunc.app.install/install_list接口流程


## kdm-intent review

### Design
Sort model 改成 ranking mode
架构中的槽位填充，改为槽位抽取
流程图改为正规的调用流程图，补充对应的异常处理，每个块中断的时候关键的异常补充
补充说明批量处理的个数限制 为 3组
架构中三元素：业务、管理、数据

### API
Domain 可以 填写 AIPC，明确说明咱不支持


### 通用建议
有序才能高效，数据结构至为关键
架构设计可以通过业务功能、运营管理、数据三部分来体现完整性和清晰度
C++库是如何发布，比如发布的Linux 版本，可以走源码发布，打tag 说明 release note


- 20250326
迁移intent2代码到标准kdm_intent仓库
编写kdm_intent标准化文档kdm.json
编写kdm_intent标准化文档README.md
编写kdm_intent标准化文档design.md


- 20250325
编写sysfunc.app.get/installable/install整体流程测试用例
调测sysfunc.app.get/installable/install整体流程
梳理汇总sysfunc.app.get/installable/install整体流程测试情况
搭建intent kdm标准化工程框架



|  流程可通  |  name  |  package  |  desktop:Name(ukui search)  |  desktop_name  |
|:-----:|:-----:|:-----:|:-----:|:-----:|
|  可通  |  微信  |  wechat  |  wechat / 微信  |  /usr/share/applications/wechat.desktop  |
|  不通|  360安全浏览器  |  browser360-cn-stable  |  360 Secure Browser / 360安全浏览器  |  /usr/share/applications/browser360-cn.desktop  |
|  不通  |  QQ  |  linuxqq  |  QQ  |  /usr/share/applications/qq.desktop  |
|  不通  |  XMind  |  xmind-vana  |  Xmind  |  /usr/share/applications/xmind.desktop  |



- 20250324
定位dbus接口InstallDebFile离线安装个别deb包(kt-ktbrowser-stable)失败报错#0200问题
自测sysfunc.app.install接口在线源安装功能
自测sysfunc.app.install接口离线deb包安装功能
排查离线安装deb包成功，但ukui search查不到对应应用信息问题
，deb包文件名package_name 和 .desktop文件中Name 不对应, 导致ukui search不到应用信息





## TODO （外部）麒麟-联想AIPC沟通
#### Q：@兜兜里面没有糖  hello，咨询个问题哈，调用InstallDebFile方法，安装本地不同deb包(wechat和kt-ktbrowser-stable)，其中wechat包可以正常安装，但安装kt-ktbrowser-stable时，InstalldebFinishedWithErrCode信号会报错#0200，如图，请问这可能是什么原因导致的？

#### A:麒麟技术反馈：执行postinst报错了, 可以看下是不是缺少了环境变量导致的, 接口没有要求哪些环境变量是必要的，得看postinst里怎么写的，比如需要弹窗的得加上DISPLAY

#### Conslution: 1、可能跟kt-ktbrowser-stable离线deb包，构建时相关配置有关，需要协调开天和麒麟共同推进解决
#### Conslution: 2、deb文件内包名package_name 和 .desktop文件中Name 不对应, 导致ukui search不到应用信息


yes: wechat
no: kt-ktbrowser-stable
no: xmind-vana


- 20250321
调测sysfunc.app.install中deb包下载功能
排查解决http文件下载时连接服务端抛异常、文件写入时无法打开、获取deb文件具体包名失败等问题
调测sysfunc.app.install中离线deb包安装功能
排查修复构建离线安装deb结果异常、离线安装deb接口传参报错问题


I20250321 18:08:41.619684 306457 app_manager.cc:215] app manager searching wechat
I20250321 18:08:41.687517 306457 app_manager.cc:260] app manager search [{"exec":"/usr/bin/wechat ","icon":"/usr/share/icons/hicolor/256x256/apps/wechat.png","identity":"/usr/share/applications/wechat.desktop","name":"微信","package":"wechat","status":4,"version":""}]
I20250321 18:08:41.692938 306457 sysfunc.cc:819] sysfunc reply: {"cmd":"sysfunc.app.install","data":[{"exec":"","icon":"","identity":"","name":"qq","package":"qq","status":1,"version":""},{"exec":"/usr/bin/  ","icon":"/usr/share/icons/hicolor/256x256/apps/wechat.png","identity":"/usr/share/applications/wechat.desktop","name":"微信","package":"wechat","status":4,"version":""}],"eot":true,"private":"test sysfunc","sessionId":null,"state":{"code":0,"extend":"","info":"success"},"status":0}
I20250321 18:08:41.692989 306457 main.cc:46] callback({"cmd":"sysfunc.app.install","data":[{"exec":"","icon":"","identity":"","name":"qq","package":"qq","status":1,"version":""},{"exec":"/usr/bin/wechat ","icon":"/usr/share/icons/hicolor/256x256/apps/wechat.png","identity":"/usr/share/applications/wechat.desktop","name":"微信","package":"wechat","status":4,"version":""}],"eot":true,"private":"test sysfunc","sessionId":null,"state":{"code":0,"extend":"","info":"success"},"status":0})



03-21,18:08:21 [INFO]: Emitting InstalldebStatusChanged progress = 95 , status = 正在应用更改 ,current_details = 正在安装 wechat
03-21,18:08:33 [INFO]: Emitting InstalldebStatusChanged progress = 95 , status = 正在应用更改 ,current_details = 正在配置 wechat
03-21,18:08:39 [INFO]: Emitting InstalldebStatusChanged progress = 95 , status = 正在应用更改 ,current_details = 运行安装后的触发器 kysec-utils
03-21,18:08:39 [INFO]: Emitting InstalldebStatusChanged progress = 95 , status = 正在应用更改 ,current_details = 运行安装后的触发器 desktop-file-utils
03-21,18:08:40 [INFO]: Emitting InstalldebStatusChanged progress = 95 , status = 正在应用更改 ,current_details = 运行安装后的触发器 bamfdaemon
03-21,18:08:40 [INFO]: Emitting InstalldebStatusChanged progress = 95 , status = 正在应用更改 ,current_details = 运行安装后的触发器 mime-support
03-21,18:08:40 [INFO]: Emitting InstalldebStatusChanged progress = 95 , status = 正在应用更改 ,current_details = 运行安装后的触发器 hicolor-icon-theme
03-21,18:08:41 [INFO]: Emitting InstalldebStatusChanged progress = 95 , status = 完成 ,current_details = 运行安装后的触发器 hicolor-icon-theme
03-21,18:08:41 [INFO]: Emitting InstalldebStatusChanged progress = 100 , status = 完成 ,current_details = 运行安装后的触发器 hicolor-icon-theme
03-21,18:08:41 [INFO]: Other Action:current_items = 0, total_items = 0, currenty_bytes = 0 kB, total_bytes = 0 kB, current_cps = 0 kB/s
03-21,18:08:41 [INFO]: Emitting InstalldebStatusChanged progress = 100 , status = 完成 ,current_details = 运行安装后的触发器 hicolor-icon-theme
03-21,18:08:41 [INFO]: Emitting InstalldebStatusChanged progress = 100 , status = 完成 ,current_details = 运行安装后的触发器 hicolor-icon-theme
03-21,18:08:41 [INFO]: Emitting Cancelable: True
03-21,18:08:41 [INFO]: Emptying the lockPath(/tmp/lock/) is complete...
03-21,18:08:41 [INFO]: Shutdown Has been unlocked...
03-21,18:08:41 [INFO]: Emitting InstalldebFinished success = True , error_string =  , error_desc =
03-21,18:08:41 [INFO]: Emitting InstalldebFinishedWithErrCode success = True , error_string =  , error_desc =  , error_code =




03-21,15:20:14 [INFO]: The incoming language is null...
03-21,15:20:14 [INFO]: Method InstallDebFile and check_local_dep:False, auto_satisfy:True, current_lang: , InstallDebFile sender: test .
03-21,15:20:14 [INFO]: Will install: /home/lit/995c7baea2434f77be2f7a293a1ed4b1.deb.
03-21,15:20:14 [INFO]: Verify pkg:/home/lit/995c7baea2434f77be2f7a293a1ed4b1.deb.
03-21,15:20:15 [INFO]: Signature Verified Ok!
03-21,15:20:15 [INFO]: Finished: refreshing Cache for System Update Successfully...
03-21,15:20:15 [INFO]: Install deb_package: check broken: 0.
03-21,15:20:15 [INFO]: Install deb_package: required changes
03-21,15:20:15 [WARNING]: Group depend satify, ignore libcurl3-nss.
03-21,15:20:15 [WARNING]: Group depend satify, ignore libcurl4.
03-21,15:20:15 [WARNING]: Group depend satify, ignore libcurl3.
03-21,15:20:15 [WARNING]: Group depend satify, ignore libgtk-4-1.
03-21,15:20:15 [INFO]: Cache satisfy is True.
03-21,15:20:15 [INFO]: Application installation control policy not enabled .
03-21,15:20:15 [INFO]: source name: kt-ktbrowser-stable.
03-21,15:20:15 [INFO]: Start acquiring Shutdown lock(block)...
03-21,15:20:15 [INFO]: File(/tmp/lock/) is not exists and will be create
03-21,15:20:15 [INFO]: Shutdown Has been locked...
03-21,15:20:15 [INFO]: Emitting InstalldebStatusChanged progress = 9 , status =  ,current_details =
03-21,15:20:15 [INFO]: Emitting InstalldebStatusChanged progress = 9 , status = 正在等待验证 ,current_details =
03-21,15:20:15 [INFO]: Emitting InstalldebStatusChanged progress = 9 , status = 正在解决依赖关系 ,current_details =
03-21,15:20:15 [INFO]: Emitting InstalldebStatusChanged progress = 9 , status = 正在载入软件列表 ,current_details =
03-21,15:20:16 [INFO]: Emitting InstalldebStatusChanged progress = 9 , status = 正在解决依赖关系 ,current_details =
03-21,15:20:16 [INFO]: Emitting InstalldebStatusChanged progress = 9 , status = 正在等待服务启动 ,current_details =
03-21,15:20:16 [INFO]: Emitting InstalldebStatusChanged progress = 9 , status = 正在等待验证 ,current_details =
03-21,15:20:16 [INFO]: Emitting InstalldebStatusChanged progress = 9 , status = 等待中 ,current_details =
03-21,15:20:16 [INFO]: Emitting InstalldebStatusChanged progress = 9 , status = 正在运行任务 ,current_details =
03-21,15:20:16 [INFO]: Emitting InstalldebStatusChanged progress = 11 , status = 正在运行任务 ,current_details =
03-21,15:20:16 [INFO]: Emitting InstalldebStatusChanged progress = 11 , status = 正在载入软件列表 ,current_details =
03-21,15:20:16 [INFO]: Emitting InstalldebStatusChanged progress = 11 , status = 正在载入软件列表 ,current_details =
03-21,15:20:16 [INFO]: Emitting InstalldebStatusChanged progress = 11 , status = 正在载入软件列表 ,current_details =
03-21,15:20:17 [INFO]: Emitting InstalldebStatusChanged progress = 11 , status = 正在解决依赖关系 ,current_details =
03-21,15:20:17 [INFO]: Emitting InstalldebStatusChanged progress = 11 , status = 正在应用更改 ,current_details =
03-21,15:20:17 [INFO]: Emitting InstalldebStatusChanged progress = 95 , status = 正在应用更改 ,current_details =
03-21,15:20:17 [INFO]: Emitting InstalldebStatusChanged progress = 95 , status = 正在应用更改 ,current_details = 正在安装 kt-ktbrowser-stable
03-21,15:20:23 [INFO]: Emitting InstalldebStatusChanged progress = 95 , status = 正在应用更改 ,current_details = 正在配置 kt-ktbrowser-stable
03-21,15:20:23 [INFO]: Emitting InstalldebStatusChanged progress = 95 , status = 正在应用更改 ,current_details = 运行安装后的触发器 kysec-utils
03-21,15:20:24 [INFO]: Emitting InstalldebStatusChanged progress = 95 , status = 正在应用更改 ,current_details = 运行安装后的触发器 desktop-file-utils
03-21,15:20:25 [INFO]: Emitting InstalldebStatusChanged progress = 95 , status = 正在应用更改 ,current_details = 运行安装后的触发器 bamfdaemon
03-21,15:20:25 [INFO]: Emitting InstalldebStatusChanged progress = 95 , status = 正在应用更改 ,current_details = 运行安装后的触发器 mime-support
03-21,15:20:25 [INFO]: Emitting InstalldebStatusChanged progress = 95 , status = 正在应用更改 ,current_details = 运行安装后的触发器 man-db
03-21,15:20:29 [ERROR]: Selecting previously unselected package kt-ktbrowser-stable.
(Reading database ... 216089 files and directories currently installed.)
Preparing to unpack .../995c7baea2434f77be2f7a293a1ed4b1.deb ...
Unpacking kt-ktbrowser-stable (1.0.0.2-1) ...
Setting up kt-ktbrowser-stable (1.0.0.2-1) ...
update-alternatives: using /usr/bin/kt-ktbrowser-stable to provide /usr/bin/kt-ktbrowser (kt-ktbrowser) in auto mode
Creating desktop icon...
cp: '/home/lit//kt-ktbrowser.desktop':
dpkg: error processing package kt-ktbrowser-stable (--install):
 installed kt-ktbrowser-stable package post-installation script subprocess returned error exit status 1
Processing triggers for kysec-utils (3.3.6.1-0k8.18) ...
Processing triggers for desktop-file-utils (0.24-1kylin2) ...
Processing triggers for bamfdaemon (0.5.3+18.04.20180207.2-0kylin2) ...
Rebuilding /usr/share/applications/bamf-2.index...
Processing triggers for mime-support (3.64kylin1) ...
Processing triggers for man-db (2.9.1-1kylin0k1.0) ...
Errors were encountered while processing:
 kt-ktbrowser-stable

03-21,15:20:29 [INFO]: Emitting InstalldebStatusChanged progress = 95 , status = 完成 ,current_details = 运行安装后的触发器 man-db
03-21,15:20:29 [INFO]: Emitting InstalldebStatusChanged progress = 100 , status = 完成 ,current_details = 运行安装后的触发器 man-db
03-21,15:20:29 [INFO]: Other Action:current_items = 0, total_items = 0, currenty_bytes = 0 kB, total_bytes = 0 kB, current_cps = 0 kB/s
03-21,15:20:29 [INFO]: Emitting InstalldebStatusChanged progress = 100 , status = 完成 ,current_details = 运行安装后的触发器 man-db
03-21,15:20:29 [INFO]: Emitting InstalldebStatusChanged progress = 100 , status = 完成 ,current_details = 运行安装后的触发器 man-db
03-21,15:20:29 [INFO]: Emitting Cancelable: True
03-21,15:20:29 [ERROR]: Selecting previously unselected package kt-ktbrowser-stable.
(Reading database ... 216089 files and directories currently installed.)
Preparing to unpack .../995c7baea2434f77be2f7a293a1ed4b1.deb ...
Unpacking kt-ktbrowser-stable (1.0.0.2-1) ...
Setting up kt-ktbrowser-stable (1.0.0.2-1) ...
update-alternatives: using /usr/bin/kt-ktbrowser-stable to provide /usr/bin/kt-ktbrowser (kt-ktbrowser) in auto mode
Creating desktop icon...
cp: '/home/lit//kt-ktbrowser.desktop':
dpkg: error processing package kt-ktbrowser-stable (--install):
 installed kt-ktbrowser-stable package post-installation script subprocess returned error exit status 1
Processing triggers for kysec-utils (3.3.6.1-0k8.18) ...
Processing triggers for desktop-file-utils (0.24-1kylin2) ...
Processing triggers for bamfdaemon (0.5.3+18.04.20180207.2-0kylin2) ...
Rebuilding /usr/share/applications/bamf-2.index...
Processing triggers for mime-support (3.64kylin1) ...
Processing triggers for man-db (2.9.1-1kylin0k1.0) ...
Errors were encountered while processing:
 kt-ktbrowser-stable

03-21,15:20:29 [INFO]: Emptying the lockPath(/tmp/lock/) is complete...
03-21,15:20:29 [INFO]: Shutdown Has been unlocked...
03-21,15:20:29 [INFO]: Emitting InstalldebFinished success = False , error_string = 软件包操作异常,无法安装或移除软件包。 , error_desc =
03-21,15:20:29 [INFO]: Emitting InstalldebFinishedWithErrCode success = False , error_string = 软件包操作异常,无法安装或移除软件包。 , error_desc =  , error_code = #0200






I20250321 13:58:32.661221 108697 app_manager.cc:112] app manager download deb from https://kt-software-private-1313580039.cos.ap-beijing.myqcloud.com/private/manage/2025-01-10/995c7baea2434f77be2f7a293a1ed4b1.deb to /home/lit/995c7baea2434f77be2f7a293a1ed4b1.deb
I20250321 13:58:32.661356 108697 app_manager.cc:129] app manager connect server https://kt-software-private-1313580039.cos.ap-beijing.myqcloud.com to download /private/manage/2025-01-10/995c7baea2434f77be2f7a293a1ed4b1.deb
I20250321 13:59:22.122764 108697 app_manager.cc:334] app manager deb installing kt-ktbrowser-stable from /home/lit/995c7baea2434f77be2f7a293a1ed4b1.deb
I20250321 13:59:23.031014 108697 app_manager.cc:353] app manager deb install kt-ktbrowser-stable return: 0 err_msg:

I20250321 13:59:39.814688 108701 app_manager.cc:95] app manager received signal installdeb-finished: ret_flag: 0 package_name: simulative_package_name error_info: 软件包操作异常,无法安装或移除软件包。 error_reason:


I20250321 13:59:39.815351 108697 app_manager.cc:215] app manager searching kt-ktbrowser-stable
I20250321 13:59:39.818853 108697 app_manager.cc:260] app manager search [{"exec":"","icon":"","identity":"","name":"kt-ktbrowser-stable","package":"kt-ktbrowser-stable","status":1,"version":""}]



app manager deb g_dbus_proxy_call_sync error: Method “InstallDebFile” returned type “(is)”, but expected “(b)”

app manager received signal installdeb-finished: ret_flag: 0 package_name: simulative_package_name error_info: Transaction failed: 无法打开软件包文件 /home/lit/995c7baea2434f77be2f7a293a1ed4b1.deb error_reason:
app manager received signal installdeb-finished: ret_flag: 0 package_name: simulative_package_name error_info: 无法打开软件包文件,请将该文件复制到您的本地电脑中并检查文件的权限。 error_reason:



[I20250321 10:38:23.663755 96612 app_manager.cc:333] app manager deb installing kt-ktbrowser-stable from 995c7baea2434f77be2f7a293a1ed4b1.deb
[I20250321 10:38:23.686916 96616 app_manager.cc:94] app manager received signal installdeb-finished: ret_flag: 0 package_name: simulative_package_name error_info: No such file or directory . error_reason:
[E20250321 10:38:23.687659 96612 app_manager.cc:345] app manager deb g_dbus_proxy_call_sync error: Method “InstallDebFile” returned type “(is)”, but expected “(b)”


- 20250320
研究麒麟dbus接口InstallDebFile使用
开发调用dbus接口离线安装本地deb包功能
开发离线安装本地deb包时信号捕获与异步处理功能
编写deb包下载及其离线安装测试用例


cpp-httplib/httplib.h


- 20250319
调研http client网络库
开发http 文件url下载功能
修改优化sysfunc.app.install接口调用流程
开发AppManager模块支持deb安装包下载和安装接口


<!--
  {"id":6,"appCode":"XMind","appName":"XMind","appClass":"效率工具",
   "appLogo":"https://kt-software-private-1313580039.cos.ap-beijing.myqcloud.com/private/manage/2025-01-10/4595fa8d1d5840d89107229e5ee73f1e.png",
   "appType":"deb","appVersion":"22.8.2224",
   "linkUrl":"https://kt-software-private-1313580039.cos.ap-beijing.myqcloud.com/private/manage/2025-01-10/edaf3696bdbf43a1bf52ac7ec0b9f859.deb",
   "describe":"一款全功能的思维导图和头脑风暴软件。像大脑的瑞士军刀一般，助你理清思路，捕捉创意。","cpu":"x86_64","xtVersion":null,"osVersion":"2403",
   "packageName":"xmind-vana_22.8.2224-202209010010_amd64.deb",
   "appDetails":{"age":null,"size":"108.46","language":null,"ranking":null,"developer":null},"preview":[],"comment":[null]},

  {"id":2,"appCode":"开天AI浏览器","appName":"开天AI浏览器","appClass":"AI应用",
   "appLogo":"https://kt-software-prod-1313580039.cos.ap-beijing.myqcloud.com/private/manage/2025-01-16/038782f9ef434af0b58788bb088783b9.png",
   "appType":"deb","appVersion":"1.0.0.2",
   "linkUrl":"https://kt-software-private-1313580039.cos.ap-beijing.myqcloud.com/private/manage/2025-01-10/995c7baea2434f77be2f7a293a1ed4b1.deb",
   "describe":"一款基于信创生态体系开发的新一代安全浏览器，专为满足中国自主创新需求而设计。采用国密算法，全面保障数据传输与用户信息安全，同时深度集成AI技术，为用户提供智能化的浏览体验。","cpu":"x86_64","xtVersion":null,"osVersion":"2403",
   "packageName":"kt-ktbrowser-stable_1.0.0.2-1_amd64-signed.deb",
   "appDetails":{"age":null,"size":"92.81","language":null,"ranking":null,"developer":null},"preview":[],"comment":[null]},

  {"id":1,"appCode":"微信","appName":"微信","appClass":"社交沟通",
   "appLogo":"https://kt-software-private-1313580039.cos.ap-beijing.myqcloud.com/private/manage/2024-12-30/3425059e85904224b99c14a3c8a2f834.png",
   "appType":"deb","appVersion":"4.0.1.7",
   "linkUrl":"https://kt-software-private-1313580039.cos.ap-beijing.myqcloud.com/private/manage/2024-12-30/05520e524c58411eb56851604d65d606.deb",
   "describe":"一款跨平台的通讯工具，支持文字、语音、视频聊天，可分享生活点滴，还有支付等功能。","cpu":"x86_64","xtVersion":null,"osVersion":"2403",
   "packageName":"wechat",
   "appDetails":{"age":null,"size":"224.18","language":null,"ranking":null,"developer":null},"preview":["https://kt-software-private-1313580039.cos.ap-beijing.myqcloud.com/private/manage/2024-12-30/3425059e85904224b99c14a3c8a2f834.png","https://kt-software-private-1313580039.cos.ap-beijing.myqcloud.com/private/manage/2024-12-30/3425059e85904224b99c14a3c8a2f834.png","https://kt-software-private-1313580039.cos.ap-beijing.myqcloud.com/private/manage/2024-12-30/3425059e85904224b99c14a3c8a2f834.png"],"comment":[null]}
-->


通过网盘分享的文件：sample.zip
链接: https://pan.baidu.com/s/1tG94-o-dU26O9UUVVzaObg 提取码: t6sy




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


- 20250318
探讨语音合成cache预热技术实现方案
研究分析tts-proxy cache模块代码ttsCache
开发tts-proxy讯飞API支持cssml功能
搭建开发环境，编译调试tts-proxy和kd-unimrcp



- unimrcp:
 - processTts -> mpf_buffer_audio_write -> audio_buffer
  <!-- demo_synth_channel_t:mpf_buffer_t{audio_buffer} -->
 - demo_synth_stream_read <- mpf_buffer_frame_read <- audio_buffer

- tts-proxy:
 - pTtsProxySpeak -> speak -> sendframe




- 20250317
筛选并转码典型场景下带噪样本语音
分析tts-proxy讯飞模块接口iflytekTtsInst、iflytekRequestParam
分析mrcp集成tts-proxy模块调用逻辑
调研讯飞语音合成API cssml使用方式，评估TTS功能支持



- TTS厂商、发音人、语速、音量、音高四个配置项:
 - 静态配置1、env::XUNFEI_SPEED;
 - 动态配置2、fs api(speak):mrcp-client(engine, voiceId, speed, pitch, volume, sessionId, traceId, vadEndTime8个参数);

## 语音合成多音字、静音停顿、数字读法
`SSML:Speech Synthesis Markup Language`

- 讯飞API在线语音合成如何在指定的文本处标记静音停顿？
 - [cssml方法](https://developer.xfyun.cn/thread/15340)
（1）对于发音人xiaoyan、xiaoyu、xiaofeng、xiaoqi、catherine、mary需使用cssml方法进行静音标记,并且不支持unicode文本编码。
（2）在business中添加参数ttp值为cssml。
（3）在指定文本位置添加静音标记，如：风<break time="500ms"/>轻轻摇着树梢。
 - 简单标记方法：
（1）“除去”cssml方法列举的发音人以外，均可以使用简单标记法。
（2）在指定文本位置添加静音标记，如：你好[p500]科大讯飞。

- [阿里语音合成SSML](https://help.aliyun.com/zh/isi/developer-reference/ssml-overview?spm=5176.12061040.J_3140004040.1.33e63871fJljX6)


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
