FROM python

WORKDIR /app

COPY /flask/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY /flask/ .

ENTRYPOINT ["python","main.py"]
