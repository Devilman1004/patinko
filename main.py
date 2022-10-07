import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import gspread
import json
import pandas as pd
#ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials

#2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
json_path = 'kitaichi-fd2dd716665b.json'
#認証情報設定
#ダウンロードしたjsonファイル名をクレデンシャル変数に設定（秘密鍵、Pythonファイルから読み込みしやすい位置に置く）
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_path, scope)
#OAuth2の資格情報を使用してGoogle APIにログインします。
gc = gspread.authorize(credentials)
# １．ファイル名を指定してワークブックを選択
workbook = gc.open('収支表')
worksheet = workbook.worksheet('機種_1')
df = pd.DataFrame(worksheet.get_all_values()[1:], columns=worksheet.get_all_values()[0]).set_index('開始')
df['期待値'] = df['期待値'].astype('int')

st.title('パチンコ・パチスロ期待値稼働')


left,right=st.columns(2)

left.text_input('機種名')
game_len = right.number_input('ゲーム数',0,2000)

left,center,right=st.columns(3)