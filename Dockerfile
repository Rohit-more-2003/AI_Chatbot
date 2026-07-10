FROM python:3.12-alpine

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

EXPOSE 7860

CMD ["python", "main.py"]