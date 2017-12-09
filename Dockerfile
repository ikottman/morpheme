FROM nikolaik/python-nodejs:latest

# set working directory
RUN mkdir -p /opt/morpheme
WORKDIR /opt/morpheme

# install python dependencies
COPY ./requirements.txt /opt/morpheme/requirements.txt
RUN pip install -r requirements.txt

# install javascript dependencies
COPY ./package.json /opt/morpheme/package.json
RUN yarn install

# add code
COPY ./manage.py /opt/morpheme
COPY ./src /opt/morpheme/src

# run server
CMD python manage.py runserver -h 0.0.0.0