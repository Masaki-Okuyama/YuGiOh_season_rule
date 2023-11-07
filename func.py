import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

def determine_season(release):
    # 引数の収録日から期と04を判断する関数
    date = datetime.strptime(release, '%Y-%m-%d')
    if date <= datetime(2000, 3, 31):
        season = "1"
    elif date <= datetime(2002, 5, 15):
        season = "2"
    elif date <= datetime(2004, 5, 26):
        season = "3"
    elif date <= datetime(2006, 5, 17):
        season = "4"
    elif date <= datetime(2008, 3, 11):
        season = "5"
    else:
        season =  "6"

    if date <= datetime(2004, 11, 25):
        zero_four = 'true'
    else:
        zero_four = 'false'

    return season, zero_four

def clean_text(base_text):
    # カードテキストから余計なタグを削除する関数
    text = str(base_text)
    text = re.sub(r'<tr[^>]*>', '', text)
    text = re.sub(r'<td[^>]*>', '', text)
    text = re.sub(r'<a[^>]*>', '', text)
    text = re.sub(r'<div[^>]*>', '', text)
    text = re.sub(r'<span[^>]*>', '', text)
    text = re.sub(r'<p[^>]*>', '', text)
    text = re.sub(r'</[^>]*>', '', text)
    return text

def pick_url(html, base_url):
    #htmlの中からbase_urlが含まれるURLを探す
    url_buffer = html.find(href = re.compile(base_url))
    url = url_buffer.attrs['href']
    return url

def get_release(card_html_url):
    html = requests.get(card_html_url)
    soup = BeautifulSoup(html.content, "html.parser")
    release = soup.find(class_ ="entry-date date published updated").text
    if release:
        release = release.replace(' ','')
        release = release.replace('/','-')
    else:
        release = '1000-01-01'
    parts = release.split('-')
    # 日付部分を0埋めして2桁にする
    year = parts[0]
    month = parts[1].zfill(2)
    day = parts[2].zfill(2)
    if day == '00':
        day = '01'
    # 0埋めされた日付部分を結合
    release = f"{year}-{month}-{day}"
    return release

