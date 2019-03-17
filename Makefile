.PHONY: build, dev, test
IMAGE_NAME=wildnlp

build:
	docker build -t $(IMAGE_NAME) .

dev:
	docker run --rm -ti \
		-v $(PWD)/:/project \
		-w="/project" \
		$(IMAGE_NAME)

test:
	python3 -m pytest tests/ -s