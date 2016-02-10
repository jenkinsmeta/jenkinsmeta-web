build:
	docker build -t jenkinsmeta-web .

run:
	docker run -it -p 8080:8080 jenkinsmeta-web
