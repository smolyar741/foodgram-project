FROM python:3.8.5
WORKDIR /code
COPY . /code
RUN pip install pip --upgrade && pip install -r requirements.txt
ENTRYPOINT ["/code/commands.sh"]