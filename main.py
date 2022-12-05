import streamlit as st
import pandas as pd
import gspread
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
sh = workbook.worksheet('収支')
df = pd.DataFrame(sh.get_all_values()[1:], columns=sh.get_all_values()[0])

st.title('期待値稼働')

st.dataframe(df.tail(5))

st.header('打ち始め')
with st.form(key='start_form'):    
    shop_name = st.selectbox('店名',('ダイナム宇部港町店',
                                        'ダイナム小郡店',
                                        'メガガイア小郡店',
                                        'RITZ 新山口店',
                                        'ダイナム阿知須店',
                                        'テキサス山口店',
                                        'ピー・パーク',
                                        'ＶＩＰ山口店',
                                        'プレイランドエイト'))
    dai_number = st.number_input('台番号',0,10000)
    kisyu_name = st.text_input('機種名')
    game_len = st.number_input('開始ゲーム数',0,2000)
    kitaiti = st.number_input('期待値',-50000,50000)
    touroku_buton = st.form_submit_button('登録')
    if touroku_buton: 
        if list(df.index)==[]:
            index = 0
        else:
            index = int(list(df.index)[-1]+1)
        
        now = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
        day = now.date()
        start_time = now.time()
        
        df.loc[index,'年月日'] = day
        df.loc[index,'開始時間'] = start_time
        df.loc[index,'店舗名'] = shop_name
        df.loc[index,'台番号'] = dai_number
        df.loc[index,'機種名'] = kisyu_name
        df.loc[index,'開始G数'] = game_len
        df.loc[index,'期待値'] = kitaiti
        
        set_with_dataframe(sh, df, include_index = False)
        
        st.dataframe(df[df['年月日'] == day.strftime('%Y-%m-%d')])
        st.text('登録完了')
     
     
     
        
st.header('遊技中')
with st.form(key='yugi_form'):
    sen_mai_len = st.number_input('1000円枚数',0,500,100)
    push_mai_len = st.number_input('1プッシュ枚数',0,50,50)
    push_col1, push_col2 = st.columns(2)
    with push_col1:
        genkin_push_number = st.number_input('現金プッシュ回数',0,100)
    with push_col2:
        medal_push_number = st.number_input('持ちメダルプッシュ回数',0,100,1)
        
    endG_col1, endG_col2 = st.columns(2)
    with endG_col1:
        tousen_game_len = st.number_input('当選ゲーム数',0,2000)
    with endG_col2:
        yame_game_len = st.number_input('ヤメゲーム数',0,2000)
    
    yugi_touroku_buton = st.form_submit_button('登録')
    if yugi_touroku_buton: 
        
        index = int(list(df.index)[-1])
        
        toushi_medal = (push_mai_len*genkin_push_number) + (push_mai_len*medal_push_number)
        
        df.loc[index,'当選G数'] = tousen_game_len
        df.loc[index,'ヤメG数'] = yame_game_len
        df.loc[index,'投資メダル枚数'] = toushi_medal
        
        one_mai = 1000 / sen_mai_len
        if one_mai >= 20:
            df.loc[index,'投資金額'] = (push_mai_len*medal_push_number*20) + (push_mai_len*genkin_push_number*one_mai)
        elif 20>one_mai>=10:
            df.loc[index,'投資金額'] = (push_mai_len*medal_push_number*10) + (push_mai_len*genkin_push_number*one_mai)
        elif 10>one_mai>=5:
            df.loc[index,'投資金額'] = (push_mai_len*medal_push_number*5) + (push_mai_len*genkin_push_number*one_mai)
        elif 5>one_mai>=2:
            df.loc[index,'投資金額'] = (push_mai_len*medal_push_number*2) + (push_mai_len*genkin_push_number*one_mai)
        
        set_with_dataframe(sh, df, include_index = False)
        now = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
        day = now.date()
        st.dataframe(df[df['年月日'] == day.strftime('%Y-%m-%d')])
        st.text('登録完了')



st.header('結果')
with st.form(key='kekka_form'):
    hyaku_mai_len = st.number_input('交換枚数', min_value=0.0, value=5.0, step=0.1,)
    kaisyu_medal = st.number_input('回収メダル枚数',0,20000)
    
    kekka_touroku_buton = st.form_submit_button('登録')
    if kekka_touroku_buton: 
        
        index = int(list(df.index)[-1])
        
        now = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
        day = now.date()
        end_time = now.time()
        
        df.loc[index,'回収メダル枚数'] = kaisyu_medal
        df.loc[index,'回収金額'] = (100/hyaku_mai_len)*kaisyu_medal
        df.loc[index,'終了時間'] = end_time
        
        toushi_money = int(df.at[index,'投資金額'])
        toushi_medal = int(df.at[index,'投資メダル枚数'])
        kaisyuu_money = int(df.at[index,'回収金額'])
        kaisyuu_medal = int(df.at[index,'回収メダル枚数'])
        
        syushi_medal = kaisyu_medal - toushi_medal
        syushi_money = kaisyuu_money - toushi_money
        
        df.loc[index,'収支金額'] = syushi_money
        df.loc[index,'収支メダル枚数'] = syushi_medal
        
        set_with_dataframe(sh, df, include_index = False)

        st.dataframe(df[df['年月日'] == day.strftime('%Y-%m-%d')])
        st.text('登録完了')