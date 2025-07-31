# Task Management App

A simple but production-ready task management app built with **Next.js** and **FastAPI**. This was built as a coding exercise, so I kept it focused on the core requirements while maintaining good practices.

## 🚀 Quick Start

```bash
# Clone and setup
git clone <your-repo-url>
cd dragonfly-task-app

# Copy environment file and adjust if needed
cp .env.example .env

# Start everything up
make up

# That's it! The app should be running at:
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

## 🏗️ What's Inside

### **Frontend (Next.js 14)**
- Next.js with the new App Router
- TypeScript for type safety
- Tailwind CSS for styling (kept it simple)
- React hooks for state management
- Axios for API calls

### **Backend (FastAPI)**
- FastAPI for the REST API
- Python 3.11+ with proper type hints
- PostgreSQL with SQLAlchemy ORM
- Pydantic for data validation
- Pytest for testing (with separate test DB)

### **Infrastructure**
- Docker & Docker Compose for easy setup
- GitHub Actions for CI/CD
- Code quality tools: ESLint, Black, isort, Flake8, Mypy

## 📁 Project Structure

```
dragonfly-task-app/
├── .env.example          # Environment template
├── .env                  # Your local config (not in git)
├── docker-compose.yml    # Services orchestration
├── Makefile             # Handy commands
├── README.md            # This file
├── .github/workflows/   # CI/CD setup
├── backend/
│   ├── app/             # FastAPI app
│   ├── tests/           # Backend tests
│   ├── Dockerfile       # Backend container
│   └── requirements.txt # Python deps
└── frontend/
    ├── src/app/         # Next.js app
    ├── public/          # Static files
    ├── Dockerfile.dev   # Frontend container
    └── package.json     # Node deps
```

## 🛠️ Development Commands

### **Basic Operations**
```bash
# Start everything
make up

# Stop everything
make down

# Rebuild if needed
make build

# Check logs
make logs
```

### **Backend Stuff**
```bash
# Run tests
make test

# Check code quality
make code-quality

# Individual checks
make lint
make format-check
make imports-check
make type-check
```

### **Frontend Stuff**
```bash
# Run frontend tests
make test-frontend

# Lint frontend
make lint-frontend
```

## 🧪 Testing

### **Backend Tests**
- Uses Pytest with a separate test database
- Tests the API endpoints properly
- Run with: `make test`

### **CI/CD Pipeline**
I've set up GitHub Actions for automated testing and code quality checks. The pipeline includes:
- Backend tests with PostgreSQL service
- Frontend linting
- Code formatting checks
- Type checking

**Note**: The CI pipeline is configured but tests only run locally since there's no deployed database instance for this exercise. You can run everything locally without issues.

## 🔧 Configuration

### **Environment Variables**
Copy `.env.example` to `.env` and adjust:

```bash
# Database settings
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=tasks
POSTGRES_HOST=db
POSTGRES_PORT=5432

# API settings
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=true

# Frontend settings
FRONTEND_PORT=3000
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 🚀 Deployment

### **Local Development**
```bash
make up
```

### **Production Ready**
- Environment-specific configs ready
- AWS Secrets Manager integration prepared
- Docker Compose for orchestration
- GitHub Actions for CI/CD

## 📊 API Endpoints

- `GET /tasks` - Get all tasks
- `POST /tasks` - Create a new task
- `PATCH /tasks/{id}` - Update a task
- `DELETE /tasks/{id}` - Delete a task

Interactive docs at: http://localhost:8000/docs

## 🛡️ Code Quality

### **Backend**
- **Linting**: Flake8
- **Formatting**: Black
- **Imports**: isort
- **Types**: Mypy

### **Frontend**
- **Linting**: ESLint
- **Formatting**: Prettier
- **Types**: TypeScript

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch
3. Make your changes
4. Run tests: `make test && make test-frontend`
5. Run quality checks: `make code-quality`
6. Submit a PR

## 📄 License

MIT License - see [LICENSE](LICENSE) file.

## 🆘 Troubleshooting

### **Common Issues**

**Database connection problems:**
```bash
make down
make up
```

**Frontend can't connect to backend:**
- Check `NEXT_PUBLIC_API_URL` in `.env`
- Make sure backend is running: `docker compose ps`

**Tests failing:**
```bash
make clean-test-db
make test
```

## 🎯 Areas Where I Took Shortcuts

Given the time constraints of this exercise, I made some intentional simplifications:

### **UI/UX**
- **Simple UI**: Used basic Tailwind styling instead of a complex design system
- **No animations**: Kept it functional without fancy transitions
- **Basic error handling**: Simple error messages, no advanced UX patterns

### **Authentication & Security**
- **No user system**: Skipped authentication to focus on core functionality
- **No authorization**: No role-based access control
- **Basic validation**: Used Pydantic's built-in validation, no custom business rules

### **Testing**
- **Backend-focused**: Comprehensive backend tests, minimal frontend tests
- **No E2E tests**: Skipped end-to-end testing for time
- **No performance tests**: No load testing or performance benchmarks

### **Infrastructure**
- **Local-only**: No cloud deployment setup
- **Simple database**: Single PostgreSQL instance, no replication
- **No monitoring**: No logging, metrics, or observability tools

### **Features**
- **No search/filter**: Basic CRUD operations only
- **No pagination**: Simple list view
- **No bulk operations**: Individual task operations only
- **No data export**: No CSV/JSON export functionality

These shortcuts were taken to deliver a working, production-quality application within the time constraints while demonstrating good coding practices and architecture decisions.

## 🔗 Quick Links

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **CI/CD**: [GitHub Actions](.github/workflows/ci.yml) 
