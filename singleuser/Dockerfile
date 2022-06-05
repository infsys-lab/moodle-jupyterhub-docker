# Copyright (c) Atreya Shankar
# Distributed under the terms of the MIT License.
# Copyright (c) Jupyter Development Team
# Distributed under the terms of the Modified BSD License.

# Set up defaults
ARG DOCKER_NOTEBOOK_IMAGE
FROM $DOCKER_NOTEBOOK_IMAGE
ARG JUPYTERHUB_VERSION
RUN python3 -m pip install --no-cache-dir jupyterhub==$JUPYTERHUB_VERSION

# Copy .condarc
COPY ./.condarc /home/jovyan/
