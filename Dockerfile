FROM python:3.13-alpine AS builder
RUN apk add --no-cache gcc musl-dev libffi-dev
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt


FROM python:3.13-alpine
WORKDIR /app

RUN apk add --no-cache libffi && adduser -D -u 1000 appuser
WORKDIR /app
COPY --from=builder --chown=appuser:appuser /root/.local /home/appuser/.local
COPY --chown=appuser:appuser netbox ./netbox
COPY --chown=appuser:appuser server.py .
COPY --chown=appuser:appuser templates ./templates
COPY --chown=appuser:appuser validators ./validators

USER appuser

EXPOSE 4343

CMD ["python3", "server.py"]
