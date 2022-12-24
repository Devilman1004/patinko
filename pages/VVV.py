import streamlit as st

st.title('革命機ヴァルヴレイヴ')

st.header('noteURL')
st.text('https://note.com/zema/n/ncf5ff14fe77b')

st.header('期待値')

data_wich = st.selectbox('打ち始めor打ち終わり',('打ち始め','打ち終わり'))

if data_wich == '打ち始め':
    data_type = st.selectbox('データ表示機タイプ',('ART表示あり','ART表示なし'))

    if data_type == 'ART表示なし' :
        st.text(data_type)
        
        RB_through = st.selectbox('RBスルー回数',('0','1','2','3','4'))
        
        st.text('スルー回数：' + RB_through)
        
        if RB_through == '0':
            st.subheader('RB 0スルー ボーナス間期待値')
            st.image("https://assets.st-note.com/img/1671053880862-GJLOxWiBcu.png?width=600", use_column_width=True)
            st.subheader('RB 0スルー BBまで期待値')
            st.image("https://assets.st-note.com/img/1671053858042-0Cwx5Ksk2v.png?width=600", use_column_width=True)
        elif RB_through == '1':
            st.subheader('RB 1スルー ボーナス間期待値')
            st.image("https://assets.st-note.com/img/1671053896835-IE3CnrsIGy.png?width=600", use_column_width=True)
            st.subheader('RB 1スルー BBまで期待値')
            st.image("https://assets.st-note.com/img/1671053976718-4Ev24GzBGl.png?width=600", use_column_width=True)
        elif RB_through == '2':
            st.subheader('RB 2スルー ボーナス間期待値')
            st.image("https://assets.st-note.com/img/1671053904935-ea0yVGmdsu.png?width=600", use_column_width=True)
            st.subheader('RB 2スルー BBまで期待値')
            st.image("https://assets.st-note.com/img/1671053991629-rhlwwJrvmF.png?width=600", use_column_width=True)
        elif RB_through == '3':
            st.subheader('RB 3スルー ボーナス間期待値')
            st.image("https://assets.st-note.com/img/1671053912722-ZiXh9BkFC7.png?width=600", use_column_width=True)
            st.subheader('RB 3スルー BBまで期待値')
            st.image("https://assets.st-note.com/img/1671054005878-kq6VqcKEJX.png?width=600", use_column_width=True)
        elif RB_through == '4':
            st.subheader('RB 4スルー BBまで期待値')
            st.image("https://assets.st-note.com/img/1671054016717-Bu0U3blEaH.png?width=600", use_column_width=True)
        
    elif data_type == 'ART表示あり' :
        st.text(data_type)
        
        CZ_through = st.selectbox('CZスルー回数',('0','1','2','3','4','5'))
        st.text('CZスルー回数:' + CZ_through)
        RB_through = st.selectbox('RBスルー回数',('0','1','2','3','4'))
        st.text('RBスルー回数:' + RB_through)
        
        if RB_through == '0' and CZ_through == '0':
            st.subheader('RB 0スルー・CZ 0スルー 期待値表')
            st.image("https://assets.st-note.com/img/1671051876577-12i1wSOWlo.png?width=2000&height=2000&fit=bounds&format=jpg&quality=85", use_column_width=True)            
        if RB_through == '0' and CZ_through == '1':
            st.subheader('RB 0スルー・CZ 1スルー 期待値表')
            st.image("https://assets.st-note.com/img/1671052080831-b6VyqfUMGF.png?width=600", use_column_width=True)            
        if RB_through == '0' and CZ_through == '2':
            st.subheader('RB 0スルー・CZ 2スルー 期待値表')
            st.image("https://assets.st-note.com/img/1671052139017-6zKMhqfVCM.png?width=600", use_column_width=True)  
        if RB_through == '0' and CZ_through == '3':
            st.subheader('RB 0スルー・CZ 3スルー 期待値表')
            st.image("https://assets.st-note.com/img/1671052156246-SoJhIy4Gri.png?width=600", use_column_width=True) 
        if RB_through == '0' and CZ_through == '4':
            st.subheader('RB 0スルー・CZ 4スルー 期待値表')
            st.image("https://assets.st-note.com/img/1671052196166-zpTKTYXdDx.png?width=600", use_column_width=True)
        if RB_through == '0' and CZ_through == '5':
            st.subheader('RB 0スルー・CZ 5スルー 期待値表')
            st.image("https://assets.st-note.com/img/1671052224484-GpgCkk9QBB.png?width=600", use_column_width=True) 
        if RB_through == '1' and CZ_through == '0':
            st.subheader('RB 1スルー・CZ 0スルー 期待値表')
            st.image("https://assets.st-note.com/img/1671052248804-BhfDbxDOZf.png?width=600", use_column_width=True)
        if RB_through == '1' and CZ_through == '1':
            st.subheader('RB 1スルー・CZ 1スルー 期待値表')
            st.image("https://assets.st-note.com/img/1671052292848-nVEmQ1fPQD.png?width=600", use_column_width=True)
        if RB_through == '1' and CZ_through == '2':
            st.subheader('RB 1スルー・CZ 2スルー 期待値表')
            st.image("https://assets.st-note.com/img/1671052328969-zBPwEQ6vaR.png?width=600", use_column_width=True)
        if RB_through == '1' and CZ_through == '3':
            st.subheader('RB 1スルー・CZ 3スルー 期待値表')
            st.image("https://assets.st-note.com/img/1671052347820-nhkhH5tlxq.png?width=600", use_column_width=True)
        if RB_through == '2' and CZ_through == '0':
            st.subheader('RB 2スルー・CZ 0スルー 期待値表')
            st.image("https://assets.st-note.com/img/1671052361930-3yD8wPBBpd.png?width=600", use_column_width=True)
        if RB_through == '2' and CZ_through == '1':
            st.subheader('RB 2スルー・CZ 1スルー 期待値表')
            st.image("https://assets.st-note.com/img/1671052385523-wU7V3KqbBf.png?width=600", use_column_width=True)
        if RB_through == '2' and CZ_through == '2':
            st.subheader('RB 2スルー・CZ 2スルー 期待値表')
            st.image("https://assets.st-note.com/img/1671052418270-nq5aKDDFoN.png?width=600", use_column_width=True)
        if RB_through == '3' and CZ_through == '0':
            st.subheader('RB 3スルー・CZ 0スルー 期待値表')
            st.image("https://assets.st-note.com/img/1671052429399-EA20yiRD1e.png?width=600", use_column_width=True)
                                            
elif data_wich == '打ち終わり':
    
    st.text('打つ場合は画面上部の紫のモヤモヤがなくなるまで！！')
    
    hikimodoshi_type = st.selectbox('最後の当たり',('CZ後','RB後','BB単発後','革命ラッシュBB2連~4連以下後','超革命ラッシュBB4連以上後'))

    if hikimodoshi_type == 'CZ後':
        st.image("https://assets.st-note.com/img/1671052916270-b905RQqTqz.png?width=600", use_column_width=True)
    elif hikimodoshi_type == 'RB後':
        st.image("https://assets.st-note.com/img/1671053001235-yPTx5adLTe.png?width=600", use_column_width=True)
    elif hikimodoshi_type == 'BB単発後':
        st.image("https://assets.st-note.com/img/1671053083213-YFpAvQauzh.png?width=600", use_column_width=True)
    elif hikimodoshi_type == '革命ラッシュBB2連~4連以下後':
        st.image("https://assets.st-note.com/img/1671053162369-fYXv9xWctz.png?width=600", use_column_width=True)
    elif hikimodoshi_type == '超革命ラッシュBB4連以上後':
        st.image("https://assets.st-note.com/img/1671053292996-4khc7UUgVv.png?width=600", use_column_width=True)
