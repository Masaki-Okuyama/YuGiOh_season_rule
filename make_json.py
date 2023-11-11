def main():
    card_list = []
    json_list = []

    json_list.append("{\"Records\":[")

    with open('database.txt', 'r', encoding='utf-8') as file:
        # ファイル内の各行を順に読み込む
        for line in file:
            line = line.strip() # 行の先頭と末尾の余分な空白文字を削除
            card = line.split(" | ")
            card_list.append(card)


    for card_data in card_list:
        print(card_data[1])
        result_dict = {
            "cid": int(card_data[0].strip()),
            "card_name": {"name": card_data[1].strip(), "name_ruby": card_data[2].strip()},
            "card_properties": {"attribute": card_data[3].strip(), "monster_type": card_data[4].strip(), "incantation_type": card_data[5].strip(), "level": int(card_data[6].strip()), "card_type": eval(card_data[7].strip())},
            "text": card_data[8].strip(),
            "status": {"atk": int(card_data[9].strip()), "def": int(card_data[10].strip())},
            "card_release": {"release": card_data[11].strip(), "season": int(card_data[12].strip()), "zero_four": card_data[13].strip()},
            "card_url": {"ocg_url": card_data[14].strip(), "wiki_url": card_data[15].strip()},
            "image_url": card_data[16].strip()
        }

        # 結果を出力
        json_data = str(result_dict).replace("'","\"") + ","
        json_list.append(json_data)

    json_list.append("]}")

    with open('buff.txt', 'w', encoding='utf-8') as file:
        # テキストをファイルに書き込む
        for card_data in json_list:
            file.write(card_data + '\n')


if __name__ == "__main__":
    main()

