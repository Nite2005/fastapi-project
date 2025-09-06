FROM Python:3.10

WORKDIR /app

COPY . .

RUN pip  install --no-cache-dir --upgrade pip && \
    pip install --no-cacahe-dir -r requirements.txt


CMD ["uvicorn","app.main:app","--host","0.0.0.0","port","8000"]