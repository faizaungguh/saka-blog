dev-backend:
	docker build -t dev-backend .

dev-backend-run:
	docker container run -d -p 3000:3000 --name api-blog dev-backend

dev-backend-kill:
	docker container kill api-blog && docker container rm api-blog && docker image rm dev-backend

dev-backend-rm:
	docker image rm dev-backend