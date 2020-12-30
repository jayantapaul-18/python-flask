FROM python:3.9
RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt
ENV PORT=5000
EXPOSE 5000
CMD ["python", "/app/server.py"]