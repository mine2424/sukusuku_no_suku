from html.parser import HTMLParser
import requests
from bs4 import BeautifulSoup


class ScrapingService:

    def init_BeautifulSoup(self, url: str):
        res = requests.get(url)
        res.encoding = res.apparent_encoding
        return BeautifulSoup(res.text, 'html.parser')

    def find_all(self, bs: BeautifulSoup, tag_name: str, attrs_key: str, attrs_value: str):
        res_list = list(bs.find_all(tag_name, attrs={attrs_key: attrs_value}))
        # return res_list
        new_list = []
        for res in res_list:
            overview_value = {
                'text': res.get_text().replace('　', ','),
                'html': res
            }
            new_list.append(overview_value)
        return new_list
