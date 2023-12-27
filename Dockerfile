FROM python:3.11.2-slim-bullseye

RUN apt-get update && \
    apt-get upgrade --yes

RUN useradd --create-home cubuff
USER cubuff
WORKDIR /home/cubuff

ENV PYTHONUNBUFFERED=1
ENV VIRTUALENV=/home/cubuff/venv
RUN python3 -m venv $VIRTUALENV
ENV PATH="$VIRTUALENV/bin:$PATH"

RUN python -m pip install --upgrade pip

COPY --chown=cubuff app.py app.py
COPY --chown=cubuff test_app.py test_app.py

RUN python -m unittest test_app.py

CMD ["python", "app.py"]