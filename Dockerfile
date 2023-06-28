FROM python:3.10.11-slim

WORKDIR /usr/src/app

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]