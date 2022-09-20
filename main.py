import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
st.title('Streamlit 超入門')

st.write('Display Imag')

condtion = st.sidebar.slider('あなたの今の調子は？',0,10,5)

'コンディション', condtion


option = st.sidebar.text_input('あなたの趣味を教えてください')

'あなたの好きな趣味は、',option,'です'

option = st.selectbox(
    'あなたが好きな数字をいれてください',
    list(range(1,11))
)

'あなたの好きな数字は、',option,'です'
if st.checkbox('Show Image'):
    img = Image.open('../img/1204350-2.jpg')
    st.image(img,caption='Ero',use_column_width=True)

