import aiohttp
import asyncio

async def get_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data


async def main():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    result = await get_json(url)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
