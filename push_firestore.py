import firebase_admin
from firebase_admin import credentials, firestore
import json

# Firebase Admin SDKの初期化
cred = credentials.Certificate('./text/mykey.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# JSONデータの読み込み
with open('./db_text/database.json', 'r') as file:
    data = json.load(file)

# Firestoreにデータをアップロード
# 'data'コレクション内の各ドキュメントにデータをセット
for document_id, document_data in data['Cards'].items():
    doc_ref = db.collection('cards').document(document_id)
    doc_ref.set(document_data)

print('アップロード完了')
