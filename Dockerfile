FROM python:3.11
EXPOSE 1326
WORKDIR /opt/app

COPY requirements.txt /opt/app
RUN pip install -r requirements.txt --no-cache-dir --upgrade
RUN apt-get clean \
    && apt-get update \
    && apt-get install -y --no-install-recommends libopenblas-dev
COPY . /opt/app
RUN python3 getmodelupdate.py
CMD ["uvicorn","app:app","--reload","--port","1326","-k","uvicorn.workers.UvicornWorker"]
