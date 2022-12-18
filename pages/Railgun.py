import pandas as pd
import streamlit as st

st.title('レールガン')

st.text('https://slotjin.com/note/railgun-at/')
st.text('https://slotjin.com/note/railgun-cz/')
st.text('600biribiri')

with st.form("rireki",True):
    now = st.number_input('現在のG数',min_value=0,max_value=800)
    through1 = st.number_input('1スルー目',min_value=0,max_value=800)
    through2 = st.number_input('2スルー目',min_value=0,max_value=800)
    through3 = st.number_input('3スルー目',min_value=0,max_value=800)
    through4 = st.number_input('4スルー目',min_value=0,max_value=800)
    through5 = st.number_input('5スルー目',min_value=0,max_value=800)
    through6 = st.number_input('6スルー目',min_value=0,max_value=800)
    
    kitaichi_submitted = st.form_submit_button("解析")
    
    if kitaichi_submitted:
        yurikukan_list = [now,
                          through1,
                          through2,
                          through3,
                          through4,
                          through5,
                          through6]
        
        yurikukan_sum_G = sum(yurikukan_list)
        
        for i in range(1,7):
            if yurikukan_list[i] == 0:
                through_len = i - 1
                break
        
        st.subheader('スルー回数')
        st.text(through_len)       
        
        st.subheader('有利区間ハマりG数')
        st.text(yurikukan_sum_G)
        
        if now < 50:
            now_kizyun = '0'
        elif 50 <= now < 100:
            now_kizyun = '50'
        elif 100 <= now < 150:
            now_kizyun = '100'
        elif 150 <= now < 200:
            now_kizyun = '150'
        elif 200 <= now < 250:
            now_kizyun = '200'
        elif 250 <= now < 300:
            now_kizyun = '250'
        elif 300 <= now < 350:
            now_kizyun = '300'
        elif 350 <= now < 400:
            now_kizyun = '350'
        elif 400 <= now < 450:
            now_kizyun = '400'
        elif 450 <= now < 500:
            now_kizyun = '450'
        elif 500 <= now < 550:
            now_kizyun = '500'
        elif 550 <= now < 600:
            now_kizyun = '550'
        elif 600 <= now:
            now_kizyun = '600'
            
        filename = 'data/Railgun/AT/' + str(through_len) + '_' + now_kizyun + '.csv'
        kitaichi_df = pd.read_csv(filename, index_col=0)
        
        st.dataframe(kitaichi_df)
