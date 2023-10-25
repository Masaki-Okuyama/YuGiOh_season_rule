import requests
from bs4 import BeautifulSoup
import re
from func import pick_url

def main():
    card_list = []
    noimage_list = []
    newimage_list = []
    # with open('database.txt', 'r', encoding='utf-8') as file:
    #     # ファイル内の各行を順に読み込む
    #     for line in file:
    #         line = line.strip() # 行の先頭と末尾の余分な空白文字を削除
    #         card = line.split(" | ")
    #         card_list.append(card)

    with open('newimage.txt', 'r', encoding='utf-8') as file:
        # ファイル内の各行を順に読み込む
        for line in file:
            line = line.strip() # 行の先頭と末尾の余分な空白文字を削除
            card = line.split(" | ")
            card_list.append(card)

    # cidが同じものを探す
    # returnは2次元配列
    # duplicates_in_card = find_duplicates_in_column(card_list, 0)

    # 正しい画像URLを入れてくれる
    # returnは1次元配列
    # for noimage_card in noimage_list:
    #     print(noimage_card[1])
    #     noimage_card[16] = get_image(noimage_card)
    #     newimage_list.append(noimage_card)

    #no-imageを見つける
    # returnは2次元配列
    matching_rows = get_rows_with_element(card_list, 'https://ocg-card.com/img/card/ocg/dama-062.jpg')

    # with open('database.txt', 'w', encoding='utf-8') as file:
    #     # テキストをファイルに書き込む
    #     for card_data in card_list:
    #         file.write(' | '.join(card_data) + '\n')

    with open('noimage.txt', 'w', encoding='utf-8') as file:
        # テキストをファイルに書き込む
        for card_data in matching_rows:
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


if __name__ == "__main__":
    main()

