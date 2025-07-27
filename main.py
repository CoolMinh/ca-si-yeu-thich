
import streamlit as st

st.title('Điền thông tin giới thiệu bản thân em')

quiz = ['Họ và tên:', 'Ngày tháng năm sinh:', 'Sở thích:']
len_quiz = len(quiz)

# Initialize session state for answers
if 'answers' not in st.session_state:
    st.session_state.answers = ['', '', '']

# Create input fields and store answers
for i in range(len_quiz):
    st.session_state.answers[i] = st.text_input(quiz[i], st.session_state.answers[i])

# Count filled answers
filled_answers = sum(1 for answer in st.session_state.answers if answer.strip() != '')

# Update progress bar
my_bar = st.progress(filled_answers / len_quiz)

if st.button('Confirm'):
    if filled_answers == len_quiz:
        my_bar.progress(1.0)
        st.write('Bạn đã hoàn thành đầy đủ thông tin!')
        st.balloons()
        
        # Display all answers
        st.write("### Thông tin của bạn:")
        for i in range(len_quiz):
            st.write(f"**{quiz[i]}** {st.session_state.answers[i]}")
    else:
        st.write('Bạn chưa hoàn thành đầy đủ thông tin!')
        st.write(f'Đã điền: {filled_answers}/{len_quiz} câu')

if st.button('Reset'):
    st.session_state.answers = ['', '', '']
    st.rerun()
