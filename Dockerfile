FROM python:3.13
WORKDIR /app
# Копируем только нужное (игнорируя ненужное через .dockerignore)
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]