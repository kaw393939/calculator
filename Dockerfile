FROM python:3.7

COPY . /web
ENTRYPOINT ["python"]
CMD ["/web/Database/sqlite_create.py"]