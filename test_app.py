import pytest
import aiohttp
from app import get_json

@pytest.mark.asyncio
async def test_get_json_successful(event_loop):
    url = "https://jsonplaceholder.typicode.com/todos/1"
    result = await get_json(url)
    assert "userId" in result

@pytest.mark.asyncio
async def test_get_json_invalid_url(event_loop):
    url = "https://example.com/invalid"
    with pytest.raises(aiohttp.ClientError):
        await get_json(url)

@pytest.mark.asyncio
@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@pytest.allure.description("Тест для проверки get_json с корректным URL.")
def test_get_json_allure_successful(event_loop):
    url = "https://jsonplaceholder.typicode.com/todos/1"
    result = await get_json(url)
    assert "userId" in result
