FROM python:3
WORKDIR /app/api
COPY . ./
RUN pip install -r requirements.txt
RUN ["chmod", "+x", "/app/api/startup.sh"]
EXPOSE 8000
ENTRYPOINT ["/app/api/startup.sh"]