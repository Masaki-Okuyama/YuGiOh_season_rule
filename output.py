from bs4 import BeautifulSoup
import re
from func import determine_season
from func import clean_text
from func import pick_url
from func import get_release
import sys

def get_monster(card_status, monster_status, base_text):
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
    monster_force = []
    atk = ''
    def_ = ''
    if monster_status.find(class_ = 'non-stts'):
        if monster_status.find(class_ = 'card-force'):
            status_contents =  monster_status.contents
            atk = status_contents[3].text.replace('-','-1')
            def_ = status_contents[4].text.replace('-','-1')
        else:
            atk = '-1'
            def_ = '-1'
    else:
        monster_force = monster_status.find_all(class_ = 'card-force')
        atk = monster_force[0].text
        def_ = monster_force[1].text

    a_tags = card_status.find(class_ = 'card-info')
    ocg_url = pick_url(a_tags, "yugioh-card.com")
    cid = ocg_url.split('cid=')[1]
    wiki_url = pick_url(a_tags, "yugioh-wiki.net")
    if card_status.find(href = re.compile("/img/card")):
        image_url = pick_url(card_status, "/img/card")
        image_url = 'https://ocg-card.com' + image_url
    else:
        ## ********トラブルサンの画像を差し込む
        image_url = 'https://ocg-card.com/img/card/ocg/dama-062.jpg'
    release_url = pick_url(a_tags, "/latest/")
    release_url = 'https://ocg-card.com' + release_url
    release = str(get_release(release_url))
    season, zero_four = determine_season(release)

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

    return total_card_data


def get_spell(card_status, spell_type, base_text):
    total_card_data = []

    name = ''
    name_ruby = ''
    if spell_type == 'magic':
        name_name_ruby_html = card_status.find(class_ = 'magic')
        name = name_name_ruby_html.text
        name_ruby_html = name_name_ruby_html.find('div', class_ = 'card-ruby')
        if name_ruby_html:
            name_ruby = name_ruby_html.text
            name = name.replace(name_ruby, '')
        else:
            name_ruby = name
        attribute = '魔'
        incantation_type = card_status.find(class_ = 'card-category').text
        incantation_type = incantation_type.strip('魔法')
    elif spell_type == 'trap':
        name_name_ruby_html = card_status.find(class_ = 'trap')
        name = name_name_ruby_html.text
        name_ruby_html = name_name_ruby_html.find('div', class_ = 'card-ruby')
        if name_ruby_html:
            name_ruby = name_ruby_html.text
            name = name.replace(name_ruby, '')
        else:
            name_ruby = name
        attribute = '罠'
        incantation_type = card_status.find(class_ = 'card-category').text
        incantation_type = incantation_type.strip('罠')

    monster_type = '-'
    level = '-1'
    card_type = "['-']"
    text = clean_text(str(base_text))
    atk = '-1'
    def_ = '-1'

    a_tags = card_status.find(class_ = 'card-info')
    ocg_url = pick_url(a_tags, "yugioh-card.com")
    cid = ocg_url.split('cid=')[1]
    wiki_url = pick_url(a_tags, "yugioh-wiki.net")
    if card_status.find(href = re.compile("/img/card")):
        image_url = pick_url(card_status, "/img/card")
        image_url = 'https://ocg-card.com' + image_url
    else:
        image_url = 'image-not-found'
    release_url = pick_url(a_tags, "/latest/")
    release_url = 'https://ocg-card.com' + release_url
    release = str(get_release(release_url))
    season, zero_four = determine_season(release)

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

    return total_card_data

