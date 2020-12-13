FROM ubuntu:18.04
RUN sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list
RUN apt update && DEBIAN_FRONTEND=noninteractive apt install -y php && rm /var/www/html/index.html
ENV TZ=Asia/Shanghai
RUN ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN dpkg-reconfigure --frontend noninteractive tzdata
COPY php.ini /etc/php/7.2/apache2/php.ini
COPY index.php /var/www/html
COPY entrypoint.sh /
CMD ["/entrypoint.sh"]
