FROM python:3.10.1

ADD ./ /api

WORKDIR /api

RUN pip install -r requirements.txt

CMD ["python", "main.py"]