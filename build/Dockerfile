FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# use -u for unbuffered. otherwise logs/stdout of the script gets buffered and not printed until a threshold is reached
CMD [ "python", "-u", "./scanner.py" ]
