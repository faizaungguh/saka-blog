# Development Environment Image
# Build Dev
build-dev: 
	cd backend && $(MAKE) dev-backend
	cd frontend && $(MAKE) dev-frontend

be-dev:
	cd backend && $(MAKE)  dev-backend

fe-dev:
	cd frontend && $(MAKE) dev-frontend

# Run Docker-compose
run-dev:
	docker-compose -f docker-compose-dev.yml up

# Stop Docker
stop:
	docker-compose down