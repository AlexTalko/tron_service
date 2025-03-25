import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base, get_db
from main import app


@pytest.fixture(scope="session")
def engine():
    """Фикстура для создания тестового движка БД"""
    test_db_url = "sqlite:///./test.db"
    engine = create_engine(
        test_db_url,
        connect_args={"check_same_thread": False}
    )
    yield engine
    engine.dispose()


@pytest.fixture(scope="session")
def create_tables(engine):
    """Создание всех таблиц перед тестами"""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def db_session(engine, create_tables):
    """Фикстура для тестовых сессий БД"""
    connection = engine.connect()
    transaction = connection.begin()
    session = sessionmaker(bind=connection)()

    yield session

    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture
def override_get_db(db_session):
    """Подмена зависимости get_db для тестов"""

    def _override_get_db():
        try:
            yield db_session
        finally:
            pass  # Сессия закрывается в db_session

    return _override_get_db


@pytest.fixture
def client(override_get_db):
    """Тестовый клиент FastAPI"""
    # Подменяем оригинальную зависимость
    app.dependency_overrides[get_db] = override_get_db

    from fastapi.testclient import TestClient
    with TestClient(app) as test_client:
        yield test_client

    # Восстанавливаем оригинальную зависимость
    app.dependency_overrides.clear()
