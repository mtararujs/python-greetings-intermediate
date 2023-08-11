FROM python:3-alpine

WORKDIR /python-app
COPY requirements.txt requirements.txt
COPY app.py app.py
RUN pip install -r requirements.txt

EXPOSE 3000 

ENTRYPOINT ["python"]
CMD ["app.py"]
