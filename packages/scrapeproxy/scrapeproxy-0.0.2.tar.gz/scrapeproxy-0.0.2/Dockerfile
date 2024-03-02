FROM python:3.11-slim

ENV USER=tms
ENV GROUP=tms_group
ENV BASEDIR=scrapeproxy


# Create a non-root user and switch to it
RUN addgroup --gid 1000 ${GROUP} && \
    adduser --uid 1000 --ingroup ${GROUP} --home /home/${USER} --shell /bin/sh --disabled-password --gecos "" ${USER}

USER ${USER}
WORKDIR /home/${USER}/app

RUN pip install --user click toml
COPY pyproject.toml /home/${USER}/app/pyproject.toml
COPY --chown=${USER}:${USER} ${BASEDIR}/tools/toml_to_requirements.py /home/${USER}/app/toml_to_requirements.py

RUN python toml_to_requirements.py pyproject.toml requirements.txt
RUN pip install --user -r requirements.txt

COPY --chown=${USER}:${USER} ${BASEDIR} /home/${USER}/app/${BASEDIR}

ENV PACKAGE_VERSION=1.0.0
ENV SETUPTOOLS_SCM_PRETEND_VERSION=1.0.0
RUN pip install -e .

ARG ENV
ENV ENV=${ENV} \
    PATH=/home/${USER}/.local/bin:$PATH