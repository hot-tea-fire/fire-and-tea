
FROM     test_log:1.0
COPY     supervisor_config/supervisord.conf /etc/
ENV      PYTHONIOENCODING=utf-8

RUN    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN    echo 'Asia/Shanghai' >/etc/timezone

# CMD    python /package/yucenpu/project/main.py

CMD    /usr/local/bin/supervisord -c /etc/supervisord.conf
