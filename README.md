# Library Service [![Build](https://github.com/flapflapio/library-service/actions/workflows/test.yml/badge.svg)](https://github.com/flapflapio/library-service/actions/workflows/test.yml)

## QuickStart

1. Install [`poetry`](https://github.com/python-poetry/poetry)
2. Install dependencies inside your poetry virtualenv: `poetry install`
3. Run the app: `./app.py`
   - You can also run by invoking uvicorn directly: `poetry run uvicorn library_service.main:app --reload`

**\*Run tests with pytest: `poetry run pytest`**

**\*For creating a production build, check out [Deploying to Production](#running-in-production)**

Check out the below section [Using Poetry](#using-poetry) on using poetry to
manage the virtual environment associated with your project. If you are using
vscode, remember that you need to point vscode to the virtual environment
associated installed by poetry (see below).

## Using Poetry

This project uses [poetry](https://github.com/python-poetry/poetry) for
dependency management. To operate a poetry environment:

```bash
# Install all dependencies
poetry install

# Open vscode
poetry run code .

# Then go to bottom left > configure python interpreter > select the one in your virtualenv
```

## Running in Production

To run the app in production:

```bash
gunicorn library_service.main:app \
    --workers 1 \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:8080
```

To run the Docker image:

```bash
# Build the docker image (ghcr.io/flapflapio/library-service:latest)
make

# Run the docker image
make docker-run
```
