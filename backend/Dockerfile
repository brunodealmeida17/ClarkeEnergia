# Usar uma imagem base do Python
FROM python:3.9-slim

WORKDIR /app


COPY . /app


RUN pip install --no-cache-dir -r requirements.txt


COPY . .

EXPOSE 5000

CMD ["python", "main.py"]
