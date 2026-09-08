FROM python:3.14

WORKDIR /app

COPY addition.py .

CMD ["python", "addition.py"]
