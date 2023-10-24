from collections import Counter

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

def main():
    card_list = []
    with open('database.txt', 'r', encoding='utf-8') as file:
        # ファイル内の各行を順に読み込む
        for line in file:
            # 行の先頭と末尾の余分な空白文字を削除
            line = line.strip()
            # 1行ずつの処理

            # 区切り文字 "|" を使用して文字列を分割し、リストに格納
            card = line.split(" | ")

            # 結果を表示
            card_list.append(card)

    # duplicates_in_card = find_duplicates_in_column(card_list, 0)

    # with open('noimage.txt', 'w', encoding='utf-8') as file:
    #     # テキストをファイルに書き込む
    #     for card_data in card_list:
    #         file.write(' | '.join(card_data) + '\n')

    matching_rows = get_rows_with_element(card_list, 'https://ocg-card.com/img/card/ocg/dama-062.jpg')
    with open('noimage.txt', 'w', encoding='utf-8') as file:
        # テキストをファイルに書き込む
        for card_data in matching_rows:
            file.write(' | '.join(card_data) + '\n')


if __name__ == "__main__":
    main()

