FROM python:3.8
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN chmod 765 /app/bin/main.sh
ENTRYPOINT ["python", "/app/FrontMatterGenerator.py"]
