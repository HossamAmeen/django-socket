FROM python:3

ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN useradd -ms /bin/bash hossam
ENV PATH="/home/hossam/.local/bin:${PATH}"

USER hossam
COPY --chown=hossam . /home/hossam/

RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir -r /home/hossam/requirments.txt

WORKDIR /home/hossam/

EXPOSE 8000

ENTRYPOINT daphne notification_project.asgi:application --port 8000 --bind 0.0.0.0