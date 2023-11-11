import requests
from bs4 import BeautifulSoup
import re
from func import pick_url
from func import clean_text

def main():
    card_list = []
    noimage_list = []
    newimage_list = []

    with open('database.txt', 'r', encoding='utf-8') as file:
        # ファイル内の各行を順に読み込む
        for line in file:
            line = line.strip() # 行の先頭と末尾の余分な空白文字を削除
            card = line.split(" | ")
            card_list.append(card)

    # with open('noimage.txt', 'r', encoding='utf-8') as file:
    #     # ファイル内の各行を順に読み込む
    #     for line in file:
    #         line = line.strip() # 行の先頭と末尾の余分な空白文字を削除
    #         card = line.split(" | ")
    #         noimage_list.append(card)

    # cidが同じものを探す
    # returnは2次元配列
    # duplicates_in_card = find_duplicates_in_column(card_list, 0)

    # 正しい画像URLを入れてくれる
    # returnは1次元配列
    # for noimage_card in noimage_list:
    #     print(noimage_card[1])
    #     noimage_card[16] = get_image(noimage_card)
    #     newimage_list.append(noimage_card)

    # OCGページからカードの正しい種類を持ってくる
    # for card_data in card_list:
    #     if not card_data[4] == '-':
    #         card_data[7] = get_correct_cardtype(card_data[14])

    for card_data in card_list:
        card_data[7] = card_data[7].replace("'", "\"")

    # no-imageを見つける
    # returnは2次元配列
    # matching_rows = get_rows_with_element(card_list, 'https://ocg-card.com/img/card/ocg/dama-062.jpg')

    # noimageとcardlist比べて同じデータあったら差し替える
    # for data_row in card_list:
    #     for no_row in noimage_list:
    #         if data_row[0] == no_row[0]:
    #             data_row[16] = no_row[16]

    with open('buff.txt', 'w', encoding='utf-8') as file:
        # テキストをファイルに書き込む
        for card_data in card_list:
            file.write(' | '.join(card_data) + '\n')


def find_duplicates_in_column(matrix, column_index):
    seen = set()
    duplicates = []

    for row in matrix:
        element = row[column_index]
        if element in seen:
            duplicates.append(element)
        seen.add(element)

    return duplicates

def get_rows_with_element(matrix, target_element):
    matching_rows = [row for row in matrix if target_element in row]
    return matching_rows

def get_image(noimage_card):
    card_name = noimage_card[1]
    base_url = 'https://ocg-card.com/list/result/?name_0='
    query = '&name-op_0=1'
    get_url = base_url + card_name + query

    html = requests.get(get_url)
    soup = BeautifulSoup(html.content, "html.parser")
    card_html = soup.find('table')
    if card_html.find(href = re.compile("/img/card")):
        image_url = pick_url(card_html, "/img/card")
        image_url = 'https://ocg-card.com' + image_url
    else:
        ## ********トラブルサンの画像を差し込む
        print('no image')
        image_url = 'https://ocg-card.com/img/card/ocg/dama-062.jpg'

    return image_url

def get_correct_cardtype(base_url):

    card_url = base_url + '&request_locale=ja'
    html = requests.get(card_url )
    soup = BeautifulSoup(html.content, "html.parser")
    card_info = soup.find(class_ = 'species')
    origin_card_text = clean_text(str(card_info))
    card_text = origin_card_text.replace('\t','').replace('\n','')
    monster_card_type = card_text.split('／')
    monster_card_type.pop(0)

    return_text = '['
    for item in monster_card_type:
        return_text = return_text + "'" + item + "'" + ', '
    return_text = return_text + ']'
    return_text = return_text.replace(', ]',']')

    print(return_text)
    return return_text

def get_correct_text(base_url):

    card_url = base_url + '&request_locale=ja'
    html = requests.get(card_url )
    soup = BeautifulSoup(html.content, "html.parser")
    card_info = soup.find(class_ = 'item_box_text')
    origin_card_text = clean_text(str(card_info))
    card_text = origin_card_text.replace('カードテキスト','').replace('\t','').replace('\n','')

    print(card_text)
    return card_text


if __name__ == "__main__":
    main()

