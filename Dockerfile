FROM python:3.7

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip==20.1.1
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000" ] 
 