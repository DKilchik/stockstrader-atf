FROM python:3.11-slim

# Установка необходимых системные пакеты
RUN apt-get update && apt-get install -y \
    curl unzip gnupg ca-certificates fonts-liberation \
    libnss3 libatk-bridge2.0-0 libxss1 libgtk-3-0 libasound2 libgbm1 libxshmfence1 \
    libxrandr2 libxi6 openjdk-17-jre-headless wget \
    && rm -rf /var/lib/apt/lists/*

# Установка Google Chrome
RUN wget https://storage.googleapis.com/chrome-for-testing-public/139.0.7258.66/linux64/chrome-linux64.zip \
    && unzip chrome-linux64.zip \
    && mv chrome-linux64 /opt/chrome \
    && ln -s /opt/chrome/chrome /usr/bin/google-chrome \
    && rm chrome-linux64.zip

# Установка ChromeDriver
RUN wget https://storage.googleapis.com/chrome-for-testing-public/139.0.7258.66/linux64/chromedriver-linux64.zip \
    && unzip chromedriver-linux64.zip \
    && mv chromedriver-linux64/chromedriver /usr/local/bin/chromedriver \
    && chmod +x /usr/local/bin/chromedriver \
    && rm -rf chromedriver-linux64.zip chromedriver-linux64

# Установка Allure CLI
RUN wget https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.tgz \
    && tar -zxvf allure-2.27.0.tgz -C /opt/ \
    && ln -s /opt/allure-2.27.0/bin/allure /usr/bin/allure \
    && rm allure-2.27.0.tgz

# Создаём рабочую директорию
WORKDIR /tests

# Устанавливаем зависимости
COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Копируем весь проект внутрь контейнера
COPY . .

# Команда по умолчанию
CMD ["pytest", "--alluredir=allure-results"]
