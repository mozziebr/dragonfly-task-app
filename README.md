# Task Management App

A full-stack task management application built with FastAPI (backend) and Next.js (frontend).

## Features
- Create, read, update, and delete tasks
- Mark tasks as completed
- Modern, responsive UI
- RESTful API
- Dockerized for easy development and deployment

## Tech Stack
- **Backend**: FastAPI, SQLAlchemy, PostgreSQL
- **Frontend**: Next.js, React, TypeScript, Tailwind CSS
- **Database**: PostgreSQL
- **Containerization**: Docker & Docker Compose

## Quick Start

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd dragonfly-task-app
   ```

2. Set up environment variables:
   ```bash
   # Backend
   cp backend/.env.example backend/.env
   # Edit backend/.env for your local setup
   
   # Frontend
   cp frontend/.env.example frontend/.env.local
   # Edit frontend/.env.local for your local setup
   ```

3. Start all services:
   ```bash
   make up
   ```

4. Open your browser and navigate to:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## Development

### Start all services
```bash
make up
```

### Stop all services
```bash
make down
```

### Rebuild containers
```bash
make build
```

### Backend testing
```bash
cd backend
make test
```

## Environment Configuration

### Backend (.env)
Copy `backend/.env.example` to `backend/.env` and adjust:
- `POSTGRES_HOST`: Database host (default: `db` for Docker, `localhost` for local)
- `POSTGRES_PORT`: Database port (default: `5432`)
- `DEBUG`: Enable debug mode (default: `true`)

### Frontend (.env.local)
Copy `frontend/.env.example` to `frontend/.env.local` and adjust:
- `NEXT_PUBLIC_API_URL`: Backend API URL (default: `http://localhost:8000`)

## Project Structure
```
├── backend/          # FastAPI backend
│   ├── app/         # Application code
│   ├── tests/       # Backend tests
│   └── Makefile     # Backend commands
├── frontend/        # Next.js frontend
│   ├── src/         # Source code
│   └── public/      # Static assets
├── docker-compose.yml
└── Makefile         # Main project commands
```

## API Endpoints
- `GET /tasks/` - Get all tasks
- `POST /tasks/` - Create a new task
- `PATCH /tasks/{id}` - Update a task
- `DELETE /tasks/{id}` - Delete a task

## License
MIT # DragonFlyInsurance
# dragonfly-task-app
# dragonfly-task-app
