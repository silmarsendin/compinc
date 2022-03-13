import streamlit as st
from PIL import Image
image = Image.open('compinc.png')
st.image(image)


altura = st.select_slider('Defina a altura da edificação',options=['Térrea', '<= 6,00 m', '> 6,00 m e <= 12,00 m', '> 12,00 e <= 23,00 m', '> 23,00 m e <=30,00 m', '> 30,00 m'])

grupo = st.selectbox('Defina o Grupo de Edificação: ',['A - Residencial','B - Hospedagem','C - Comercial','D - Serviços', 'E - Educacional','F - Reunião de Público','G - Serviço Automotivo','H - Saúde e Institucional','I - Industria','J - Depósito','K - Energia','M - Especial'])
if grupo == 'A - Residencial':
    st.write('Não é exigido o sistema de compartimentação')
elif grupo == 'B - Hospedagem':
    if altura == 'Térrea':
        st.write('Não é exigida a compartimentação.')
    elif altura == '<= 6,00 m':
        st.write('Deve haver compartimentação a cada 5.000 m2.')
        st.write('Devem ser atendidas somente as regras específicas de compartimentação entre unidades autônomas.')
    elif altura == '> 6,00 m e <= 12,00 m':
        st.write('Deve haver compartimentação a cada 4.000 m2.')
        st.write('Pode ser substituído por chuveiros automáticos.')
    elif altura == '> 12,00 e <= 23,00 m':
        st.write('Deve haver compartimentação a cada 3.000 m2.')
        st.write('Pode ser substituído por sistema de detecção de incêndios e chuveiros automáticos.')
    elif altura == '> 23,00 m e <=30,00 m':
        st.write('Deve haver compartimentação a cada 2.000 m2.')
        st.write('Pode ser substituído por sistema de detecção de incêndios e chuveiros automáticos.')
    elif altura == '> 30,00 m':
        st.write('Deve haver compartimentação a cada 1.500 m2.')

elif grupo == 'C - Comercial':
    divisao = st.selectbox('Defina a divisão da ocupação:',['C-1','C-2','C-3'])
    if divisao == 'C-1':
        if altura == 'Térrea':
            st.write('Deve haver compartimentação a cada 5.000 m2.')
            st.write('Pode ser substituído por chuveiros automáticos.')
        elif altura == '<= 6,00 m':
            st.write('Deve haver compartimentação a cada 3.000 m2.')
            st.write('Pode ser substituído por chuveiros automáticos.')
        elif altura == '> 6,00 m e <= 12,00 m':
            st.write('Deve haver compartimentação a cada 2.000 m2.')
            st.write('Pode ser substituído por sistema de detecção de incêndios e chuveiros automáticos.')
        elif altura == '> 12,00 e <= 23,00 m':
            st.write('Deve haver compartimentação a cada 2.000 m2.')
            st.write('Pode ser substituído por sistema de detecção de incêndios e chuveiros automáticos.')
        elif altura == '> 23,00 m e <=30,00 m':
            st.write('Deve haver compartimentação a cada 1.500 m2.')
            st.write('Pode ser substituído por sistema de detecção de incêndios e chuveiros automáticos.')
        elif altura == '> 30,00 m':
            st.write('Deve haver compartimentação a cada 1.500 m2.')
            st.write('Pode ser substituído por sistema de detecção de incêndios e chuveiros automáticos.')
    if divisao == 'C-2':
        if altura == 'Térrea':
            st.write('Deve haver compartimentação a cada 5.000 m2.')
            st.write('Pode ser substituído por chuveiros automáticos.')
        elif altura == '<= 6,00 m':
            st.write('Deve haver compartimentação a cada 3.000 m2.')
            st.write('Pode ser substituído por chuveiros automáticos.')
        elif altura == '> 6,00 m e <= 12,00 m':
            st.write('Deve haver compartimentação a cada 2.000 m2.')
            st.write('Pode ser substituído por sistema de detecção de incêndios e chuveiros automáticos.')
        elif altura == '> 12,00 e <= 23,00 m':
            st.write('Deve haver compartimentação a cada 2.000 m2.')
            st.write('Pode ser substituído por sistema de detecção de incêndios e chuveiros automáticos.')
        elif altura == '> 23,00 m e <=30,00 m':
            st.write('Deve haver compartimentação a cada 1.500 m2.')
            st.write('Pode ser substituído por sistema de detecção de incêndios e chuveiros automáticos.')
        elif altura == '> 30,00 m':
            st.write('Deve haver compartimentação a cada 1.500 m2.')
            st.write('Pode ser substituído por sistema de detecção de incêndios e chuveiros automáticos.')
    elif divisao == 'C-3':
        if altura == 'Térrea':
            st.write('Deve haver compartimentação a cada 5.000 m2.')
            st.write('Pode ser substituído por chuveiros automáticos.')
        elif altura == '<= 6,00 m':
            st.write('Deve haver compartimentação a cada 2.500 m2.')
            st.write('Pode ser substituído por chuveiros automáticos.')
        elif altura == '> 6,00 m e <= 12,00 m':
            st.write('Deve haver compartimentação a cada 1.500 m2.')
            st.write('Pode ser substituído por sistema de detecção de incêndios e chuveiros automáticos.')
        elif altura == '> 12,00 e <= 23,00 m':
            st.write('Deve haver compartimentação a cada 1.000 m2.')
            st.write('Pode ser substituído por sistema de detecção de incêndios e chuveiros automáticos.')
        elif altura == '> 23,00 m e <=30,00 m':
            st.write('Deve haver compartimentação a cada 2.000 m2.')
            st.write('Pode ser substituído por sistema de detecção de incêndios e chuveiros automáticos.')
        elif altura == '> 30,00 m':
            st.write('Deve haver compartimentação a cada 2.000 m2.')
            st.write('Pode ser substituído por sistema de detecção de incêndios e chuveiros automáticos.')

