import requests
from bs4 import BeautifulSoup

base_url = "https://ocg-card.com/list/101/"

html = requests.get(base_url)
soup = BeautifulSoup(html.content, "html.parser")

cards = soup.find('table').find_all('tr')

for card in cards:

    # 最初にいらないものが２個出てくる
    # モンスターは３個の塊、魔法罠は２個の塊になって出てくる

    print('****************')
    print(card)
    print()


