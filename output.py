from bs4 import BeautifulSoup
import re
from datetime import datetime

def determine_season(release):
    date = datetime.strptime(release, "%Y-%m-%d")

    if date <= datetime(2000, 3, 31):
        season = "1"
    elif date <= datetime(2002, 5, 15):
        season = "2"
    elif date <= datetime(2004, 5, 26):
        season = "3"
    elif date <= datetime(2006, 5, 17):
        season = "4"
    elif date <= datetime(2008, 3, 14):
        season = "5"
    else:
        return "6"

    if date <= datetime(2004, 11, 25):
        _04 = 'true'
    else:
        _04 = 'false'

    return season, _04

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

    text = str(base_text)
    text = re.sub(r'<tr[^>]*>', '', text)
    text = re.sub(r'<td[^>]*>', '', text)
    text = re.sub(r'<a[^>]*>', '', text)
    text = re.sub(r'</[^>]*>', '', text)

    monster_force = monster_status.find_all(class_ = 'card-force')
    attack = monster_force[0].text
    defense = monster_force[1].text
    release = base_release
    season, _04 = determine_season(release)

    url_buffer = card_status.find_all(href=re.compile("yugioh-card.com"))
    ocg_url = url_buffer[0].attrs['href']
    cid = ocg_url.split('cid=')[1]
    url_buffer = card_status.find_all(href=re.compile("yugioh-wiki.net"))
    wiki_url = url_buffer[0].attrs['href']
    url_buffer = card_status.find_all(href=re.compile("/img/card"))
    image_url = url_buffer[0].attrs['href']
    image_url = 'https://ocg-card.com' + image_url



    print(name + '(' + name_ruby)
    print(attribute + ', ' + monster_type + ', ' + incantation_type + ', ' + card_type + ', ' + level + ', ' + attack + ', ' + defense)
    print(release + ', ' + season + ', ' + _04 + ', ' + cid)
    print(ocg_url)
    print(wiki_url)
    print(image_url)
    print(text)

def output_spell(card_status, base_text, base_release):


    text = str(base_text)
    text = re.sub(r'<tr[^>]*>', '', text)
    text = re.sub(r'<td[^>]*>', '', text)
    text = re.sub(r'<a[^>]*>', '', text)
    text = re.sub(r'</[^>]*>', '', text)

    print(card_status)
    print(text)