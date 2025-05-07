#!/bin/sh
lan_ip=$LAN_IP
wan_ip=$WAN_IP
int_sip_port=$INT_SIP_PORT
ext_sip_port=$EXT_SIP_PORT
esl_port=$ESL_PORT
wss_port=$WSS_PORT
ws_port=$WS_PORT
acl_service=$ACL_SERVICE
mrcp_ip=$MRCP_IP
mrcp_port=$MRCP_PORT

sed -i '/rtp-ip/s@value=".*"@value="'$lan_ip'"@'  /usr/local/freeswitch/conf/sip_profiles/internal.xml
sed -i '/sip-ip/s@value=".*"@value="'$lan_ip'"@'  /usr/local/freeswitch/conf/sip_profiles/internal.xml
sed -i '/rtp-ip/s@value=".*"@value="'$lan_ip'"@'  /usr/local/freeswitch/conf/sip_profiles/external.xml
sed -i '/sip-ip/s@value=".*"@value="'$lan_ip'"@'  /usr/local/freeswitch/conf/sip_profiles/external.xml
if [ -n "$wss_port" ]; then
	sed -i '/wss-binding/s@value=":.*"@value=":'$wss_port'"@g' /usr/local/freeswitch/conf/sip_profiles/internal.xml
fi
if [ -n "$ws_port" ]; then
	sed -i '/ws-binding/s@value=":.*"@value=":'$ws_port'"@g' /usr/local/freeswitch/conf/sip_profiles/internal.xml
fi
if [ -n "$RTP_START_PORT" ]; then
	sed -i '/rtp-start-port/s@value=".*"@value="'$RTP_START_PORT'"@' /usr/local/freeswitch/conf/autoload_configs/switch.conf.xml
fi
if [ -n "$RTP_END_PORT" ]; then
	sed -i '/rtp-end-port/s@value=".*"@value="'$RTP_END_PORT'"@' /usr/local/freeswitch/conf/autoload_configs/switch.conf.xml
fi
sed -i '/ext-rtp-ip/s@value=".*"@value="'$wan_ip'"@'  /usr/local/freeswitch/conf/sip_profiles/internal.xml
sed -i '/ext-sip-ip/s@value=".*"@value="'$wan_ip'"@'  /usr/local/freeswitch/conf/sip_profiles/internal.xml
sed -i '/ext-sip-ip/s@value=".*"@value="'$wan_ip'"@'  /usr/local/freeswitch/conf/sip_profiles/external.xml
sed -i '/ext-rtp-ip/s@value=".*"@value="'$wan_ip'"@'  /usr/local/freeswitch/conf/sip_profiles/external.xml
sed -i '/domain=/s@domain=.*"@domain='$wan_ip'"@'  /usr/local/freeswitch/conf/vars.xml
if [ -n "$int_sip_port" ]; then
sed -i '/internal_sip_port/s@internal_sip_port=.*"@internal_sip_port='$int_sip_port'"@' /usr/local/freeswitch/conf/vars.xml
fi

if [ -n "$ext_sip_port" ]; then
sed -i '/external_sip_port/s@external_sip_port=.*"@external_sip_port='$ext_sip_port'"@' /usr/local/freeswitch/conf/vars.xml
fi

if [ -n "$esl_port" ]; then
sed -i '/listen-port/s@value=".*"@value="'$esl_port'"@'  /usr/local/freeswitch/conf/autoload_configs/event_socket.conf.xml
fi

if [ -n "$acl_service" ]; then
sed -i '/gateway-url/s@http://.*/acl@http://'$acl_service'/acl@' /usr/local/freeswitch/conf/autoload_configs/xml_curl.conf.xml
fi

if [ -n "$mrcp_ip" ]; then
sed -i '/server-ip/s@value=".*"@value="'$mrcp_ip'"@' /usr/local/freeswitch/conf/mrcp_profiles/unimrcpserver-mrcp-v2.xml
fi

if [ -n "$mrcp_port" ]; then
sed -i '/server-port/s@value=".*"@value="'$mrcp_port'"@' /usr/local/freeswitch/conf/mrcp_profiles/unimrcpserver-mrcp-v2.xml
fi

if [ -n "$PGSQL_HOST" ]; then
find /usr/local/freeswitch/conf/ -name "*.xml"|xargs sed -i '/pgsql/s/hostaddr=.* port/host='$PGSQL_HOST' port/g'
fi

if [ -n "$PGSQL_PORT" ]; then
	find /usr/local/freeswitch/conf/ -name "*.xml"|xargs sed -i '/pgsql/s/port=.* db/port='$PGSQL_PORT' db/g'
fi
if [ -n "$PGSQL_USER" ]; then
	find /usr/local/freeswitch/conf/ -name "*.xml"|xargs sed -i '/pgsql/s/user=.* password/user='$PGSQL_USER' password/g'
fi
if [ -n "$PGSQL_PASSWORD" ]; then
	find /usr/local/freeswitch/conf/ -name "*.xml"|xargs sed -i '/pgsql/s#password='.*'"/#password='$PGSQL_PASSWORD'"/#g'
fi
if [ -n "$PGSQL_DBNAME" ]; then
	find /usr/local/freeswitch/conf/ -name "*.xml"|xargs sed -i '/pgsql/s#dbname=.* user#dbname='$PGSQL_DBNAME' user#g'
fi

if [ -n "$VA_EP" ]; then
    sed -i '/socket/s#data=".*async full"#data="'$VA_EP' async full"#g' /usr/local/freeswitch/conf/dialplan/public.xml
    sed -i '/socket/s#data=".*async full"#data="'$VA_EP' async full"#g' /usr/local/freeswitch/conf/dialplan/default.xml
fi
if [ -n "$FS_RECORD_SWITCH" ] && [ $FS_RECORD_SWITCH == "ON" ]; then
    python3 uploadWav.py &
fi
/usr/local/freeswitch/bin/freeswitch -nonat
