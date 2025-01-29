FROM python:3.11
EXPOSE 1326
WORKDIR /opt/app

COPY requirements.txt /opt/app
RUN pip install -r requirements.txt --no-cache-dir --upgrade
RUN apt-get clean \
    && apt-get update \
    && apt-get install -y --no-install-recommends libopenblas-dev
ADD --checksum=sha256:73993ed4b440460825f21611731564503cc1d5a0c123746477da6cd574f34885 https://github.com/airockchip/rknn-toolkit2/raw/refs/tags/v2.3.0/rknpu2/runtime/Linux/librknn_api/aarch64/librknnrt.so /usr/lib/
COPY . /opt/app
CMD ["gunicorn","app:app","-k","uvicorn.workers.UvicornWorker","--bind","0.0.0.0:1326"]
