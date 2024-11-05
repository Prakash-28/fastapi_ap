
# FastAPI PostgreSQL Example

This is a sample FastAPI app connected to PostgreSQL using Async SQLAlchemy.

## Requirements
- Python 3.7+
- PostgreSQL
- Install dependencies with:
  ```bash
  pip install fastapi sqlalchemy asyncpg
  ```

## Running the App
1. Update `DATABASE_URL` in `main.py` with your PostgreSQL credentials.
2. Run the app with:
   ```bash
   uvicorn main:app --reload
   ```
