import json

# JSONデータの読み込み
with open('./db_text/database.json', 'r') as file:
    data = json.load(file)

# リストからデータを抜き出して編集
for item in data["cards"]:
    if item["card_properties"]["attribute"] == "魔":
        item["status"]["atk"] = -2
        item["status"]["def"] = -2
        print(str(item["card_name"]["name"]) + " -2")
    elif item["card_properties"]["attribute"] == "罠":
        item["status"]["atk"] = -3
        item["status"]["def"] = -3
        print(str(item["card_name"]["name"]) + " -3")

# JSONデータをファイルに書き込み
with open("./db_text/buff.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=2)

