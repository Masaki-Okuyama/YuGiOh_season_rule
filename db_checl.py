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

    duplicates_in_card = find_duplicates_in_column(card_list, 0)
    print(duplicates_in_card)
    with open('database.txt', 'w', encoding='utf-8') as file:
        # テキストをファイルに書き込む
        for card_data in card_list:
            file.write(' | '.join(card_data) + '\n')

if __name__ == "__main__":
    main()

