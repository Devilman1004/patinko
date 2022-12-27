import streamlit as st

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
            
if 'befor_kaiten_len' not in st.session_state:
    st.session_state.befor_kaiten_len = 0
if 'now_kaiten_len' not in st.session_state:
    st.session_state.now_kaiten_len = 0
if 'push_len' not in st.session_state:
    st.session_state.push_len = 0
    
st.session_state.befor_kaiten_len = st.number_input('打ち始めの回転数',0,10000,st.session_state.befor_kaiten_len,1)
st.session_state.now_kaiten_len = st.number_input('現在の回転数',0,10000,0,1)
st.session_state.push_len = st.number_input('プッシュ数',0,10000,st.session_state.push_len,1)

kaitenritsu_button = st.button('計算')
if kaitenritsu_button:
    my_kaiten_len = st.session_state.now_kaiten_len - st.session_state.befor_kaiten_len
    my_kaitenritsu = my_kaiten_len / st.session_state.push_len
    st.text('回転数:' + str(my_kaiten_len))
    st.text('回転率:' + str(my_kaitenritsu))
    
st.subheader('※注意書き')
st.text('1 打ち始めの回転数を入れる')
st.text('2 ワンプッシュ分打ち終わったら現在の回転数とプッシュを１回追加')
