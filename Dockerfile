FROM python:3.9

WORKDIR /app
COPY . /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH="${PYTHONPATH}:app"

CMD python get_raw_data.py
CMD python financial/api/v1/api.py
