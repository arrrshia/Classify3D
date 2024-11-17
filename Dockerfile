FROM python:3.9

RUN apt-get update && apt-get install -y && apt-get clean

ENV PORT=${PORT:-5000}

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD flask run --host=0.0.0.0 --port=${PORT}
