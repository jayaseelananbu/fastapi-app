#base image to create container
FROM python:3.9-slim

#creating work directory inside container
WORKDIR /app

#copying requirements.txt to container work directory
COPY requirements.txt ./

# Installing dependency files inside container
RUN pip3 install --no-cache-dir -r requirements.txt 

#copying all other codes into container work directory
COPY . .

#Exposing container port
EXPOSE 8000