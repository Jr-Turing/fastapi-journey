# fastapi-journey

A structured learning journey to master FastAPI from fundamentals to production-ready backend development.

## Overview

This repository contains notes, examples, and practical implementations for learning FastAPI and modern Python backend development.

## Goals

- Learn the fundamentals of FastAPI and Python backend development
- Build APIs with validation, database integration, and authentication
- Practice clean project structure and scalable backend design
- Develop real-world projects from beginner to production-ready examples

## Topics Covered

- FastAPI basics and routing
- Pydantic models and validation
- CRUD operations
- Database integration
- Dependency injection
- Authentication and authorization
- Testing and debugging
- Deployment and environment configuration

## Repository Structure

```text
fastapi-journey/
├── README.md
├── api-notes.md
├── pyproject.toml
└── fastapi-ecommerce/
	└── app/
		├── main.py
		├── data/
		├── schema/
		└── service/
```

## Getting Started

1. Clone the repository.
2. Install the dependencies with `uv`.
3. Start the FastAPI development server.

```bash
git clone https://github.com/jr-Turing/fastapi-journey.git
cd fastapi-journey
uv sync
uv run uvicorn app.main:app --reload --app-dir fastapi-ecommerce
```

## Learning Path

- FastAPI fundamentals
- API design and routing
- Data validation and schemas
- Database integration
- Authentication and security
- Testing and deployment

## Notes

See [api-notes.md](api-notes.md) for introductory API and architecture notes.
