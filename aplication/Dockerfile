FROM python:3.9
WORKDIR /app
COPY lib.txt .
RUN pip install --no-cache-dir -r lib.txt
COPY app.py .
EXPOSE 4500
CMD ["python", "app.py"]

