FROM python:3.9-slim

# Install Default JRE
RUN apt-get update && \
    apt-get install -y default-jre && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY atlassian-agent.jar .
COPY app.py .
COPY templates/ templates/

EXPOSE 5000

CMD ["python", "app.py"]
