FROM python:3.13
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY netbox.py .
COPY server.py .
COPY templates ./templates

EXPOSE 4343

ENTRYPOINT ["python3", "server.py"]
