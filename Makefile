# Task Management App - Unified Makefile
# Industry standard commands for the full-stack application

.PHONY: help up down build logs test test-frontend lint lint-frontend code-quality clean clean-test-db

# Default target
help: ## Show this help message
	@echo "Task Management App - Available Commands:"
	@echo ""
	@echo "Project Management:"
	@echo "  up              Start all services (frontend, backend, databases)"
	@echo "  down            Stop all services"
	@echo "  build           Rebuild all containers"
	@echo "  logs            View service logs"
	@echo ""
	@echo "Testing:"
	@echo "  test            Run backend tests"
	@echo "  test-frontend   Run frontend tests"
	@echo ""
	@echo "Code Quality:"
	@echo "  lint            Lint backend code (flake8)"
	@echo "  lint-frontend   Lint frontend code (eslint)"
	@echo "  code-quality    Run all backend quality checks"
	@echo ""
	@echo "Maintenance:"
	@echo "  clean           Clean all containers and volumes"
	@echo "  clean-test-db   Clean test database"
	@echo ""

# Project Management
up: ## Start all services
	docker compose up -d

down: ## Stop all services
	docker compose down

build: ## Rebuild all containers
	docker compose build --no-cache

logs: ## View service logs
	docker compose logs -f

# Testing
test: ## Run backend tests
	docker compose up -d db_test
	docker compose run --rm backend env PYTHONPATH=/app TESTING=true TEST_DB_URL=postgresql://postgres:postgres@db_test:5432/tasks_test pytest -v tests/
	docker compose down -v --remove-orphans

test-frontend: ## Run frontend tests
	docker compose run --rm frontend npm test

# Code Quality
lint: ## Lint backend code
	docker compose run --rm backend env PYTHONPATH=/app flake8 app/ tests/

lint-frontend: ## Lint frontend code
	docker compose run --rm frontend npm run lint

format-check: ## Check backend code formatting
	docker compose run --rm backend env PYTHONPATH=/app black --check app/ tests/

imports-check: ## Check backend import sorting
	docker compose run --rm backend env PYTHONPATH=/app isort --check-only app/ tests/

type-check: ## Run backend type checking
	docker compose run --rm backend mypy app/

code-quality: lint format-check imports-check type-check ## Run all backend quality checks

# Maintenance
clean: ## Clean all containers and volumes
	docker compose down -v --remove-orphans
	docker system prune -f

clean-test-db: ## Clean test database
	docker compose down -v --remove-orphans && docker compose up -d db_test

# Development shortcuts
dev: up ## Alias for up
stop: down ## Alias for down
rebuild: build ## Alias for build
