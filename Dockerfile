FROM python:3.8-slim-buster
LABEL "maintainer" = "debugicu <debugicu@163.com>"

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "FrontMatterGenerator.py"]