elif grupo == 'D - Serviços':
    if altura == 'Térrea':
        st.write('Deve haver compartimentação a cada 5.000 m2.')
        st.write('Pode ser substituído por chuveiros automáticos.')
    elif altura == '<= 6,00 m':
        st.write('Deve haver compartimentação a cada 2.500 m2.')
        st.write('Pode ser substituído por chuveiros automáticos.')
    elif altura == '> 6,00 m e <= 12,00 m':
        st.write('Deve haver compartimentação a cada 1.500 m2.')
        st.write('Pode ser substituído por chuveiros automáticos.')
    elif altura == '> 12,00 e <= 23,00 m':
        st.write('Deve haver compartimentação a cada 1.000 m2.')
        st.write('Pode ser substituído por sistema de detecção de incêndios e chuveiros automáticos.')
    elif altura == '> 23,00 m e <=30,00 m':
        st.write('Deve haver compartimentação a cada 800 m2.')
        st.write('Pode ser substituído por sistema de detecção de incêndios e chuveiros automáticos.')
    elif altura == '> 30,00 m':
        st.write('Deve haver compartimentação a cada 2.000 m2.')

elif grupo == 'E - Educacional':
    if altura == 'Térrea':
        st.write('Não é exigida a compartimentação.')
    elif altura == '<= 6,00 m':
        st.write('Não é exigida a compartimentação.')
    elif altura == '> 6,00 m e <= 12,00 m':
        st.write('Não é exigida a compartimentação.')
    elif altura == '> 12,00 e <= 23,00 m':
        st.write('Não é exigida a compartimentação.')
    elif altura == '> 23,00 m e <=30,00 m':
        st.write('Deve haver compartimentação a cada 1.500 m2.')
        st.write('Pode ser substituído por sistema de detecção de incêndios e chuveiros automáticos.')
    elif altura == '> 30,00 m':
        st.write('Deve haver compartimentação a cada 2.000 m2.')

