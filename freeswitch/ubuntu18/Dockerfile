FROM ubuntu:18.04

RUN apt-get update && apt-get -yq install git

# RUN git clone https://github.com/signalwire/freeswitch /usr/src/freeswitch
RUN git clone -b v1.10 https://github.com/signalwire/freeswitch.git /usr/src/freeswitch
RUN git clone https://github.com/signalwire/libks /usr/src/libs/libks
RUN git clone https://github.com/freeswitch/sofia-sip /usr/src/libs/sofia-sip
RUN git clone https://github.com/freeswitch/spandsp /usr/src/libs/spandsp
# RUN git clone https://github.com/signalwire/signalwire-c /usr/src/libs/signalwire-c

RUN apt-get -yq install \
# build
    build-essential cmake automake autoconf 'libtool-bin|libtool' pkg-config \
# general
    vim libssl-dev zlib1g-dev libdb-dev unixodbc-dev libncurses5-dev libexpat1-dev libgdbm-dev bison erlang-dev libtpl-dev libtiff5-dev uuid-dev \
# core
    libpcre3-dev libedit-dev libsqlite3-dev libcurl4-openssl-dev nasm \
# core codecs
    libogg-dev libspeex-dev libspeexdsp-dev \
# mod_enum
    libldns-dev \
# mod_python3
    python3-dev \
# mod_av
    libavformat-dev libswscale-dev libavresample-dev \
# mod_lua
    liblua5.2-dev lua-socket lua-cjson \
# mod_opus
    libopus-dev \
# mod_pgsql
    libpq-dev \
# mod_sndfile
    libsndfile1-dev libflac-dev libogg-dev libvorbis-dev
# mod_shout
    # libshout3-dev libmpg123-dev libmp3lame-dev

# RUN cd /usr/src/libs/libks && cmake . -DCMAKE_INSTALL_PREFIX=/usr -DWITH_LIBBACKTRACE=1 && make install
RUN cd /usr/src/libs/libks && cmake . -DCMAKE_INSTALL_PREFIX=/usr && make install
RUN cd /usr/src/libs/sofia-sip && ./bootstrap.sh && ./configure CFLAGS="-g -ggdb" --with-pic --with-glib=no --without-doxygen --disable-stun --prefix=/usr && make -j`nproc --all` && make install
# RUN cd /usr/src/libs/spandsp && ./bootstrap.sh && ./configure CFLAGS="-g -ggdb" --with-pic --prefix=/usr && make -j`nproc --all` && make install
RUN cd /usr/src/libs/spandsp && git reset --hard 67d2455efe02e7ff0d897f3fd5636fed4d54549e && ./bootstrap.sh && ./configure CFLAGS="-g -ggdb" --with-pic --prefix=/usr && make -j`nproc --all` && make install
# RUN cd /usr/src/libs/signalwire-c && PKG_CONFIG_PATH=/usr/lib/pkgconfig cmake . -DCMAKE_INSTALL_PREFIX=/usr && make install

# Enable modules
# RUN sed -i 's|#formats/mod_shout|formats/mod_shout|' /usr/src/freeswitch/build/modules.conf.in
RUN sed -i 's|applications/mod_signalwire|#applications/mod_signalwire|' /usr/src/freeswitch/build/modules.conf.in
RUN sed -i 's|say/mod_say_en|#say/mod_say_en|' /usr/src/freeswitch/build/modules.conf.in
RUN sed -i 's|#say/mod_say_zh|say/mod_say_zh|' /usr/src/freeswitch/build/modules.conf.in
RUN echo 'asr_tts/mod_unimrcp' >> /usr/src/freeswitch/build/modules.conf.in

RUN cd /usr/src/freeswitch && ./bootstrap.sh -j
RUN cd /usr/src/freeswitch && ./configure
RUN cd /usr/src/freeswitch && make -j`nproc` && make install
# RUN make cd-sounds-install && make cd-moh-install

# Cleanup the image
RUN apt-get clean

# Uncomment to cleanup even more
#RUN rm -rf /usr/src/*
