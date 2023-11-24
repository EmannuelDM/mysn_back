FROM python:3.10

WORKDIR /app

COPY . /app
COPY pyproject.toml /app 

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
