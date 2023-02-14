FROM python:3.10-alpine

RUN apk update \
    && apk add build-base linux-headers
COPY . /src/memory_service
WORKDIR /src/memory_service


RUN pip install --upgrade pip
COPY ./requirements.txt /src/memory_service
RUN pip install -r /src/memory_service/requirements.txt

EXPOSE 5000

CMD ["python", "wsgi.py"]