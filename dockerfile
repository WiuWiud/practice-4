FROM python:3.12-slim
RUN useradd -m -u 10009 appuser
WORKDIR /app
COPY app.py .
COPY disk_check.py .
RUN mkdir -p /data && chown appuser:appuser /data
USER appuser
EXPOSE 8009
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8009/health')" || exit 1
CMD ["python", "app.py"]