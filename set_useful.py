

def main():
    card_list = []
    useful_list = [4354, 4842, 4861, 4909, 4758, 4818, 5114, 5323, 5031, 5400, 5432, 5655, 5719, 5799, 5835, 5914, 6000, 5217, 6390, 6558, 6770, 7403, 7349, 7421, 7516, 7574]

    with open('./db_text/database.txt', 'r', encoding='utf-8') as file:
        # ファイル内の各行を順に読み込む
        for line in file:
            line = line.strip() # 行の先頭と末尾の余分な空白文字を削除
            card = line.split(" | ")
            card_list.append(card)

    for card in card_list:
        if int(card[0]) in useful_list:
            card[17] = 'true'
        else:
            card[17] = 'false'

    with open('./db_text/buff.txt', 'w', encoding='utf-8') as file:
        # テキストをファイルに書き込む
        for card_data in card_list:
            file.write(' | '.join(card_data) + '\n')


if __name__ == "__main__":
    main()
