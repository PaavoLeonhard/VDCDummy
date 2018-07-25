FROM python:3


COPY ./start.sh start.sh

ADD VDCDummy VDCDummy
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
#EXPOSE 8000
#EXPOSE 8080

#CMD ["sh","start.sh"]
CMD ["python", "VDCDummy/manage.py", "runserver", "0.0.0.0:8000"]