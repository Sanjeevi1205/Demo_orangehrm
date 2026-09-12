FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN python -m playwright install chromium

COPY . .

RUN mkdir -p reports
RUN mkdir -p screenshots
RUN mkdir -p videos

ENTRYPOINT ["python", "-m", "behave"]