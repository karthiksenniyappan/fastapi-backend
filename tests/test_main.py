import warnings

import httpx
import pytest
from pydantic import PydanticDeprecatedSince20

from server import app

@pytest.mark.filterwarnings(
    "ignore::pydantic.PydanticDeprecatedSince20",
    "ignore::DeprecationWarning:crypt"
)
@pytest.mark.asyncio
async def test_root_route():
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': 'API is working'}
