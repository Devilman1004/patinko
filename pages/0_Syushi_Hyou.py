import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st

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
sh = workbook.worksheet('収支')
df = pd.DataFrame(sh.get_all_values()[1:], columns = sh.get_all_values()[0])

st.title('収支表')

st.dataframe(df)

st.header('生涯収支')

st.text('期待値合計')
st.text(sum([int(i) for i in list(df['期待値'])]))

st.text('収支金額')
st.text(sum([int(i) for i in list(df['収支金額'])]))

days_list=[]
day_list = list(set(df['年月日']))
for day in day_list:
    day_df = df[df['年月日']==day]
    sum([int(i) for i in list(day_df['期待値'])])
    sum([int(i) for i in list(day_df['収支金額'])])
    days_list.append([day,sum([int(i) for i in list(day_df['期待値'])]),sum([int(i) for i in list(day_df['収支金額'])])])
day_df = pd.DataFrame(days_list,columns=['年月日','期待値','収支金額']).sort_values('年月日').reset_index(drop=True)
suii_list = []
kitaiti_sum = 0
syushi_sum = 0
for i in range(len(list(day_df['期待値']))):
    if i == 0:
        kitaiti_sum = list(day_df['期待値'])[i]
        syushi_sum = list(day_df['収支金額'])[i]
    else:
        kitaiti_sum = list(day_df['期待値'])[i] + kitaiti_sum
        syushi_sum = list(day_df['収支金額'])[i] + syushi_sum
    
    suii_list.append([list(day_df['年月日'])[i],kitaiti_sum,syushi_sum])
suii_df = pd.DataFrame(suii_list,columns=['年月日','期待値','収支金額']).set_index('年月日')

st.text('収支推移')
st.line_chart(suii_df)