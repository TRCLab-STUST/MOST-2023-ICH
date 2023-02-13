include .env

.PHONY: help
.DEFAULT_GOAL := help

### Mount ###
_MNT_PROJECT := $(shell pwd):/app
_MNT_DATASETS := $(DATASET_DIR):$(DOCKER_MOUNT_DATASET_DIR)
_MNT := -v ${_MNT_PROJECT} -v ${_MNT_DATASETS}

### Docker ###
_DOCKER_IMG := $(DOCKER_USER)/$(DOCKER_IMAGE):$(DOCKER_IMAGE_TAG)
_DOCKER_IMG_JUPY := ${_DOCKER_IMG}-jupyter
_DOCKER_IMG_VSCO := ${_DOCKER_IMG}-vscode
_DOCKER_ARGS := -it --rm ${_MNT}

# Port
_PORT_TENSORBOARD := $(TENSORBOARD_PORT):6007
_PORT_JUPYTER := $(JUPYTER_PORT):8888

### Tensorboard ###
_TENSORBOARD_ARGS := --logdir $(TENSORBOARD_LOGDIR) --port 6007 --host 0.0.0.0

help: ## This help message
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

runtime: ## Run default runtime
	docker run ${_DOCKER_ARGS} ${_DOCKER_IMG}

tensorboard: ## Up tensorboard serivce on port 8081
	docker run ${_DOCKER_ARGS} -p ${_PORT_TENSORBOARD} ${_DOCKER_IMG} tensorboard ${_TENSORBOARD_ARGS}

jupyter: ## Up jupyter serivce on port 8081
	docker run ${_DOCKER_ARGS} -p ${_PORT_JUPYTER} -d ${_DOCKER_IMG_JUPY}

### Build ###
build: build-gpu ## Build Image From Dockerfile

build-gpu: gpu-image gpu-jupyter-image gpu-vscode-image

gpu-image:
	docker build . -t ${_DOCKER_IMG} --target tf-gpu

gpu-jupyter-image:
	docker build . -t ${_DOCKER_IMG_JUPY} --target tf-gpu-jupyter

gpu-vscode-image:
	docker build . -t ${_DOCKER_IMG_VSCO} --target tf-gpu-vscode