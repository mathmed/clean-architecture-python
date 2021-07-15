
FROM python:3.8

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod 755 /usr/local/bin/entrypoint.sh \
    && ln -s /usr/local/bin/entrypoint.sh /
    
ENTRYPOINT [ "entrypoint.sh" ]