import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('パチンコ・パチスロ期待値稼働')

st.text_input('機種名')
st.number_input('ゲーム数',0,2000)

st.number_input('投資金額',0,1000000)
st.number_input('投資メダル枚数',0,1000000)
st.number_input('投資玉数',0,1000000)

st.number_input('収入金額',0,1000000)
st.number_input('収入メダル枚数',0,1000000)
st.number_input('収入玉数',0,1000000)