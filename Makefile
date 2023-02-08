include .env

.PHONY: help
.DEFAULT_GOAL := help

help: ## This help message
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

runtime: ## Run default runtime
	docker run -it --rm -v $(shell pwd):/app $(DOCKER_USER)/$(IMAGE_NAME):$(IMAGE_VERSION_TAG)

tensorboard: ## Up tensorboard serivce on port 8081
	docker run -it --rm -v $(shell pwd):/app -p $(TENSORBOARD_PORT):6007 $(DOCKER_USER)/$(IMAGE_NAME):$(IMAGE_VERSION_TAG) tensorboard --logdir $(TENSORBOARD_LOGDIR) --port 6007 --host 0.0.0.0

jupyter: ## Up jupyter serivce on port 8081
	docker run -it --rm -v $(shell pwd):/app -p $(JUPYTER_PORT):8888 -d $(DOCKER_USER)/$(IMAGE_NAME):$(IMAGE_VERSION_TAG)-jupyter

build: build-gpu ## Build Image From Dockerfile

build-gpu: gpu-image gpu-jupyter-image gpu-vscode-image

gpu-image:
	docker build . -t $(DOCKER_USER)/$(IMAGE_NAME):$(IMAGE_VERSION_TAG) --target tf-gpu

gpu-jupyter-image:
	docker build . -t $(DOCKER_USER)/$(IMAGE_NAME):$(IMAGE_VERSION_TAG)-jupyter --target tf-gpu-jupyter

gpu-vscode-image:
	docker build . -t $(DOCKER_USER)/$(IMAGE_NAME):$(IMAGE_VERSION_TAG)-vscode --target tf-gpu-vscode