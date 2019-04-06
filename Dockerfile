FROM python:3
ADD my_script.py /
RUN pip install requests
RUN pip install vaderSentiment
CMD [ "python", "./my_script.py" ]