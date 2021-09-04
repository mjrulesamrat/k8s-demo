FROM python:3.9-slim
COPY . /professor-service
WORKDIR /professor-service
RUN apt-get update && \
    apt-get upgrade -y
ADD . ./
RUN pip install -r requirements.txt
EXPOSE 8081
CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "8081"]