elif grupo == 'F - Reunião de Público':
    divisao = st.selectbox('Defina a divisão da ocupação:',['F-1','F-2','F-3','F-4','F-5','F-6','F-7','F-8','F-9','F-10','F-11'])
    if divisao == 'F-1' or divisao == 'F-2' or divisao == 'F-3' or divisao == 'F-4' or divisao == 'F-7' or divisao == 'F-9':
            st.write('Não é exigido o sistema de compartimentação')

    if divisao == 'F-5' or divisao == 'F-6':
        if altura == 'Térrea':
            st.write('Deve haver compartimentação a cada 5.000 m2.')
            st.write('Pode ser substituído por sistema de detecção de incêndios e chuveiros automáticos.')
        elif altura == '<= 6,00 m':
            st.write('Deve haver compartimentação a cada 4.000 m2.')
            st.write('Pode ser substituído por sistema de detecção de incêndios e chuveiros automáticos.')
        elif altura == '> 6,00 m e <= 12,00 m':
            st.write('Deve haver compartimentação a cada 3.000 m2.')
            st.write('Pode ser substituído por sistema de detecção de incêndios e chuveiros automáticos.')
        elif altura == '> 12,00 e <= 23,00 m':
            st.write('Deve haver compartimentação a cada 2.000 m2.')
            st.write('Pode ser substituído por sistema de detecção de incêndios e chuveiros automáticos.')
        elif altura == '> 23,00 m e <=30,00 m':
            st.write('Deve haver compartimentação a cada 1.000 m2.')
        elif altura == '> 30,00 m':
            st.write('Deve haver compartimentação a cada 1.500 m2.')

    if divisao == 'F-8':
        if altura == 'Térrea':
            st.write('Não é exigido o sistema de compartimentação')
        elif altura == '<= 6,00 m':
           st.write('Não é exigido o sistema de compartimentação')
        elif altura == '> 6,00 m e <= 12,00 m':
            st.write('Não é exigido o sistema de compartimentação')
        elif altura == '> 12,00 e <= 23,00 m':
            st.write('Deve haver compartimentação a cada 2.000 m2.')
            st.write('Pode ser substituído por sistema de detecção de incêndios e chuveiros automáticos.')
        elif altura == '> 23,00 m e <=30,00 m':
            st.write('Deve haver compartimentação a cada 1.000 m2.')
        elif altura == '> 30,00 m':
            st.write('Deve haver compartimentação a cada 1.500 m2.')

    if divisao == 'F-10':
        if altura == 'Térrea':
            st.write('Deve haver compartimentação a cada 5.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '<= 6,00 m':
            st.write('Deve haver compartimentação a cada 2.500 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 6,00 m e <= 12,00 m':
            st.write('Deve haver compartimentação a cada 1.500 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 12,00 e <= 23,00 m':
            st.write('Deve haver compartimentação a cada 1.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 23,00 m e <=30,00 m':
            st.write('Deve haver compartimentação a cada 1.000 m2.')
        elif altura == '> 30,00 m':
            st.write('Deve haver compartimentação a cada 1.000 m2.')
            
    if divisao == 'F-11':
        if altura == 'Térrea':
            st.write('Deve haver compartimentação a cada 5.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '<= 6,00 m':
            st.write('Deve haver compartimentação a cada 2.500 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 6,00 m e <= 12,00 m':
            st.write('Deve haver compartimentação a cada 1.500 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 12,00 e <= 23,00 m':
            st.write('Deve haver compartimentação a cada 1.000 m2.')
            st.write('Pode ser substituído por sistema de detecção de incêndios e chuveiros automáticos.')
        elif altura == '> 23,00 m e <=30,00 m':
            st.write('Deve haver compartimentação a cada 1.000 m2.')
        elif altura == '> 30,00 m':
            st.write('Deve haver compartimentação a cada 1.000 m2.')     

elif grupo == 'G - Serviço Automotivo':
    divisao = st.selectbox('Defina a divisão da ocupação:',['G-1','G-2','G-3','G-4','G-5'])
    if divisao == 'G-1' or divisao == 'G-2' or divisao == 'G-3' or divisao == 'G-5':
            st.write('Não é exigido o sistema de compartimentação')

    if divisao == 'G-4':
        if altura == 'Térrea':
            st.write('Deve haver compartimentação a cada 10.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '<= 6,00 m':
            st.write('Deve haver compartimentação a cada 5.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 6,00 m e <= 12,00 m':
            st.write('Deve haver compartimentação a cada 3.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 12,00 e <= 23,00 m':
            st.write('Deve haver compartimentação a cada 2.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 23,00 m e <=30,00 m':
            st.write('Deve haver compartimentação a cada 1.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 30,00 m':
            st.write('Deve haver compartimentação a cada 1.000 m2.')

elif grupo == 'H - Saúde e Institucional':
    divisao = st.selectbox('Defina a divisão da ocupação:',['H-1','H-2','H-3','H-4','H-5','H-6'])
    if divisao == 'H-1' or divisao == 'H-2' or divisao == 'H-4' or divisao == 'H-5':
            st.write('Não é exigido o sistema de compartimentação')

    if divisao == 'H-3':
        if altura == 'Térrea':
            st.write('Não é exigido o sistema de compartimentação')
            st.write('Somente as regras específicas de compartimentação entre as unidades autônomas')
        elif altura == '<= 6,00 m':
            st.write('Deve haver compartimentação a cada 5.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 6,00 m e <= 12,00 m':
            st.write('Deve haver compartimentação a cada 3.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 12,00 e <= 23,00 m':
            st.write('Deve haver compartimentação a cada 2.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 23,00 m e <=30,00 m':
            st.write('Deve haver compartimentação a cada 1.500 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 30,00 m':
            st.write('Deve haver compartimentação a cada 1.000 m2.')

    if divisao == 'H-6':
        if altura == 'Térrea':
            st.write('Deve haver compartimentação a cada 5.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '<= 6,00 m':
            st.write('Deve haver compartimentação a cada 2.500 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 6,00 m e <= 12,00 m':
            st.write('Deve haver compartimentação a cada 1.500 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 12,00 e <= 23,00 m':
            st.write('Deve haver compartimentação a cada 1.000 m2.')
            st.write('Pode ser substituído por sistema de detecção de incêndio e chuveiros automáticos.')
        elif altura == '> 23,00 m e <=30,00 m':
            st.write('Deve haver compartimentação a cada 800 m2.')
            st.write('Pode ser substituído por sistema de detecção de incêndio e chuveiros automáticos.')
        elif altura == '> 30,00 m':
            st.write('Deve haver compartimentação a cada 2.000 m2.')

elif grupo == 'I - Industria':
    divisao = st.selectbox('Defina a divisão da ocupação:',['I-1','I-2','I-3'])
    if divisao == 'I-1':
        if altura == 'Térrea':
            st.write('Não é exigido o sistema de compartimentação')
        elif altura == '<= 6,00 m':
            st.write('Deve haver compartimentação a cada 10.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 6,00 m e <= 12,00 m':
            st.write('Deve haver compartimentação a cada 5.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 12,00 e <= 23,00 m':
            st.write('Deve haver compartimentação a cada 3.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 23,00 m e <=30,00 m':
            st.write('Deve haver compartimentação a cada 1.500 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 30,00 m':
            st.write('Deve haver compartimentação a cada 2.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')

    if divisao == 'I-2':
        if altura == 'Térrea':
            st.write('Não é exigido o sistema de compartimentação')
        elif altura == '<= 6,00 m':
            st.write('Deve haver compartimentação a cada 10.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 6,00 m e <= 12,00 m':
            st.write('Deve haver compartimentação a cada 5.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 12,00 e <= 23,00 m':
            st.write('Deve haver compartimentação a cada 3.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 23,00 m e <=30,00 m':
            st.write('Deve haver compartimentação a cada 2.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 30,00 m':
            st.write('Deve haver compartimentação a cada 2.000 m2.')

    if divisao == 'I-3':
        if altura == 'Térrea':
            st.write('Deve haver compartimentação a cada 7.500 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '<= 6,00 m':
            st.write('Deve haver compartimentação a cada 5.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 6,00 m e <= 12,00 m':
            st.write('Deve haver compartimentação a cada 3.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 12,00 e <= 23,00 m':
            st.write('Deve haver compartimentação a cada 2.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 23,00 m e <=30,00 m':
            st.write('Deve haver compartimentação a cada 1.500 m2.')
        elif altura == '> 30,00 m':
            st.write('Deve haver compartimentação a cada 1.500 m2.')

elif grupo == 'J - Depósito':
    divisao = st.selectbox('Defina a divisão da ocupação:',['J-1','J-2','J-3','J-4'])
    if divisao == 'J-1':
        st.write('Não é exigido sistema de compartimentação')

    elif divisao == 'J-2':
        if altura == 'Térrea':
            st.write('Deve haver compartimentação a cada 10.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '<= 6,00 m':
            st.write('Deve haver compartimentação a cada 5.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 6,00 m e <= 12,00 m':
            st.write('Deve haver compartimentação a cada 3.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 12,00 e <= 23,00 m':
            st.write('Deve haver compartimentação a cada 1.500 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 23,00 m e <=30,00 m':
            st.write('Deve haver compartimentação a cada 2.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 30,00 m':
            st.write('Deve haver compartimentação a cada 1.500 m2.')

    if divisao == 'J-3' or divisao == 'J-4':
        if altura == 'Térrea':
            st.write('Deve haver compartimentação a cada 4.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '<= 6,00 m':
            st.write('Deve haver compartimentação a cada 3.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 6,00 m e <= 12,00 m':
            st.write('Deve haver compartimentação a cada 2.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 12,00 e <= 23,00 m':
            st.write('Deve haver compartimentação a cada 2.500 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 23,00 m e <=30,00 m':
            st.write('Deve haver compartimentação a cada 1.500 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 30,00 m':
            st.write('Deve haver compartimentação a cada 1.000 m2.')

elif grupo == 'K - Energia':
    if altura == 'Térrea':
        st.write('Deve haver compartimentação a cada 5.000 m2.')
    elif altura == '<= 6,00 m':
        st.write('Deve haver compartimentação a cada 3.000 m2.')
    elif altura == '> 6,00 m e <= 12,00 m':
        st.write('Deve haver compartimentação a cada 2.000 m2.')
    elif altura == '> 12,00 e <= 23,00 m':
        st.write('Deve haver compartimentação a cada 1.000 m2.')
    elif altura == '> 23,00 m e <=30,00 m':
        st.write('Deve haver compartimentação a cada 500 m2.')
    elif altura == '> 30,00 m':
        st.write('Deve haver compartimentação a cada 500 m2.')

elif grupo == 'M - Especial':
    divisao = st.selectbox('Defina a divisão da ocupação:',['M-2','M-3'])

    if divisao == 'M-2':
        if altura == 'Térrea':
            st.write('Deve haver compartimentação a cada 1.000 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '<= 6,00 m':
            st.write('Deve haver compartimentação a cada 500 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 6,00 m e <= 12,00 m':
            st.write('Deve haver compartimentação a cada 500 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 12,00 e <= 23,00 m':
            st.write('Deve haver compartimentação a cada 300 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 23,00 m e <=30,00 m':
            st.write('Deve haver compartimentação a cada 300 m2.')
            st.write('Pode ser substituído por sistema de chuveiros automáticos.')
        elif altura == '> 30,00 m':
            st.write('Deve haver compartimentação a cada 200 m2.')

    if divisao == 'M-3':
        if altura == 'Térrea':
            st.write('Deve haver compartimentação a cada 5.000 m2.')
        elif altura == '<= 6,00 m':
            st.write('Deve haver compartimentação a cada 3.000 m2.')
        elif altura == '> 6,00 m e <= 12,00 m':
            st.write('Deve haver compartimentação a cada 2.000 m2.')
        elif altura == '> 12,00 e <= 23,00 m':
            st.write('Deve haver compartimentação a cada 1.000 m2.')
        elif altura == '> 23,00 m e <=30,00 m':
            st.write('Deve haver compartimentação a cada 500 m2.')
        elif altura == '> 30,00 m':
            st.write('Deve haver compartimentação a cada 500 m2.')
