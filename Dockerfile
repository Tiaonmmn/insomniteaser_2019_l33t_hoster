from tiaonmmn/alpine-apache2-php7
LABEL Author="eboda"
COPY files/ /tmp/
RUN mv /tmp/app/* /app/public/ &&\
    mv /tmp/flag / && mv /tmp/get_flag / &&\
    chmod 400 /flag && chmod u+s+x /get_flag &&\
    mkdir /app/public/images &&\
    chown -R apache:apache /app/public/
EXPOSE 80