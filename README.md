# moodle-jupyterhub-docker

This repository documents a docker sandbox environment to test integration between the [Moodle](https://moodle.org/) LMS and [JupyterHub](https://jupyter.org/hub) and was extensively used to test LTI (v1.1) authentication from Moodle to JupyterHub using the LTI [Authenticator](https://github.com/jupyterhub/ltiauthenticator) library. This repository was adapted from the existing [`jupyterhub-deploy-docker`](https://github.com/jupyterhub/jupyterhub-deploy-docker) project, which is distributed under the [BSD 3-Clause License](THIRD_PARTY_NOTICES). In addition, docker images for the Moodle LMS were pulled from [Bitnami](https://hub.docker.com/u/bitnami). 

**Disclaimer:** The source code in this repository is meant solely for testing purposes and is not designed for production use.

## Dependencies :mag:

Since this repository operates on the level of docker containers, working installations of `docker` and `docker-compose` are required. This repository was tested against versions `20.10.16` and `2.5.1` respectively.

In the next steps, we assume that the user executing commands is part of the `docker` group and therefore can execute `docker` commands without superuser privileges (or `sudo`). If this is not the case for your environment, then the commands below must be executed with superuser privileges (or `sudo`).

## Usage :snowflake:

<details><summary>Build</summary><p> 

To build relevant docker images and generate secret data, simply execute:

```
$ make build
```

The following will be generated and dumped as files in `jupyterhub/secrets/`:

1. A randomly generated `postgres` password for the `jupyterhub` database
2. A randomly generated LTI client key and shared secret
3. An admins file for granting administrative rights to the `admin` user

</p></details>
<details><summary>Up</summary><p> 

To create and start relevant containers, simply execute:

```
$ make up
```

This will detach as a background process and it can take several minutes for the installation of Moodle to finish. Open [`http://localhost`](http://localhost) in your browser to access the Moodle UI.

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

## Guide :book:

Follow the instructions below to test LTI authentication from Moodle to JupyterHub:

1. Execute the following to launch all docker services:

    ```
    $ make up
    ```

    **Note:** The installation of Moodle can take several minutes to complete. Execute `make log` to view live installation logs.

2. Open [`http://localhost`](http://localhost) in your browser and log in with `admin` as the username and `password` as the password.

3. After logging in, select the following sequence of options:

    **Site home** > :gear: > **Restore** > **Choose a file** > **Upload a file** > Navigate filesystem and select `moodle-courses/lti_template.mbz` > **Upload this file** > **Restore**
    
4. You will then be directed to a set of pages to refine how the restoration is done. On page *2. Destination*, select the option to continue via **Restore as a new course**. Update preferences or accept defaults on pages 3-5. If all goes well, select **Perform restore** on page 5.

5. Navigate to **Site home** and select the **Test** course. 

6. Select **Turn editing on** and select **Edit** > **Edit settings** options corresponding to the green puzzle-shaped icon with the **JupyterHub** tag.

7. Then select the :gear: button in the **Preconfigured tool** field.

8. Copy the LTI client key from `jupyterhub/secrets/lti.key` and paste it in the **Consumer key** field. Copy the LTI shared secret from `jupyterhub/secrets/lti.secret` and paste it in the **Shared secret** field.

9. Select **Save changes** and then return to the **Test** course.

10. Select the green puzzle-shaped icon with the **JupyterHub** tag and you will be authenticated to `jupyterhub` as the `admin` user.
