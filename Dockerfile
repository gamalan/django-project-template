FROM python:3.7-alpine

RUN adduser -D app && \
    adduser app tty && \
    mkdir -p /opt/service/app && \
    mkdir -p /root/.local

ENV ENVIRONMENT 'production'
COPY . /opt/service/app

RUN chown app:app -R /opt/service
WORKDIR /opt/service/app

RUN apk add --no-cache libstdc++ openblas nginx wget curl && \
    apk add --no-cache --virtual=.build-dependency libffi-dev openssl-dev gfortran gcc g++ file binutils musl-dev openblas-dev git
RUN pip install --no-cache-dir pipenv supervisor
USER app
RUN pipenv install
RUN pipenv run python /opt/service/app/manage.py collectstatic --noinput
USER root
RUN apk del .build-dependency && \
    rm /etc/nginx/conf.d/default.conf && \
    mkdir /run/nginx && \
    sed -i 's/user nginx/user app/g' /etc/nginx/nginx.conf
COPY config/nginx/* /etc/nginx/conf.d/

EXPOSE 8080
ENTRYPOINT ["./boot.sh"]