.PHONY: build, dev, test, clean
IMAGE_NAME=wildnlp

clean:
	rm -rf build
	rm -rf dist
	rm -rf wild_nlp.egg-info
	rm -rf .pytest_cache

build:
	docker build -t $(IMAGE_NAME) .

dev:
	docker run --rm -ti \
		-v $(PWD)/:/project \
		-w="/project" \
		$(IMAGE_NAME)

test:
	python3 -m pytest tests/ -s