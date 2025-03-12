import pytest
from sqlalchemy import create_engine
from fast_api.models import table_registry
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from fast_api.app import app


@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture()
def session():
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)

    #gerenciamento de contexto
    with Session(engine) as session :
        yield session

    table_registry.metadata.drop_all(engine)

    