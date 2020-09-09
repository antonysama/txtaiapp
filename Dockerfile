FROM python:3.8-slim-buster
RUN apt-get update && apt-get install -y g++
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./ /app/

# ENTRYPOINT ["python"]
# CMD ["app.py"]
