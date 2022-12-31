import streamlit as st

st.title('幼女戦記')

st.header('期待値')

with st.expander("スルー別ボーナス間天井期待値"):
    st.header('スルー別ボーナス間天井期待値')

with st.expander("スルー別AT間天井期待値"):
    st.header('スルー別AT間天井期待値')

with st.expander("スルー別ゾーン狙い期待値"):
    st.header('スルー別ゾーン狙い期待値')

with st.expander("朝イチリセット狙い期待値"):
    st.header('朝イチリセット狙い期待値')

with st.expander("前回天国当選後　天国ゾーン狙い期待値"):
    st.header('前回天国当選後　天国ゾーン狙い期待値')

with st.expander("前回通常A ボーナス間期待値"):
    st.header('前回通常A ボーナス間期待値')

with st.expander("天国以上濃厚時 期待値"):
    st.header('天国以上濃厚時 期待値')

with st.expander("256G以内濃厚時 期待値"):
    st.header('256G以内濃厚時 期待値')


st.header('やめどき')
st.text('・ボーナス・AT後、幼女の目覚めステージ、OP203フォローやめ。')
st.subheader('【重要】')
st.text('・ボーナス終了画面でPUSHを押して画面左の宝珠ランプが赤なら天国以上')
st.text('濃厚で超天国にも期待できると解析にはあるのでこの場合は天国まで打っ')
st.text('てください。')
st.text('・OP203終了画面でも天国以上濃厚や、超天国濃厚の画面があるのでそちら')
st.text('も要チェックです。')