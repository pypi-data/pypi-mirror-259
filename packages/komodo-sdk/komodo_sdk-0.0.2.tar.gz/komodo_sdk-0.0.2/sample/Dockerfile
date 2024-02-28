FROM python:3.11

WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN pip3 install -r requirements.txt

COPY komodo /code/komodo/
COPY sample /code/sample/

EXPOSE 8042
CMD ["gunicorn"  , "--bind", "0.0.0.0:8042", "sample.server:SAMPLE_APP", "--workers", "8", "--timeout", "300"]
