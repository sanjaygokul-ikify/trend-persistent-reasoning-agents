dev:
	pip install -e .
	sudo docker-compose up
	sudo docker volume create memory-store
	sudo docker volume create execution-trace

docs:
	python -m docs.serve

clean:
	rm -rf __pycache__ *.egg-info
	docker-compose down

test:
	pytest tests

lint:
	pylint --rcfile=.pylintrc

bench:
	python benchmarks/reasoning_agents.py

deploy:
	make build
	sudo docker stack deploy -c docker-stack.yml pr_agents
