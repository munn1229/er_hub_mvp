FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ENV GROUP_ID 1000
ENV USER_ID 1000
ENV USER app
RUN addgroup --gid ${GROUP_ID} ${USER}
RUN adduser --uid ${USER_ID} -gid ${GROUP_ID} --disabled-password --gecos "" app
USER ${USER}

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
