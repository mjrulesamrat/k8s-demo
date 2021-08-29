FROM python:3.9-slim
WORKDIR /bank-service
RUN apt-get update && \
    apt-get upgrade -y
ADD . ./
RUN pip install -r requirements.txt
EXPOSE 8000
CMD uvicorn run:app --reload
