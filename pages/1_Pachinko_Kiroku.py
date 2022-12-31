import streamlit as st
import pandas as pd
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import set_with_dataframe
from gspread.exceptions import APIError

while True:
    try:
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
        sh_hozon = workbook.worksheet('データ保存用')
        df_hozon = pd.DataFrame(sh_hozon.get_all_values()[1:], columns=sh_hozon.get_all_values()[0])
        break
    except APIError:
        time.sleep(1)

with st.form(key='border_henkan'):
    henkan_col1, henkan_col2 = st.columns(2)
    with henkan_col1:
        to1 = st.checkbox('4円から1円')
    with henkan_col2:
        to4 = st.checkbox('1円から4円')
        
    kaitenritsu = st.number_input('回転率',0.0,40.0,10.0,0.1)
    
    henkan_buton = st.form_submit_button('変換')
    
    if henkan_buton:
        if to1 and to4:
            st.text('チェックボックスを正しく選択してください')
        elif to4:
            st.text(kaitenritsu*5/4)
        elif to1:
            st.text(kaitenritsu*4/5)
        else:
            st.text('チェックボックスを正しく選択してください')
            
before_befor_kaiten_len = int(df_hozon.loc[3,'数値'])
before_now_kaiten_len = int(df_hozon.loc[4,'数値'])
before_push_len = int(df_hozon.loc[5,'数値'])
    
befor_kaiten_len = st.number_input('打ち始めの回転数',0,10000,before_befor_kaiten_len,1)
now_kaiten_len = st.number_input('現在の回転数',0,10000,before_now_kaiten_len,1)
push_len = st.number_input('プッシュ数',0,10000,before_push_len,1)



kaitenritsu_button = st.button('計算')
if kaitenritsu_button:
    my_kaiten_len = now_kaiten_len - befor_kaiten_len
    my_kaitenritsu = my_kaiten_len / push_len
    st.text('回転数:' + str(my_kaiten_len))
    st.text('回転率:' + str(my_kaitenritsu))   
    
    df_hozon.loc[3,'数値'] = befor_kaiten_len
    df_hozon.loc[4,'数値'] = now_kaiten_len
    df_hozon.loc[5,'数値'] = push_len
    set_with_dataframe(sh_hozon, df_hozon, include_index = False) 

st.subheader('※注意書き')
st.text('1 打ち始めの回転数を入れる')
st.text('2 ワンプッシュ分打ち終わったら現在の回転数とプッシュを１回追加')

reset_button = st.button('リセット')
if reset_button:
    df_hozon.loc[3,'数値'] = 0
    df_hozon.loc[4,'数値'] = 0
    df_hozon.loc[5,'数値'] = 0
    set_with_dataframe(sh_hozon, df_hozon, include_index = False)
