.PHONY: default build docker-run docker-push
default: docker-build


SHELL	=	bash
STAGE	?=	dev

PORT	?=	8080
TAG 	?=	latest
image 	=	ghcr.io/flapflapio/library-service:$(TAG)

docker-build:
	docker build -t "$(image)" -f docker/Dockerfile .

docker-run:
	docker run \
		-it \
		-p $(PORT):$(PORT) \
		--rm \
		--name library-service \
		$(image)

docker-push:
	docker push "$(image)"

test:
	poetry run pytest -v
