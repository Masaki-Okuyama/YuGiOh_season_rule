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
    elif date <= datetime(2008, 3, 14):
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
    text = re.sub(r'</[^>]*>', '', text)
    return text


def pick_url(html, base_url):
    #htmlの中からbase_urlが含まれるURLを探す
    url_buffer = html.find(href = re.compile(base_url))
    url = url_buffer.attrs['href']
    return url

