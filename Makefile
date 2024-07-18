ROOT_DIR := ${shell git rev-parse --show-toplevel}
BUILD_DIR = $(ROOT_DIR)/build

.PHONY: clean build

clean:
	@rm -rf $(BUILD_DIR)

venv/bin/python:
	@python3 -m venv venv
	@. venv/bin/activate && pip install --upgrade build twine

build: venv/bin/python
	@mkdir -p $(BUILD_DIR)
	@. venv/bin/activate &&python3 -m build -o $(BUILD_DIR)

publish: build
	. venv/bin/activate &&twine upload --repository-url ${REPO} -u ${USER} -p ${PASSWORD} build/*

help:
	@echo "The following targets are available:"
	@echo "clean	Cleans the build forder"
	@echo "build	Compile the python code to a package"
	@echo "publish	publish package to REPO with USER and PASSWORD as variables
