FROM ubuntu:18.04

ENV IPMIEXPORTER_VERSION 1.6.1
ENV IPMIEXPORTER_ARCHT linux-amd64
ENV IPMIEXPORTER_FOLDER ipmi_exporter-${IPMIEXPORTER_VERSION}.${IPMIEXPORTER_ARCHT}
ENV IPMIEXPORTER_TGZ ${IPMIEXPORTER_FOLDER}.tar.gz

RUN apt-get update \
    && apt-get install wget freeipmi-tools -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

RUN cd /root \
    &&  wget --no-check-certificate -c https://github.com/prometheus-community/ipmi_exporter/releases/download/v${IPMIEXPORTER_VERSION}/${IPMIEXPORTER_TGZ} \
    &&  tar zxvf ${IPMIEXPORTER_TGZ} \
    &&  cd ${IPMIEXPORTER_FOLDER}/ \
    &&  cp ipmi_exporter /usr/bin/ \
    &&  cd /root \
    &&  rm ${IPMIEXPORTER_TGZ} \
    &&  rm -rf {IPMIEXPORTER_FOLDER}/

ENTRYPOINT /usr/bin/ipmi_exporter --config.file=/ipmi_root/ipmi_remote.yml
