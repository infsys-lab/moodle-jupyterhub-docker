#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Atreya Shankar
# Distributed under the terms of the MIT License.
# Copyright (c) Jupyter Development Team
# Distributed under the terms of the Modified BSD License.

# Get relevant import(s)
import os
import sys

# Get environmental variables and configurations
c = get_config()  # noqa
network_name = os.environ.get("DOCKER_NETWORK_NAME", "jupyterhub-network")
notebook_dir = os.environ.get("DOCKER_NOTEBOOK_DIR", "/home/jovyan")
data_dir = os.environ.get("JH_DATA_VOLUME_CONTAINER", "/data")

# Configure docker spawner
c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"
c.DockerSpawner.default_url = "/lab"
c.DockerSpawner.image = os.environ["DOCKER_NOTEBOOK_IMAGE"]
c.DockerSpawner.extra_create_kwargs.update({
    "user": "root",
})
c.DockerSpawner.environment = {
    "GRANT_SUDO": "1",
    "JUPYTER_ENABLE_LAB": "1",
}
c.DockerSpawner.mem_limit = "2G"
c.DockerSpawner.cpu_limit = 0.5
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = network_name
c.DockerSpawner.extra_host_config = {"network_mode": network_name}
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = {"jupyterhub-user-{username}": notebook_dir}
c.DockerSpawner.remove = True
c.DockerSpawner.debug = True

# Configure ports and ip's
c.JupyterHub.hub_ip = "jupyterhub"
c.JupyterHub.port = 8080

# Configure LTI authenticator
with open(os.environ["LTI_KEY"]) as input_file_stream:
    lti_key = input_file_stream.readlines()[0].strip()
with open(os.environ["LTI_SECRET"]) as input_file_stream:
    lti_secret = input_file_stream.readlines()[0].strip()
c.JupyterHub.authenticator_class = "ltiauthenticator.LTIAuthenticator"
c.LTI11Authenticator.username_key = "ext_user_username"
c.LTI11Authenticator.consumers = {lti_key: lti_secret}

# Persist hub data on volume mounted inside container
c.JupyterHub.cookie_secret_file = os.path.join(data_dir,
                                               "jupyterhub_cookie_secret")

# Modify hub database to postgres
c.JupyterHub.db_url = "postgresql://postgres:{password}@{host}/{db}".format(
    host=os.environ["POSTGRES_HOST"],
    password=os.environ["POSTGRES_PASSWORD"],
    db=os.environ["POSTGRES_DB"])

# Update admins
c.Authenticator.admin_users = admin = set()
c.JupyterHub.admin_access = True
with open(os.path.join(os.path.dirname(__file__), "admins")) as stream:
    for line in stream:
        if not line:
            continue
        else:
            admin.add(line.strip())

# Update services
c.JupyterHub.services = [{
    "name":
    "idle-culler",
    "admin":
    True,
    "command":
    [sys.executable, "-m", "jupyterhub_idle_culler", "--timeout=43200"],
}]
