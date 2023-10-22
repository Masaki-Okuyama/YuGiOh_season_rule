import requests
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

    name = ''
    name_ruby = ''
    if card_status.find('td', class_ = 'n-mon'):
        name = card_status.find('td', class_ = 'n-mon').text
        if card_status.find('td', class_ = 'n-mon').find('div', class_ = 'card-ruby'):
            name_ruby = card_status.find('td', class_ = 'n-mon').find('div', class_ = 'card-ruby').text
            name = name.replace(name_ruby, '')
        else:
            name_ruby = name
    elif card_status.find('td', class_ = 'f-mon'):
        name = card_status.find('td', class_ = 'f-mon').text
        if card_status.find('td', class_ = 'f-mon').find('div', class_ = 'card-ruby'):
            name_ruby = card_status.find('td', class_ = 'f-mon').find('div', class_ = 'card-ruby').text
            name = name.replace(name_ruby, '')
        else:
            name_ruby = name
    elif card_status.find('td', class_ = 'r-mon'):
        name = card_status.find('td', class_ = 'r-mon').text
        if card_status.find('td', class_ = 'r-mon').find('div', class_ = 'card-ruby'):
            name_ruby = card_status.find('td', class_ = 'r-mon').find('div', class_ = 'card-ruby').text
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

    # attack(int)
    # defense(int)
    release = base_release
    season, _04 = determine_season(release)
    # ocg_url(str)
    # cid(int)
    # wiki_url(str)
    # image_url(str)

    print(card_status)
    print(monster_status)
    print(name + '(' + name_ruby)
    print(attribute + ', ' + monster_type + ', ' + incantation_type + ', ' + card_type + ', ' + level)
    print(release + ', ' + season + ', ' + _04)
    print(text)

def output_spell(card_status, base_text, base_release):
    print(card_status)
    # cleaned_text = re.sub(re.compile('<a.*/a>'), '', base_text.text)
    text = str(base_text)
    text = re.sub(r'<tr[^>]*>', '', text)
    text = re.sub(r'<td[^>]*>', '', text)
    text = re.sub(r'<a[^>]*>', '', text)
    text = re.sub(r'</[^>]*>', '', text)
    print(text)