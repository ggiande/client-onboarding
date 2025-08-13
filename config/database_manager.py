import os
from typing import Any, Generator

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import OperationalError # Import for error handling
from dotenv import load_dotenv, find_dotenv

class DatabaseManager:
    _engine = None
    _SessionLocal = None

    @classmethod
    def get_engine(cls):
        if load_dotenv(find_dotenv()):
            print("Environment variables loaded successfully.")
        else:
            print(f".env file not found or could not be loaded")

        # print(f"os.environ {os.environ}")
        # print(f"os.environ {os.environ.get('DB_USER')} ")
        # print(f"os.environ {os.environ.get('SESSION_MANAGER')} ")
        if cls._engine is None:
            db_user = os.environ.get("DB_USER") or "postgres"
            db_password = os.environ.get("DB_PASSWORD") or "password"
            db_host = os.environ.get("DB_HOST") or "localhost"
            db_port = os.environ.get("DB_PORT") or "5432"
            db_name = os.environ.get("DB_NAME") or "your_database_name"

            connection_string = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
            # print(f"connection_string: {connection_string}")
            try:
                cls._engine = create_engine(connection_string, pool_pre_ping=True)
                # Test connection
                with cls._engine.connect() as conn:
                    result = conn.execute(text("SELECT 1"))
                    print("Database connection successful!")
            except OperationalError as e:
                print(f"Error connecting to the database: {e}")
                raise ConnectionRefusedError(f"Could not connect to database: {e}") from e
            except Exception as e:
                print(f"An unexpected error occurred during database connection setup: {e}")
                raise

        return cls._engine

    @classmethod
    def get_session_local(cls):
        if cls._SessionLocal is None:
            cls._SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=cls.get_engine())
        return cls._SessionLocal

    @classmethod
    def get_db(cls) -> Generator[Session, Any, None]:
        """
        Dependency for FastAPI to get a database session.
        Yields a session and ensures it's closed after use.
        """
        db = cls.get_session_local()() # Creates a new session
        try:
            yield db
        finally:
            db.close()
