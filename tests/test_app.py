from fastapi.testclient import TestClient
from fast_api.app import app

client = TestClient(app)

def test_read_root_deve_retornar_ok_e_hello_world():
    ...