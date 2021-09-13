FROM python:3

LABEL repository="https://github.com/sebw/shaarli-reminder"

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY remind.py /usr/src/app/remind.py

CMD ["python", "/usr/src/app/remind.py"]