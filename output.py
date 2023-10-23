from bs4 import BeautifulSoup
import re
from func import determine_season
from func import clean_text
from func import pick_url

def output_monster(card_status, monster_status, base_text, base_release):
    total_card_data = []

    name_name_ruby_html = card_status.find(class_ = re.compile("-mon"))
    name_ruby_html =name_name_ruby_html.find('div', class_ = 'card-ruby')
    name = name_name_ruby_html.text
    name_ruby = ''
    if name_ruby_html:
        name_ruby = name_ruby_html.text
        name = name.replace(name_ruby, '')
    else:
        name_ruby = name

    attribute = monster_status.find(class_ = 'card-attr').text
    monster_type = monster_status.find(class_ = 'card-type').text
    incantation_type = '-'
    level = monster_status.find(class_ = 'card-star').text

    base_card_type = card_status.find(class_ = 'card-category').text
    card_type_list = base_card_type.split("／")
    card_type = '['
    for item in card_type_list:
        card_type = card_type + "'" + item + "'" + ', '
    card_type = card_type + ']'
    card_type = card_type.replace(', ]',']')

    text = clean_text(str(base_text))
    monster_force = monster_status.find_all(class_ = 'card-force')
    atk = monster_force[0].text
    def_ = monster_force[1].text
    release = base_release
    season, zero_four = determine_season(release)

    a_tags = card_status.find(class_ = 'card-info')
    ocg_url = pick_url(a_tags, "yugioh-card.com")
    cid = ocg_url.split('cid=')[1]
    wiki_url = pick_url(a_tags, "yugioh-wiki.net")
    image_url = pick_url(card_status, "/img/card")
    image_url = 'https://ocg-card.com' + image_url

    total_card_data.append(cid)
    total_card_data.append(name)
    total_card_data.append(name_ruby)
    total_card_data.append(attribute)
    total_card_data.append(monster_type)
    total_card_data.append(incantation_type)
    total_card_data.append(level)
    total_card_data.append(card_type)
    total_card_data.append(text)
    total_card_data.append(atk)
    total_card_data.append(def_)
    total_card_data.append(release)
    total_card_data.append(season)
    total_card_data.append(zero_four)
    total_card_data.append(ocg_url)
    total_card_data.append(wiki_url)
    total_card_data.append(image_url)

    print(len(total_card_data))
    print(total_card_data[7])
    print(total_card_data)


def output_spell(card_status, base_text, base_release):

    text = clean_text(str(base_text))

    print(card_status)
    print(text)