FROM php:8.2-fpm-alpine

WORKDIR /app

RUN apk update
RUN apk add --no-cache \
  npm \
  freetype-dev libjpeg-turbo-dev libpng-dev libmcrypt-dev postgresql-dev oniguruma-dev \
  git vim unzip tzdata bash sudo mysql-client postgresql-client \
  libmcrypt-dev libltdl libzip-dev \
  && cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
  && apk del tzdata \
  && rm -rf /var/cache/apk/*

# phpredis download
RUN git clone -b 6.0.2 --depth 1 https://github.com/phpredis/phpredis.git /usr/src/php/ext/redis

# install pdo, etc...
RUN docker-php-source extract
RUN docker-php-ext-install pdo_mysql mysqli pdo_pgsql mbstring gd redis zip

# configuration
COPY ./php.ini /usr/local/etc/php/php.ini

# developer
ENV GROUP_ID 1000
ENV USER_ID 1000
ENV USER app

RUN addgroup -g ${GROUP_ID} ${USER}
RUN adduser -u ${USER_ID} -G ${USER} -D  -s /bin/ash -h /home/${USER} ${USER} 

ADD .profile /home/${USER}/
RUN chown ${USER}:${USER} /home/${USER}/.profile
ADD .profile /home/${USER}/.bashrc
RUN chown ${USER}:${USER} /home/${USER}/.bashrc

RUN mkdir /var/log/php && chown ${USER}:${USER} /var/log/php

# install composer
ENV COMPOSER_ALLOW_SUPERUSER=1
ENV COMPOSER_HOME=/composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN chown -R ${USER}:${USER} /composer

USER ${USER}
