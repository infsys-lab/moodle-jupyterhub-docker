# moodle-jupyterhub-docker

This repository documents a docker sandbox environment to test integration between the [Moodle](https://moodle.org/) LMS and [JupyterHub](https://jupyter.org/hub). This repository was extensively used to test LTI (v1.1) authentication from Moodle to JupyterHub using the LTI [Authenticator](https://github.com/jupyterhub/ltiauthenticator) library.

This repository was extensively adapted from the existing [`jupyterhub-deploy-docker`](https://github.com/jupyterhub/jupyterhub-deploy-docker) project, which is distributed under the [BSD 3-Clause License](THIRD_PARTY_NOTICES.txt). In addition, docker images for the Moodle LMS were pulled from [Bitnami](https://hub.docker.com/u/bitnami). 

**Disclaimer:** The source code in this repository is meant solely for testing purposes and is not designed for production use.

## Dependencies :mag:

Since this repository operates on the level of docker containers, working installations of `docker` and `docker-compose` are required. This repository was tested against versions `20.10.16` and `2.5.1` respectively.

## Usage :snowflake:

<details><summary>Build</summary><p> 

To build relevant docker images and generate secret data, simply execute:

```
$ make build
```

The following will be generated and dumped as files in `jupyterhub/secrets/`:

1. A randomized `postgres` password for the `jupyterhub` database
2. A randomly generated LTI client key and shared secret
3. An admins file for granting administrative rights to the `admin` user

</p></details>
<details><summary>Up</summary><p> 

To create and start relevant containers, simply execute:

```
$ make up
```

This will detach as a background process and it can take several minutes for the installation of Moodle to finish. Open `http://localhost` in your browser to access the Moodle UI.

</p></details>
<details><summary>Log</summary><p> 

To view logs from launched docker containers, simply execute:

```
$ make log
```

</p></details>
<details><summary>Down</summary><p> 

To stop and remove previously created docker containers and networks, simply execute:

```
$ make down
```

</p></details>
<details><summary>Restart</summary><p> 

To restart all containers, simply execute:

```
$ make restart
```

**Note:** This will stop/remove all containers and rebuild images from scratch. This is useful for testing changes in configurations.

</p></details>
<details><summary>Clean</summary><p> 

To stop and remove previously created docker containers, networks, volumes and secret data, simply execute.

```
$ make clean
```

</p></details>
