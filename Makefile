.PHONY: build, dev, test, clean, example, send_to_pypi, update_leaderboard
IMAGE_NAME=wildnlp

clean:
	rm -rf build \
		dist \
		wild_nlp.egg-info \
		.pytest_cache \
		tests/aspects/__pycache__ \
		tests/datests/__pycache__

build:
	docker build -t $(IMAGE_NAME) .

dev:
	docker run --rm -ti \
		-v $(PWD)/:/project \
		-w="/project" \
		$(IMAGE_NAME)

test:
	python3 -m pytest tests/ -s

example:
	pip3 install -e .
	python3 example/evaluation.py

send_to_pypi:
	python3 -m pip install --upgrade setuptools wheel, twine
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload dist/*

# Works only in the container
update_leaderboard:
	(cd /codalab-cli/ && \
		venv/bin/python scripts/competitiond.py \
		/project/Leaderboard/_cl_config.yaml \
		/project/Leaderboard/out.json)