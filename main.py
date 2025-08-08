import streamlit as st

with st.sidebar:
    image='https://media.cnn.com/api/v1/images/stellar/prod/200127063956-tyler-the-creator-grammy.jpg?q=x_3,y_3,h_1684,w_2993,c_crop/h_653,w_1160/f_avif'
    st.image(image,caption='Tyler,the creator')
    st.write('tên: Tyler Gregory Okonma')
    st.write('nghệ danh:Tyler,the creator')
    st.write('Tyler The Creator, tên thật là Tyler Gregory Okonma, là một rapper, producer, và nghệ sĩ đa ngành người Mỹ. Anh nổi tiếng với phong cách âm nhạc độc đáo, phá cách, kết hợp giữa hip-hop, alternative và jazz, cùng khả năng sáng tác cực đỉnh.

Bắt đầu nổi lên cùng nhóm nhạc Odd Future, Tyler nhanh chóng xây dựng tên tuổi cá nhân qua các album như Goblin, Wolf, Flower Boy, và đặc biệt là Igor – album đoạt giải Grammy. Không chỉ làm nhạc, Tyler còn tham gia thiết kế thời trang và đạo diễn video ca nhạc, tạo nên phong cách riêng biệt, đầy màu sắc và cá tính.

Với sự sáng tạo không ngừng, Tyler The Creator là biểu tượng của giới trẻ yêu âm nhạc độc lập và nghệ thuật phá cách.')
    st.title('Bài hát yêu thích')
    st.write('Answer')
    audio=open('Answer - Tyler, The Creator.mp3','rb')
    st.audio(audio,format='audio/mp3')
    st.write('New magic wand')
    audio=open('Tyler, The Creator - NEW MAGIC WAND (feat. Santigold & Jessy Wilson).mp3','rb')
    st.audio(audio,format='audio/mp3')
    st.write('Sweet/I thought you wanted to dance')
    audio=open('SWEET - I THOUGHT YOU WANTED TO DANCE(Audio).mp3','rb')
    st.audio(audio,format='audio/mp3')
    st.write('Take your mask off')
    
    
    
    