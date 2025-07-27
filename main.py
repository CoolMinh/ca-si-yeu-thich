
import streamlit as st

st.title('Điền thông tin giới thiệu bản thân em')
my_bar = st.progress(0)

quiz = ['Họ và tên:', 'Ngày tháng năm sinh:', 'Sở thích:']

# Initialize session state for answers
if 'answers' not in st.session_state:
    st.session_state.answers = []

len_quiz = len(quiz)

# Clear answers when starting fresh
if st.button('Reset Form'):
    st.session_state.answers = []

st.session_state.answers = []  # Reset for each run
for i in range(len_quiz):
    answer = st.text_input(quiz[i], '')
    if answer != '':
        st.session_state.answers.append(answer)

if st.button('Confirm'):
    if len(st.session_state.answers) == len_quiz:
        my_bar.progress(100)
        st.write('Bạn đã hoàn thành đầy đủ thông tin!')
        st.balloons()
    else:
        my_bar.progress(len(st.session_state.answers)/len_quiz)
        st.write('Bạn chưa hoàn thành đầy đủ thông tin!')

    for i in range(len(st.session_state.answers)):
        st.write(quiz[i], st.session_state.answers[i])
