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

df = df.astype({'投資金額': int ,
                '回収金額': int ,
                '投資メダル枚数': int ,
                '期待値': int ,
                '回収メダル枚数': int , 
                '回収金額': float ,
                '収支金額': int ,
                '収支メダル枚数': int})
df['年月日'] = pd.to_datetime(df['年月日'])

st.title('収支表')

st.header('生涯収支')
ichiran = st.checkbox('一覧を表示')
if ichiran:
    st.dataframe(df)
syougai_col1, syougai_col2, syougai_col3 = st.columns(3)
with syougai_col1:
    st.subheader('期待値合計')
    st.text(str(sum([int(i) for i in list(df['期待値'])])) + '円')
with syougai_col2:
    st.subheader('収支金額')
    st.text(str(sum([int(i) for i in list(df['収支金額'])])) + '円')
with syougai_col3:
    st.subheader('台数')
    st.text(str(len(df.index)) + '台')

days_list=[]
day_list = list(set(df['年月日']))
day_list.sort()
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

st.subheader('収支推移')
st.line_chart(suii_df)


kari_day_list = []
for day in day_list:
    day_df = df[df['年月日']==day]
    day_kitaichi = sum([int(i) for i in list(day_df['期待値'])])
    day_syushi_money = sum([int(i) for i in list(day_df['収支金額'])])
    kari_day_list.append([day,day_kitaichi,day_syushi_money])
day_bestu_df = pd.DataFrame(kari_day_list,columns=['年月日','期待値','収支金額'])




with st.expander("月別収支"):
    st.header('月別収支')

    shitei_month = st.selectbox('月',tuple(set(day_bestu_df['年月日'].dt.strftime('%Y-%m'))))
    shitei_month_df = day_bestu_df[day_bestu_df['年月日'].dt.strftime('%Y-%m') == shitei_month]

    tukibetsu_col1, tukibetsu_col2, tukibetsu_col3 = st.columns(3)
    with tukibetsu_col1:
        st.subheader('期待値合計')
        st.text(str(sum(shitei_month_df['期待値'])) + '円')
    with tukibetsu_col2:
        st.subheader('収支金額')
        st.text(str(sum(shitei_month_df['収支金額'])) + '円')
    with tukibetsu_col3:
        st.subheader('台数')
        st.text(str(len(df[df['年月日'].dt.strftime('%Y-%m') == shitei_month].index)) + '台')
        
    st.dataframe(shitei_month_df)
    
    suii_list = []
    kitaiti_sum = 0
    syushi_sum = 0
    for i in range(len(list(shitei_month_df['期待値']))):
        if i == 0:
            kitaiti_sum = list(shitei_month_df['期待値'])[i]
            syushi_sum = list(shitei_month_df['収支金額'])[i]
        else:
            kitaiti_sum = list(shitei_month_df['期待値'])[i] + kitaiti_sum
            syushi_sum = list(shitei_month_df['収支金額'])[i] + syushi_sum
        
        suii_list.append([list(shitei_month_df['年月日'])[i],kitaiti_sum,syushi_sum])
    suii_df = pd.DataFrame(suii_list,columns=['年月日','期待値','収支金額']).set_index('年月日')

    st.subheader('収支推移')
    st.line_chart(suii_df)



with st.expander("日別収支"):
    st.header('日別収支')

    shitei_day = st.selectbox('日付',day_list)
    shitei_day_df = df[df['年月日']==shitei_day]

    nishibetsu_col1, nishibetsu_col2, nishibetsu_col3 = st.columns(3)
    with nishibetsu_col1:
        st.subheader('期待値合計')
        st.text(str(sum(shitei_day_df['期待値'])) + '円')
    with nishibetsu_col2:
        st.subheader('収支金額')
        st.text(str(sum(shitei_day_df['収支金額'])) + '円')
    with nishibetsu_col3:
        st.subheader('台数')
        st.text(str(len(shitei_day_df.index)) + '台')
        
    st.dataframe(shitei_day_df)