FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN chmod +x /app/capstone.py
CMD ./capstone.py