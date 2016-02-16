build:
	docker build -t jenkinsmeta-web .

run:
	docker run -it -p 8080:8080 jenkinsmeta-web

debug:
	python app.py

test:
	discover

clean:
	find . -name '*.pyc' -exec rm {} +
