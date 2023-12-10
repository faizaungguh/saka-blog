dev-frontend:
	docker build -t dev-frontend .

dev-frontend-run:
	docker container run -d -p 3000:8080 --name ui-blog dev-frontend

dev-frontend-kill:
	docker container kill ui-blog && docker container rm ui-blog && docker image rm dev-frontend

dev-frontend-rm:
	docker image rm dev-frontend