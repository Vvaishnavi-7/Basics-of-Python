import asyncio
import aiohttp

async def fetch_data(session, url):
    async with session.get(url) as response:
        data=await response.text()
        return url,data
    
async def main():
    urls=[
        "https://www.geeksforgeeks.org/python/decorators-in-python/",
        "https://angular.dev/",
        "https://timesofindia.indiatimes.com/home/headlines"
    ]

    async with aiohttp.ClientSession() as session:
        tasks=[fetch_data(session, url) for url in urls]

        res=await asyncio.gather(*tasks)

        for url,content in res:
            print(f"URL: {url}")
            print(f"Content lenght:{len(content)}")
            print("-"*40)

asyncio.run(main())