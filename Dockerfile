FROM tiangolo/uvicorn-gunicorn:python3.7
# Update packages
RUN apt-get update -y
RUN python3.7 -m pip install six pytest scipy
# Set Asia/Kolkata Timezone
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata
RUN ln -fs /usr/share/zoneinfo/Asia/Kolkata /etc/localtime
RUN dpkg-reconfigure --frontend noninteractive tzdata
# Create code directory
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code
# Install requirements
RUN python3 -m pip install -r requirements.txt
# Expose port
EXPOSE 8000
RUN mkdir -p /var/log
CMD ["./startup.sh"]