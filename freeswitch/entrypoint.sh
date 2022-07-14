#!/bin/sh

get_password() {
    < /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-12};echo;
}

if [ ! -f "/etc/freeswitch/freeswitch.xml" ]; then
    #SIP_PASSWORD=$(get_password)
    SIP_PASSWORD=speech,123
    #sed -i -e "s/default_password=.*\?/default_password=$SIP_PASSWORD\"/" /etc/freeswitch/vars.xml
    echo "New FreeSwitch password for SIP calls set to '$SIP_PASSWORD'"
fi

trap '/usr/bin/freeswitch -stop' SIGTERM
/usr/bin/freeswitch -nc -nf -nonat &
pid="$!"

# python http server
pushd /usr/share/freeswitch/scripts/httpCallout/
nohup sh server.sh &
popd

wait $pid
exit 0
