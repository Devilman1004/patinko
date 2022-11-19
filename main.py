import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import gspread
import json
import pandas as pd
#ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials
import datetime
from gspread_dataframe import set_with_dataframe

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
sh_kari = workbook.worksheet('シート7')
df_secchi = pd.DataFrame(sh_secchi.get_all_values()[1:], columns=sh_secchi.get_all_values()[0])
df_shop = pd.DataFrame(sh_shop.get_all_values()[1:], columns=sh_shop.get_all_values()[0])
df_slot_kisyu = pd.DataFrame(sh_slot_kisyu.get_all_values()[1:], columns=sh_slot_kisyu.get_all_values()[0])
df_kari = pd.DataFrame(sh_kari.get_all_values()[1:], columns=sh_kari.get_all_values()[0])

st.title('期待値稼働')

st.header('◎　目標')
st.subheader('・年収120万円')
st.subheader('・月収10万円')
st.subheader('・週収2万5000円')
st.subheader('・日収3334円')
# st.header('◎　マイルール')
# st.subheader('・次の日が仕事だったら２１までには帰宅')

st.header('打ち始め')
with st.form(key='nyuryoku_form'):    
    shop_name = st.selectbox(
        '店名',
        tuple(df_shop['店名'])
        )
    dai_number = st.number_input('台番号',0,10000)
    kisyu_name = st.selectbox(
        '機種名',
        tuple(df_slot_kisyu['機種名'])
        )
    game_len = st.number_input('ゲーム数',0,20000)
    kitaiti = st.number_input('期待値',0,50000)
    replay = st.number_input('貯メダル数',0,10000)
    
# shop_num = list(df_shop['店番号'])[(list(df_shop['店名']).index(shop_name))]

# shop_df = df_secchi[df_secchi['店番号'] == shop_num]

# dai_number = st.selectbox(
#     '台番号',
#     tuple(shop_df['台番号'])
#     )
    
# kisyu_num = shop_df['機種番号'][list(shop_df['台番号']).index(dai_number)]

# kisyu_name = df_slot_kisyu['機種名'][list(df_slot_kisyu['機種番号']).index(kisyu_num)]

# st.text_input('機種名',kisyu_name)

# kisyu_df = df_slot_kisyu[df_slot_kisyu['機種名'] == kisyu_name].set_index('機種番号')

# kisyu_df = df_kari[df_kari['機種番号'] == kisyu_num]

# tenzyo_df = kisyu_df[kisyu_df['カテゴリ'] == '天井狙い']

# game_list = list(tenzyo_df['項目'])
# kitaiti_list = list(tenzyo_df['内容'])

# kitaiti=int(kitaiti_list[game_list.index(str(game_len))])

# st.text(str(kitaiti) + '円')

    touroku_buton = st.form_submit_button('登録')
    
    if touroku_buton:

        # １．ファイル名を指定してワークブックを選択
        sh_syushi = workbook.worksheet('収支')
        df_syushi = pd.DataFrame(sh_secchi.get_all_values()[1:], columns=sh_secchi.get_all_values()[0])
        
        if list(df_syushi.index)==[]:
            index = 0
        else:
            index = list(df_syushi.index)[-1]+1
        
        now = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
        day = now.date()
        start_time = now.time()
        
        df_syushi.loc[index,'年月日'] = day
        df_syushi.loc[index,'開始時間'] = start_time
        df_syushi.loc[index,'店舗名'] = shop_name
        df_syushi.loc[index,'台番号'] = dai_number
        df_syushi.loc[index,'期待値	'] = kitaiti
        
        set_with_dataframe(sh_syushi, df_syushi,include_index = False)
        
        st.dataframe(df_syushi.tail(5))
        st.text('登録完了')

# with st.sidebar:
#     kihon_df = kisyu_df[kisyu_df['カテゴリ'] == '基本情報'][['項目','内容']].set_index('項目')

#     st.table(kihon_df)

    # st.text('メーカー：' + kisyu_df.loc[kisyu_num,'メーカー'])
    # st.text('タイプ：' + kisyu_df.loc[kisyu_num,'タイプ'])
    # st.text('５０枚あたり：' + kisyu_df.loc[kisyu_num,'コイン持ち'])
    # st.text('天井ゲーム数：' + kisyu_df.loc[kisyu_num,'天井'])
    # st.text('純増：' + kisyu_df.loc[kisyu_num,'純増'])

    # st.image('./images/sammy-rump.jpg')
    #st.text('メーカー:' + kisyu_df.iloc[])

