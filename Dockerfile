FROM python:3.9.7

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8008

CMD ["uvicorn", "postgresfilejemacode:bhargav12", "--host", "0.0.0.0", "--port", "8008"]
