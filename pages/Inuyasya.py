import pandas as pd
import streamlit as st

def tanpatsu(df,RB_g_len,RB_get_len):
    RB_get_len = RB_get_len - int(RB_g_len/33.6)*50
    RB_g_len = int(RB_g_len) + 12
    RB_df = pd.DataFrame([['RB',RB_g_len,RB_get_len,'四魂ボーナス当選']] , columns=['種別','G数','獲得枚数','備考'])
    df = df.append(RB_df)
    df = df.reset_index(drop=True)
    return df

st.title('犬夜叉')

if 'df' not in st.session_state:
	st.session_state.df = pd.DataFrame(columns=['種別','G数','獲得枚数','備考']) 

if 'now_g' not in st.session_state:
	st.session_state.now_g = 0
else:
    st.write(str(st.session_state.now_g))

st.session_state.now_g = st.number_input('現在のG数',min_value=0,max_value=665)

mode = st.radio('モード',('ビッグボーナス', 'レギュラーボーナス'))

if mode == 'ビッグボーナス':
    with st.form("big_form",True):
        col1, col2 = st.columns(2)
        with col1:
            BB_g_len = st.number_input('G数',min_value=0,max_value=665)
        with col2:
            BB_get_len = st.number_input('獲得枚数',min_value=0,max_value=1000)
        
        submitted = st.form_submit_button("入力")
        if submitted:
            syubetsu = 'BB'
            if not BB_g_len == 0:
                if BB_g_len < 22:
                    bikou = '鉄砕牙チャンス当選'
                else:
                    bikou = 'ブッた斬りスラッシュ直撃当選'
            else:
                bikou = 'ブッた斬りスラッシュ成功'
            kari_df = pd.DataFrame([[syubetsu,BB_g_len,BB_get_len,bikou]],columns=['種別','G数','獲得枚数','備考'])
            st.session_state.df = st.session_state.df.append(kari_df)
            st.session_state.df = st.session_state.df.reset_index(drop=True)
elif mode == 'レギュラーボーナス':
    with st.form("reg_form",True):
        col1, col2 = st.columns(2)
        with col1:
            RB_g_len = st.number_input('G数',min_value=0,max_value=665)
        with col2:
            RB_get_len = st.number_input('獲得枚数',min_value=0,max_value=100)
        
        submitted = st.form_submit_button("入力")
        if submitted:
            st.session_state.df = tanpatsu(st.session_state.df,RB_g_len,RB_get_len)

if not list(st.session_state.df.index)==[]:
    with st.form("syusei",True):
            col1, col2, col3 = st.columns(3)
            with col1:
                index_num = st.selectbox('インデックス番号',tuple(st.session_state.df.index))
            with col2:
                columns_name = st.selectbox('行名',tuple(st.session_state.df.columns))
            with col3:
                syusei_naiyou = st.text_input('修正内容')
            
            submitted_syusei = st.form_submit_button("修正")
            if submitted_syusei:
                st.session_state.df.loc[index_num,columns_name] = syusei_naiyou

if not list(st.session_state.df.index)==[]:
    with st.form("sakuzyo",True):
        index_num = st.selectbox('インデックス番号',tuple(st.session_state.df.index))
    
        submitted_syusei = st.form_submit_button("削除")
        if submitted_syusei:
            st.session_state.df.drop(index=index_num,inplace=True)

kaiseki_submitted = st.button("解析")

if kaiseki_submitted:
    kouzyun_df = st.session_state.df.sort_index(ascending=False).reset_index(drop=True)

    index_li = kouzyun_df.index.values.tolist()
    syubetsu_li = list(kouzyun_df['種別'])
    g_len_li = list(kouzyun_df['G数'])
    get_len_li = list(kouzyun_df['獲得枚数'])
    bikou_li = list(kouzyun_df['備考'])

    now_smai = 0
    now_yuri_g_len = 0
    rest_flg = False
    for i in index_li:
        syubetsu = syubetsu_li[i]
        g_len = g_len_li[i]
        get_len = get_len_li[i]
        bikou = bikou_li[i]
        if syubetsu == 'RB':
            if rest_flg:
                now_smai = 0
                now_yuri_g_len = 0
                rest_flg = False
            now_yuri_g_len = now_yuri_g_len + g_len
            now_smai = now_smai + get_len
        elif syubetsu == 'BB':
            if not i == 0: #インデックスが0ではない＝直撃ではない
                if syubetsu_li[i-1] == 'RB': 
                    if g_len < 22:
                        kouzyun_df.loc[i,'備考'] = '鉄砕牙チャンス当選'
                else:
                    if g_len == 0:
                        kouzyun_df.loc[i,'備考'] = 'ブッた斬りスラッシュ成功'
                    elif 0 < g_len < 13:
                        kouzyun_df.loc[i,'備考'] = 'ブッた斬りゾーン当選'
                        now_smai = 0
                        now_yuri_g_len = 0
                    elif 12 < g_len:
                        kouzyun_df.loc[i,'備考'] = 'ブッた斬りスラッシュ直撃当選'
                        if rest_flg:
                            now_smai = 0
                            now_yuri_g_len = 0
                            rest_flg = False
            now_yuri_g_len = now_yuri_g_len + g_len + int((get_len/4.5))
            now_smai = now_smai - int((g_len/33.6*50)) + get_len
            if 2500 < now_yuri_g_len < 3000:
                rest_flg = True
                kouzyun_df.loc[i,'備考'] = kouzyun_df.loc[i,'備考'] + ':2500G到達'
            if 3000 < now_yuri_g_len:
                rest_flg = True
                kouzyun_df.loc[i,'備考'] = kouzyun_df.loc[i,'備考'] + ':3000G到達'
            if 1000 < now_smai:
                rest_flg = True
                kouzyun_df.loc[i,'備考'] = kouzyun_df.loc[i,'備考'] + ':1000枚到達'

    if rest_flg:
        now_smai = 0
        now_yuri_g_len = 0
        rest_flg = False
    now_yuri_g_len = now_yuri_g_len + st.session_state.now_g
    now_smai = now_smai + int((st.session_state.now_g/33.6*50))

    st.write('現在の状況')
    st.write('有利区間：' + str(now_yuri_g_len))
    st.write('差枚：' + str(now_smai))
    st.dataframe(kouzyun_df)
else:
    st.dataframe(st.session_state.df)

with st.form("kitaichi_form",True):
    col1, col2, col3 = st.columns(3)
    with col1:
        through_name = st.selectbox('スルー回数',('0', '1', '2', '3', '4', '5', '6', '7'))
    with col2:
        game_name = st.selectbox('現在のゲーム数',('0', '50', '100', '150', '200', '250', '300', '350', '400', '450', '500', '550', '600'))
    with col3:
        samai_name = st.selectbox('差枚数',('500', '400', '300', '200', '100', '0', '-100', '-200', '-300', '-400', '-500', '-600', '-700', '-800', '-900', '-1000', '-1100', '-1200', '-1300', '-1400', '-1500', '-1600', '-1700', '-1800', '-1900', '-2000', '-2100', '-2200', '-2300', '-2400', '-2500', '-2600', '-2700', '-2800', '-2900', '-3000'))
    
    kitaichi_submitted = st.form_submit_button("入力")
    if kitaichi_submitted:
        filename = 'data/' + through_name + '_' + game_name + '_' + samai_name + '.csv'
        kitaichi_df = pd.read_csv(filename, index_col=0)
        st.dataframe(kitaichi_df)