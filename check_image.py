import requests
from bs4 import BeautifulSoup
import re
import json

def main():
    card_list = []
    # JSONデータの読み込み
    with open('./db_text/database.json', 'r') as file:
        data = json.load(file)

    # リストからデータを抜き出して編集
    for item in data["cards"]:

        print(str(item["card_name"]["name"]))
        image_url = item["image_url"]

        if is_image_url_valid(image_url):
            print("画像が存在します。")
        else:
            print("画像が存在しません。")
            card_list.append(item["card_name"]["name"])

    print("********************")
    for name in card_list:
        print(name)

    return
    # JSONデータをファイルに書き込み
    with open("./db_text/buff.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)

def is_image_url_valid(image_url):
    try:
        response = requests.head(image_url)
        return response.status_code == 200
    except requests.RequestException:
        return False

if __name__ == "__main__":
    main()
