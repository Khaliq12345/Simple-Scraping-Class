from requests_html import HTMLSession
from latest_user_agents import get_random_user_agent


class Aldoshoe:
    def __init__(self):
        self.session = HTMLSession()
        self.headers = {'User-Agent': get_random_user_agent()}

    def extract(self, url):
        r = self.session.get(url, headers=self.headers)
        title = r.html.find('h1', first=True).text
        price = r.html.find('.c-product-price__formatted-price', first=True).text
        scraped_item = (
            title,
            price
        )

        return scraped_item