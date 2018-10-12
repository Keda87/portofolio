FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /sourcecode
WORKDIR /sourcecode
COPY . /sourcecode/

RUN apk update \
    && apk add vim \
    && apk add build-base gcc abuild binutils binutils-doc gcc-doc zlib-dev git

RUN pip install -U pip && pip install -r requirements.txt