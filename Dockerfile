FROM python:3.6.1

# set working directory
RUN mkdir -p /opt/morpheme
WORKDIR /opt/morpheme

# install requirements
ADD ./requirements.txt /opt/morpheme/requirements.txt
RUN pip install -r requirements.txt

# add code
ADD . /morpheme

# run server
CMD python manage.py runserver -h 0.0.0.0