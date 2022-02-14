FROM python:3.7-alpine
COPY app.py /
CMD ["python", "app.py"]