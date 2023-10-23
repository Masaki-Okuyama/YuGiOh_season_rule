import requests
from bs4 import BeautifulSoup
import re
from output import get_monster
from output import get_spell

def main():
    # base_url = 'https://ocg-card.com/list/101/'
    # release = '1999-02-04'
    base_url = 'https://ocg-card.com/list/302/'
    release = '2004-07-18'

    html = requests.get(base_url)
    soup = BeautifulSoup(html.content, "html.parser")
    cards = soup.find('table').contents

    card_data_list = []
    card_index = 0
    while card_index < len(cards):
        if cards[card_index].find(class_ = 'magic'):
            # 魔法カードの情報ならここに
            card_status = cards[card_index]
            card_text = cards[card_index + 1]
            card_data_list.append(get_spell(card_status, 'magic', card_text, release))
            card_index = card_index + 1
        elif cards[card_index].find(class_ = 'trap'):
            # 罠カードの情報ならここに
            card_status = cards[card_index]
            card_text = cards[card_index + 1]
            card_data_list.append(get_spell(card_status, 'trap', card_text, release))
            card_index = card_index + 1
        elif cards[card_index].find(class_ = re.compile("-mon")):
            # モンスターカードの情報ならここに
            card_status = cards[card_index]
            monster_status = cards[card_index + 1]
            card_text = cards[card_index + 2]
            card_data_list.append(get_monster(card_status, monster_status, card_text, release))
            card_index = card_index + 2

        card_index = card_index + 1

    for card_data in card_data_list:
        print('****************')
        print(card_data)
        print()


if __name__ == "__main__":
    main()