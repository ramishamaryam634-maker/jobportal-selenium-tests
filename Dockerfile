FROM python:3.10-slim

WORKDIR /app

# Install Google Chrome and required libraries

RUN apt-get update && apt-get install -y \

    wget \

    curl \

    unzip \

    gnupg \

    xvfb \

    libxi6 \

    libgconf-2-4 \

    libnss3 \

    libatk-bridge2.0-0 \

    libgtk-3-0 \

    libxss1 \

    libasound2 \

    libgbm1 \

    libu2f-udev \

    fonts-liberation \

    && rm -rf /var/lib/apt/lists/*

# Add Google Chrome

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -

RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'

RUN apt-get update && apt-get install -y google-chrome-stable

# Copy project files

COPY . .

# Install python libraries

RUN pip install selenium pytest webdriver-manager

CMD ["pytest"]
