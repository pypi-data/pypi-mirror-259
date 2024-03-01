### navigation

- [navigation](#navigation)
- [how to run code](#how-to-run-code)
- [how to run tests](#how-to-run-tests)
- [how to run code in docker](#how-to-run-code-in-docker)
  - [Features:](#features)
  - [Getting started](#getting-started)
  - [Start the API container in production mode](#start-the-api-container-in-production-mode)
  - [Start the API container locally for development](#start-the-api-container-locally-for-development)
  - [Stopping the services](#stopping-the-services)
  - [Rebuilding images](#rebuilding-images)
  - [Delete project](#delete-project)
- [command line arguments](#command-line-arguments)
- [documentation](#documentation)

### how to run code

```shell
git clone https://github.com/gmankab/magnus_backend
python magnus_backend/magnus.py
```

### how to run tests

```shell
git clone https://github.com/gmankab/magnus_backend
python magnus_backend/magnus.py --tests
```

### how to run code in docker

#### Features:
* PostgreSQL as a project database
* Adminer for database administration
* Docker containers for easy deployment

#### Getting started
Configure Environment Variables:
   * Create a `.env` file and populate it using the provided `.env.example` as a template. You can use the variables from the example without changes or create a copy and rename it to `.env`.
```
cp .env.example .env
```

#### Start the API container in production mode
```
make start-prod
```

#### Start the API container locally for development
```
make start-dev
```

#### Stopping the services
To stop the services, use the following command:

```
make down
```

#### Rebuilding images
If you make changes to the Dockerfile or dependencies, rebuild the images with:
```
make start-prod-rebuild
```
or
```
make start-dev-rebuild
```

#### Delete project
```
make delete
```

### command line arguments

- `-h`, `--help` - show this help message and exit
- `--reload` - enable uvicorn reloading
- `--noreload` - disable uvicorn reloading
- `--clean` - delete .venv dir, stop all containers and delete all podman and docker data
- `--podman` - run code in podman container
- `--podman_rebuild` - rebuild podman container and run code
- `--systemd` - generate systemd service
- `--update_req_txt` - update requirements.txt file to newest versions
- `--install_req` - install all requirements via pip
- `--autotests` - run autotests
- `--db_url` - set url for database, default is in-memory sqlite
- postgresql url example:
```
--db_url=postgres://my_username:my_password@my_server_ip_adress:5432/my_database_name
```

### documentation

- [adminer](http://localhost:8888)
- [fastapi automatic api docs](http://localhost:8000/docs)
- [github api docs](docs/api_docs.md)
- [database roadmap](https://github.com/gmankab/magnus_backend/issues/5)
- [api roadmap](https://github.com/gmankab/magnus_backend/issues/3)
- [tt_ru.txt](docs/tt_ru.txt)
- [tt_en.txt](docs/tt_en.txt)
- [tt_ru.pdf](docs/tt_ru.pdf)

