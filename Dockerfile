FROM python:3.6

WORKDIR /usr/flask/plattshacks

COPY . .

RUN pip install requests
RUN pip install flask

EXPOSE 7070

CMD ["python","app.py"]
