import requests
from bs4 import BeautifulSoup
import re
from output import output_monster
from output import output_spell

def main():
    # base_url = 'https://ocg-card.com/list/101/'
    # release = '1999-02-04'
    base_url = 'https://ocg-card.com/list/302/'
    release = '2004-07-18'

    html = requests.get(base_url)
    soup = BeautifulSoup(html.content, "html.parser")
    cards = soup.find('table').contents

    card_index = 0
    while card_index < len(cards):
        if cards[card_index].find(class_ = 'magic'):
            # 魔法カードの情報ならここに
            # card_status = cards[card_index]
            # card_text = cards[card_index + 1]
            # print('****************')
            # output_spell(card_status, card_text, release)
            # print()
            card_index = card_index + 1
        elif cards[card_index].find(class_ = 'trap'):
            # 罠カードの情報ならここに
            # card_status = cards[card_index]
            # card_text = cards[card_index + 1]
            # print('****************')
            # output_spell(card_status, card_text, release)
            # print()
            card_index = card_index + 1
        elif cards[card_index].find(class_ = re.compile("-mon")):
            # モンスターカードの情報ならここに
            card_status = cards[card_index]
            monster_status = cards[card_index + 1]
            card_text = cards[card_index + 2]
            print('****************')
            output_monster(card_status, monster_status, card_text, release)
            print()
            card_index = card_index + 2

        card_index = card_index + 1


    # if monster_card_count > 0:
    #     for monster_index in range(0, len(monster_cards), 2):
    #         print('****************')
    #         output_monster(monster_cards[monster_index], monster_cards[monster_index + 1], card_texts[int(monster_index/2)])
    #         print()

    # if spell_card_count > 0:
    #     for spell_index in range(0, spell_card_count, 1):
    #         print('****************')
    #         output_spell(spell_cards[spell_index], card_texts[spell_index + monster_card_count])
    #         print()



if __name__ == "__main__":
    main()