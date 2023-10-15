FROM python:3.11.0

# same as running python with "-u"
ENV PYTHONUNBUFFERED 1

RUN mkdir /ADPB
COPY . /ADPB/
WORKDIR /ADPB

RUN pip install -r requirements.txt
