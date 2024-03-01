DC = docker-compose
DEV_COMPOSE = -f dev.docker-compose.yml
PROD_COMPOSE = -f prod.docker-compose.yml
REDIS = -f redis.docker-compose.yml

.PHONY: start-dev start-prod start-dev-rebuild start-prod-rebuild down delete

start-dev: ## Start the API container in development mode with local (in-memory) database.
	$(DC) $(DEV_COMPOSE) up

start-redis: ## Start the Redis container in development mode (in background)
	$(DC) $(REDIS) up -d

start-prod: ## Start the API container in production mode (with postgres)
	$(DC) $(PROD_COMPOSE) up

start-dev-rebuild: ## Start the development version with container rebuild
	$(DC) $(DEV_COMPOSE) build --no-cache
	$(DC) $(DEV_COMPOSE) up

start-prod-rebuild: ## Start the production version with container rebuild
	$(DC) $(PROD_COMPOSE) build --no-cache
	$(DC) $(PROD_COMPOSE) up

down: ## Stop all running containers
	docker stop $$(docker ps -a -q) || true

delete: ## Delete all containers, images, volumes and networks
	docker system prune -a --volumes
	docker volume prune -a
