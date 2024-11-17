FROM python:3.9

RUN apt-get update && apt-get install -y docker.io && apt-get clean

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

CMD flask run --host=0.0.0.0 --port=5500
