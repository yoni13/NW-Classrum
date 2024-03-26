FROM python:3.11
EXPOSE 1326
WORKDIR /opt/app
RUN \
    if [ `dpkg --print-architecture` = "armhf" ]; then \
    printf "[global]\nextra-index-url=https://www.piwheels.org/simple\n" > /etc/pip.conf ; \
    fi
COPY requirements.txt /opt/app
RUN pip install -r requirements.txt --no-cache-dir --upgrade --no-install-recommends
RUN apt-get clean \
    && apt-get update \
    && apt-get install -y --no-install-recommends libopenblas-dev
COPY . /opt/app
RUN python3 getmodelupdate.py
CMD ["gunicorn", "--bind", "0.0.0.0:1326", "app:app"]
