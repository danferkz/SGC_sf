FROM python

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade setuptools 

COPY . .

EXPOSE 8000

CMD ["python", "main/manage.py", "runserver", "0.0.0.0:8000"]
