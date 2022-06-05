# moodle-jupyterhub-docker

This repository documents a dockerized JupyterHub build with docker-spawned individual Jupyter servers. This project has been adapted from the existing [`jupyterhub-deploy-docker`](https://github.com/jupyterhub/jupyterhub-deploy-docker) repository, which is distributed under the [BSD 3-Clause License](THIRD_PARTY_NOTICES).

In addition, we also provide docker containers for `moodle` in order to simulate the interaction between a LMS and JupyterHub.

## Dependencies :mag:

Since this repository operates on the level of docker containers, working installations of `docker` and `docker-compose` are required. Source code in this repository was tested with versions `20.10.*` and `2.*` respectively.

## Usage :snowflake:

<details><summary>1. Build </summary><p>

To build the `jupyterhub`, `postgres` and `jupyterhub-user` docker images, simply execute:

```
$ make build
```

The following will be generated and dumped in `jupyterhub/secrets/`:

1. A OpenSSL private key and self-signed SSL certificate for encrypted communication
2. An admins file for granting administrative rights to the `admin` user
3. A randomized `postgres` password for the `jupyterhub` database

</p></details>
<details><summary>2. Up</summary><p>

To start the `jupyterhub` and `postgres` containers, simply execute:

```
$ make up
```

This will detach as a background process. Open `https://127.0.0.1` in your browser to access the UI.

</p></details>
<details><summary>3. Down</summary><p>

To stop and remove relevant docker containers, simply execute:

```
$ make down
```

</p></details>
<details><summary>4. Restart</summary><p>

To hard-restart all containers, simply execute

```
$ make restart
```

**Note:** This will stop/remove all containers and rebuild images from scratch. This is useful for testing changes in configurations

</p></details>
<details><summary>5. Clean</summary><p>

To delete all dangling networks, volumes and data in `jupyterhub/secrets`, simply execute:

```
$ make clean
```

</p></details>
