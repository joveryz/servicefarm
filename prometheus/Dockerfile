FROM prom/prometheus

USER root

ENTRYPOINT [ "/bin/prometheus" ]

CMD [ "--config.file=/prometheus_root/config/prometheus.yml", \
      "--web.read-timeout=5m", \
      "--web.max-connections=10", \
      "--storage.tsdb.retention=30d", \
      "--storage.tsdb.path=/prometheus_root/data", \
      "--query.max-concurrency=20", \
      "--query.timeout=2m" ]
