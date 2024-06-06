FROM python:3.12
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD ["/bin/sh", "/app/init.sh"]