import streamlit as st

st.title('革命機ヴァルヴレイヴ')

st.text('https://note.com/zema/n/ncf5ff14fe77b')

data_type = st.selectbox('データ表示機タイプ',('ART表示あり','ART表示なし'))

if data_type == 'ART表示なし' :
    st.text(data_type)
    
    RB_through = st.selectbox('RBスルー回数',('1','2','3','4'))
    
    st.text('スルー回数：' + RB_through)
    
elif data_type == 'ART表示あり' :
    st.text(data_type)
    
    CZ_through = st.selectbox('CZスルー回数',('1','2','3','4','5'))
    RB_through = st.selectbox('RBスルー回数',('1','2','3','4'))
    
    st.text('スルー回数：' + RB_through)

hikimodoshi_type = st.selectbox('引き戻しタイプ',('CZ後','RB後','BB単発後','革命ラッシュBB2連~4連以下後','超革命ラッシュBB4連以上後'))