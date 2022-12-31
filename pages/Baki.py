import streamlit as st
import pandas as pd

st.title('バキ 強くなりたくば喰らえ!!!')

st.text('https://note.com/zema/n/na9cfc8dcd170')

st.header('期待値')

with st.expander("CZ間天井期待値"):
    st.header('CZ間天井期待値')

with st.expander("ATまで天井期待値"):
    st.header('ATまで天井期待値')

with st.expander("天国モード狙い 期待値"):
    st.header('天国モード狙い 期待値')

with st.expander("200Gゾーン 狙い期待値"):
    st.header('200Gゾーン 狙い期待値')

with st.expander("朝イチCZ間期待値"):
    st.header('朝イチCZ間期待値')

with st.expander("朝イチ天国モード狙い期待値"):
    st.header('朝イチ天国モード狙い期待値')

with st.expander("前回当選G数ごとの狙い目"):
    st.header('前回当選G数ごとの狙い目')


st.header('やめどき')
st.subheader('【重要】')
st.text('・CZ・ATの終了画面でpushボタンを押してボイスを確認できます。')
df = pd.DataFrame([['刃牙…','デフォルト','1G後ヤメ'],['やる価値十分ってわけだ','天国期待度アップ','1G後ヤメ'],['男同士イチャイチャと','通常B以上','1G後ヤメ80G後再開'],['お父さんを喜ばせなさい','通常C以上','AT当選まで'],['頭の位置をより高きに置くもの。それが勝者だ','天国A or B','CZ当選まで']],
                  columns=['ボイス','示唆内容','ヤメどき']).set_index('ボイス')
st.table(df)
st.text('・エンドルフィンポイント　バキ緑以上ならAT当選まで')
st.text('・力みカウンター 星３以上なら消灯まで')
st.text('・範馬メーター　4ポイント以上ならメーターMAXまで')
