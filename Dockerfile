FROM python:3.9

# Install Docker CLI
RUN apt-get update && apt-get install -y docker.io && apt-get clean

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]
