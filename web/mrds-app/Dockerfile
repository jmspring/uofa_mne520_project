FROM alpine:edge

RUN apk add --no-cache --update openblas openblas-dev \
    proj-util perl python3 py3-pip python3-dev py3-wheel \
    alpine-sdk musl-dev geos-dev geos gdal nginx uwsgi \
    gdal-dev py3-flask freetds-dev openssl-dev proj-dev \
    uwsgi-python3

WORKDIR /usr/src/app

COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

COPY ./app/ .
COPY wsgi.ini .

#CMD ["uwsgi", "wsgi.ini"]
CMD ["sleep", "10000"]

