FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


RUN curl -sL https://github.com/allure-framework/allure2/releases/download/2.32.2/allure-2.32.2.tgz | tar -xz -C /opt \
    && ln -s /opt/allure-2.32.2/bin/allure /usr/local/bin/allure

COPY . .

CMD ["pytest", "--alluredir=allure-results"]
