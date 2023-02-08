FROM tensorflow/tensorflow:2.11.0 AS tf-cpu
WORKDIR /app
COPY requirements.txt .
RUN /usr/bin/python3 -m pip install --upgrade pip && \
    pip install -r requirements.txt

