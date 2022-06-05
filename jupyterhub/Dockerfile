# Copyright (c) Atreya Shankar
# Distributed under the terms of the MIT License.
# Copyright (c) Jupyter Development Team
# Distributed under the terms of the Modified BSD License.

# Pull base image
ARG JUPYTERHUB_VERSION
FROM jupyterhub/jupyterhub-onbuild:$JUPYTERHUB_VERSION

# Install dockerspawner and postgres
RUN python3 -m pip install --no-cache-dir psycopg2-binary==2.9.1 \
    dockerspawner==12.1.0 jupyterhub-idle-culler==1.2.1 \
    jupyterhub-ltiauthenticator==1.3.0

# Copy LTI certificate and key
ENV LTI_KEY /srv/jupyterhub/secrets/lti.key
ENV LTI_SECRET /srv/jupyterhub/secrets/lti.secret
COPY ./secrets/lti.key "$LTI_KEY"
COPY ./secrets/lti.secret "$LTI_SECRET"
RUN chmod 700 /srv/jupyterhub/secrets && \
    chmod 600 /srv/jupyterhub/secrets/*

# Copy admins file
COPY ./secrets/admins /srv/jupyterhub/admins
