
FROM python:3.11.2


RUN apt-get update && apt-get upgrade
RUN mkdir -p /app/backend

WORKDIR /app/backend

# install the dependencies
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

# copy source code
COPY . /app

# start backend service
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

