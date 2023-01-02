import streamlit as st
import pandas as pd

with st.expander("B系以上示唆一覧"):
    st.header('B系以上示唆一覧')
    st.text('【重要】ハイビスカスの光り方をチェック')
    df = pd.DataFrame([['高速点滅,スロー点滅','通常B以上期待度UP'],['点灯→点滅,スロー→高速点滅','通常B以上期待度大幅UP'],['同時点滅,通常点滅→同時点滅,花と葉の交互点滅','通常B以上確定'],['三三七拍子','天国以上期待度UP'],['右のみ点滅,点滅+パネル消灯,カラフル点滅','天国以上確定'],['左のみ点滅,リバースストリーム点滅','ドキドキ以上確定'],['通常点滅+ドキドキランプ点灯,しだれ柳','超ドキドキ確定']],
                    columns=['光り方','モード示唆']).set_index('光り方')
    st.table(df)

with st.form("rireki",True):
    now = st.number_input('現在のG数',min_value=0,max_value=1000)
    col1, col2 = st.columns(2)
    with col1:
        through1 = st.number_input('1スルー目',min_value=0,max_value=1000)
    with col2:
        syubetsu1 = st.selectbox('ボーナス種別',('RB','BB'))
    through2 = st.number_input('2スルー目',min_value=0,max_value=1000)
    through3 = st.number_input('3スルー目',min_value=0,max_value=1000)
    through4 = st.number_input('4スルー目',min_value=0,max_value=1000)
    through5 = st.number_input('5スルー目',min_value=0,max_value=1000)
    through6 = st.number_input('6スルー目',min_value=0,max_value=1000)
    through7 = st.number_input('7スルー目',min_value=0,max_value=1000)
    through8 = st.number_input('8スルー目',min_value=0,max_value=1000)
    through9 = st.number_input('9スルー目',min_value=0,max_value=1000)
    through10 = st.number_input('10スルー目',min_value=0,max_value=1000)
    through11 = st.number_input('11スルー目',min_value=0,max_value=1000)
    through12 = st.number_input('12スルー目',min_value=0,max_value=1000)
    through13 = st.number_input('13スルー目',min_value=0,max_value=1000)
    through14 = st.number_input('14スルー目',min_value=0,max_value=1000)
    through15 = st.number_input('15スルー目',min_value=0,max_value=1000) 
    kitaichi_submitted = st.form_submit_button("解析")