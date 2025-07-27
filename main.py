
import streamlit as st

st.title('Điền thông tin giới thiệu bản thân')

# Initialize session state
if 'answers' not in st.session_state:
    st.session_state.answers = ['', '', '']

my_bar = st.progress(0)
quiz = ['Họ và tên:', 'Ngày tháng năm sinh:', 'sở thích:']
len_quiz = len(quiz)

# Create input fields and store answers in session state
for i in range(len_quiz):
    st.session_state.answers[i] = st.text_input(quiz[i], st.session_state.answers[i])

# Count non-empty answers
filled_answers = [answer for answer in st.session_state.answers if answer.strip() != '']
num_filled = len(filled_answers)

if st.button('Confirm'):
    if num_filled == len_quiz:
        my_bar.progress(100)
        st.write('Bạn đã hoàn thành đầy đủ thông tin')
        st.balloons()
    else:
        my_bar.progress(num_filled / len_quiz)
        st.write('Bạn chưa hoàn thành đầy đủ thông tin')
    
    # Display filled answers
    for i in range(len_quiz):
        if st.session_state.answers[i].strip() != '':
            st.write(quiz[i], st.session_state.answers[i])
