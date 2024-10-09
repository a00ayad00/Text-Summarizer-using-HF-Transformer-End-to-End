from python:3.11-slim

run apt update -y && apt install awscli -y

workdir /app
copy . /app
run pip install -r requirements.txt

entrypoint ["python3", "app.py"]