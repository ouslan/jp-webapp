FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000

COPY . .

# Run the application
CMD ["python", "main.py"]
