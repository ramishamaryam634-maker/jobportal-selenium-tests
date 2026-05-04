FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    xvfb \
    libnss3 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libxss1 \
    libasound2 \
    libgbm1 \
    fonts-liberation \
    libu2f-udev \
    libvulkan1 \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google.gpg

RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list

RUN apt-get update && apt-get install -y google-chrome-stable

COPY . .

RUN pip install selenium pytest webdriver-manager

CMD ["pytest", "-v"]
