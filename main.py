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
sh_secchi = workbook.worksheet('設置一覧')
sh_shop = workbook.worksheet('店一覧')
sh_slot_kisyu = workbook.worksheet('スロット機種一覧')
df_secchi = pd.DataFrame(sh_secchi.get_all_values()[1:], columns=sh_secchi.get_all_values()[0])
df_shop = pd.DataFrame(sh_shop.get_all_values()[1:], columns=sh_shop.get_all_values()[0])
df_slot_kisyu = pd.DataFrame(sh_slot_kisyu.get_all_values()[1:], columns=sh_slot_kisyu.get_all_values()[0])


st.title('パチンコ・パチスロ期待値稼働')

shop_name = st.selectbox(
    '店名',
    tuple(df_shop['店名'])
    )

shop_num = list(df_shop['店番号'])[(list(df_shop['店名']).index(shop_name))]

shop_df = df_secchi[df_secchi['店番号'] == shop_num]

dai_number = st.selectbox(
    '台番号',
    tuple(shop_df['台番号'])
    )

kisyu_num = shop_df['機種番号'][list(shop_df['台番号']).index(dai_number)]

kisyu_name = df_slot_kisyu['機種名'][list(df_slot_kisyu['機種番号']).index(kisyu_num)]

st.text_input('機種名',kisyu_name)

kisyu_df = df_slot_kisyu[df_slot_kisyu['機種名'] == kisyu_name]

st.dataframe(kisyu_df)

#st.text('メーカー:' + kisyu_df.iloc[])

game_len = st.number_input('ゲーム数',0,2000)