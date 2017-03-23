#!/usr/bin/env python3.6

import requests

from bs4 import BeautifulSoup

url = "http://w2.vatican.va/content/john-paul-ii/en/apost_exhortations/documents/hf_jp-ii_exh_30121988_christifideles-laici.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")
text_selector = "#corpo > div.documento > div > div.text.parbase.container.vaticanrichtext"

