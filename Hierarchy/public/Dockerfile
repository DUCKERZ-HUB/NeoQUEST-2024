FROM python:3  

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 25555

CMD ["python3", "host.py"]
