url = 'https://nekdo.ru/'
xpath = '//div[@class="text"]'

import requests
from parsel import Selector


class NewsScraper:
    url = "https://www.anekdot.ru/random/anekdot/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    anecdot_xpath = '//div[@class="text"]'

    def parse_data(self):
        text = requests.get(url=self.url, headers=self.headers).text

        tree = Selector(text=text)
        texts = tree.xpath(self.anecdot_xpath).getall()

        for text in texts:
            text = text.replace('<div class="text">', '')
            text = text.replace('<br>', '\n')
            text = text.replace('</div>', '')
            print(text + '\n')

        return texts

if __name__ == "__main__":
    scraper = NewsScraper()
    scraper.parse_data()