FROM tiangolo/uwsgi-nginx-flask:python3.6

FROM python:3.6-slim
COPY ./app.py /deploy/
COPY ./requirements.txt /deploy/
COPY ./brain.dump /deploy/
COPY ./std-startup.aiml /deploy/
WORKDIR /deploy/
RUN apt-get update && apt-get install -y gcc
RUN pip3 install -r requirements.txt
RUN pip3 install flask
RUN pip3 install gunicorn
RUN pip3 install --upgrade pip
RUN apt-get install -y gunicorn
RUN apt-get install -y python-gevent


# ssh
ENV SSH_PASSWD "root:Docker!"
RUN apt-get update \
        && apt-get install -y --no-install-recommends dialog \
        && apt-get update \
	&& apt-get install -y --no-install-recommends openssh-server \
	&& echo "$SSH_PASSWD" | chpasswd 

COPY sshd_config /etc/ssh/
COPY init.sh /usr/local/bin/

RUN chmod u+x /usr/local/bin/init.sh
EXPOSE 8000 2222

#CMD ["python", "/code/manage.py", "runserver", "0.0.0.0:8000"]
ENTRYPOINT ["init.sh"]


