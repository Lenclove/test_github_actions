import pytest

from app.main import app
# import pytest
from httpx import AsyncClient
from fastapi.testclient import TestClient


@pytest.mark.asyncio
async def test_get_index():
    async with AsyncClient(app=app, base_url='http://test') as ac:
        response = await ac.get('/')
    assert response.status_code == 200
    assert response.text == 'Hello World!'
