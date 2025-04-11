FROM joyzoursky/python-chromedriver:3.8

ENV PYTHONDONTWRITEBYTECODE=1
# Устанавливает переменную окружения, которая гарантирует, что вывод из python будет отправлен прямо в терминал без предварительной буферизации
ENV PYTHONUNBUFFERED=1

WORKDIR /src
COPY requirements.txt /src
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
