FROM alpine

ENV FRP_VERSION 0.51.0
ENV FRP_ARCHT linux_amd64
ENV FRP_FOLDER frp_${FRP_VERSION}_${FRP_ARCHT}
ENV FRP_TGZ ${FRP_FOLDER}.tar.gz

RUN cd /root \
    &&  wget --no-check-certificate -c https://github.com/fatedier/frp/releases/download/v${FRP_VERSION}/${FRP_TGZ} \
    &&  tar zxvf ${FRP_TGZ} \
    &&  cd ${FRP_FOLDER}/ \
    &&  cp frpc /usr/bin/ \
    &&  mkdir -p /etc/frp \
    &&  cp frpc.ini /etc/frp \
    &&  cd /root \
    &&  rm ${FRP_TGZ} \
    &&  rm -rf {FRP_FOLDER}/ 

ENTRYPOINT /usr/bin/frps -c /etc/frp/frps.ini
