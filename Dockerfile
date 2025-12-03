FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install flask
CMD ["python","random_num.py"]