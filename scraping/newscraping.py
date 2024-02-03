# import httpx
# import asyncio
# from parsel import Selector
#
#
# class AsyncNewsScraper:
#     url = "https://ru.freepik.com/search?format=search&last_filter=page&last_value={page}&page={page}&shape=lineal-color&type=icon#uuid=987ed86b-9c8a-4f61-8d81-8c31539ba4c9"
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
#         'Accept': '*/*',
#         'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
#         'Accept-Encoding': 'gzip, deflate, br',
#     }
#     anecdot_xpath = '//div[@class="text"]'
#     image_url_xpath = '//div[@class="_1ys1uvi9 _1286nb19f"]/img/@src'
#     async def async_generator(self, limit):
#         for page in range(1, limit + 1):
#             yield page
#
#     async def get_pages(self):
#         async with httpx.AsyncClient(headers=self.headers) as client:
#             async for page in self.async_generator(limit=3):
#                 data = await self.get_url(
#                     client=client,
#                     url=self.url.format(
#                         page=page
#                     )
#                 )
#
#     async def get_url(self, client, url):
#         response = await client.get(url=url)
#         print('response-url: ', response.url)
#
#         await self.scrape_url(response=response)
#
#     async def scrape_url(self, response):
#         tree = Selector(text=response.text)
#         links = tree.xpath(self.anecdot_xpath).extract()
#         for image_link in links:
#             print(image_link)
#
#
# if __name__ == "__main__":
#     scraper = AsyncNewsScraper()
#     asyncio.run(scraper.get_pages())

import httpx
import asyncio
from parsel import Selector

class AsyncNewsScraper:
    url = "https://www.anekdot.ru/random/anekdot/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    anecdot_xpath = '//div[@class="text"]'

    async def get_data(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(url=self.url, headers=self.headers)
            print('response-url: ', response.url)
            return await self.parse_data(response.text)


    async def parse_data(self, text):
        tree = Selector(text=text)
        texts = tree.xpath(self.anecdot_xpath).getall()

        for text in texts:
            text = text.replace('<div class="text">', '')
            text = text.replace('<br>', '\n')
            text = text.replace('</div>', '')
            print(text + '\n')

        return texts

    async def start_anecdot(self):
        await self.get_data()

if __name__ == "__main__":
    scraper = AsyncNewsScraper()
    asyncio.run(scraper.start_anecdot())
