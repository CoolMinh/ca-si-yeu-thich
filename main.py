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
st.write('Like him')
audio=open('Like Him.mp3','rb')
st.audio(audio,format='audio/mp3')
st.write('Glitter')
audio=open('Gliter.mp3','rb')
st.audio(audio,format='audio/mp3')
st.write('ring ring ring')
audio=open('Ring Ring Ring.mp3','rb')
st.audio(audio,format='audio/mp3')
st.title('Mv yêu thích')
st.write('sorry not sorry')
video='https://www.youtube.com/watch?v=LSIOcCcEVaE&list=RDLSIOcCcEVaE&start_radio=1'
st.video(video.format='video/mp4')
st.write('see you again')
video='https://www.youtube.com/watch?v=TGgcC5xg9YI&list=RDTGgcC5xg9YI&start_radio=1'
st.video(video.format='video/mp4')
st.write('wharf talk')
video='https://www.youtube.com/watch?v=27FswS3KESk&list=RD27FswS3KESk&start_radio=1'
st.video(video.format='video/mp4')
st.title('Album yêu thích'):
st.write('lbum Flower Boy (2017)')
image1='https://upload.wikimedia.org/wikipedia/vi/5/59/Flower_Boy.jpg'
st.image(image1,caption='Flower Boy)
st.write('album Igor (2019)')
image2='https://upload.wikimedia.org/wikipedia/en/5/51/Igor_-_Tyler%2C_the_Creator.jpg'
st.image(image2,caption='Igor')
iamge3='https://upload.wikimedia.org/wikipedia/en/3/39/Call_Me_If_You_Get_Lost_vinyl_cover.png'
st.image(image3,caption='Call me if you get lost')