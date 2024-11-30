# o1-mini-AI-engine
This project contains the "o1-mini" AI engine with full-stack features, including modular components for API handling, machine learning pipelines, procedural generation, asynchronous task handling, caching, and monitoring.

## Features
- **API**: FastAPI for RESTful API endpoints with Swagger and ReDoc documentation.
- **Machine Learning Pipeline**: Scikit-learn and XGBoost for ML tasks.
- **Procedural Generation**: Modular NPC generation using mixins.
- **Async Tasks**: Celery tasks with Redis as the broker.
- **Caching**: Redis for data caching.
- **Database**: SQLAlchemy ORM and Alembic for migrations.
- **Stream Processing**: Apache Flink integration for real-time data.

## Setup
1. Clone this repository:
    ```bash
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```bash
    cd o1-mini-AI-engine
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Start the API server:
    ```bash
    uvicorn api.main:app --reload
    ```
5. Start the Celery worker:
    ```bash
    celery -A celery_tasks.tasks worker --loglevel=info
    ```

## Running with Docker
Build and run the application using Docker Compose:
```bash
docker-compose up --build
```

## API Documentation
FastAPI provides auto-generated API documentation accessible at:
- **Swagger UI**: `/docs`
- **ReDoc**: `/redoc`

## Testing
Run tests with pytest:
```bash
pytest tests/
```

## Environment Configuration
Set environment variables in a `.env` file (see `.env.example`).

---

## Components
- **API**: `/api/main.py` with routes for item CRUD operations.
- **Machine Learning Pipeline**: `/ml_pipeline/pipeline.py`.
- **Celery Tasks**: `/celery_tasks/tasks.py`.
- **Flink Streaming**: `/flink_streaming/streaming.py`.

Refer to each module's inline documentation for usage details.
