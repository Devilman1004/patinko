import streamlit as st

st.title('リノヘブン')

st.header('期待値')

with st.expander("スルー別ボーナス間天井期待値"):
    st.header('スルー別ボーナス間天井期待値')

with st.expander("スルー別天国間天井期待値"):
    st.header('スルー別天国間天井期待値')

with st.expander("朝イチボーナス間天井期待値"):
    st.header('朝イチボーナス間天井期待値')

with st.expander("天国後200以内当選後 １スルーボーナス間期待値"):
    st.header('天国後200以内当選後 １スルーボーナス間期待値')

with st.expander("天国後200以降当選後 １スルーボーナス間期待値"):
    st.header('天国後200以降当選後 １スルーボーナス間期待値')

with st.expander("天国でそこそこ出た後の0スルーボーナス間期待値"):
    st.header('天国でそこそこ出た後の0スルーボーナス間期待値')

with st.expander("0スルー 引き戻しゾーン狙い期待値"):
    st.header('0スルー 引き戻しゾーン狙い期待値')

st.header('やめどき')
st.text('・ボーナス後、32Gまわしてやめ。')
st.text('・慎重派は33Gまで回していいと思います。')