import streamlit as st

# SIDEBAR
with st.sidebar:
    image = 'https://media.cnn.com/api/v1/images/stellar/prod/200127063956-tyler-the-creator-grammy.jpg?q=x_3,y_3,h_1684,w_2993,c_crop/h_653,w_1160/f_avif'
    st.image(image, caption='Tyler, The Creator')
    st.write("Tên: Tyler Gregory Okonma")
    st.write("Nghệ danh: Tyler, The Creator")
    st.write("""
Tyler The Creator, tên thật là Tyler Gregory Okonma, là một rapper, producer và nghệ sĩ đa ngành người Mỹ.

Anh nổi tiếng với phong cách âm nhạc độc đáo, phá cách, kết hợp giữa hip-hop, alternative và jazz, cùng khả năng sáng tác cực đỉnh.

Bắt đầu nổi lên cùng nhóm nhạc Odd Future, Tyler nhanh chóng xây dựng tên tuổi cá nhân qua các album như Goblin, Wolf, Flower Boy, và đặc biệt là Igor – album đoạt giải Grammy.

Không chỉ làm nhạc, Tyler còn tham gia thiết kế thời trang và đạo diễn video ca nhạc, tạo nên phong cách riêng biệt, đầy màu sắc và cá tính.

Với sự sáng tạo không ngừng, Tyler The Creator là biểu tượng của giới trẻ yêu âm nhạc độc lập và nghệ thuật phá cách.
""")

# BÀI HÁT YÊU THÍCH
st.title('Bài hát yêu thích')

st.write('Like Him')
audio = open('Like Him.mp3', 'rb')
st.audio(audio, format='audio/mp3')

st.write('Glitter')
audio = open('Glitter.mp3', 'rb')
st.audio(audio, format='audio/mp3')

st.write('Ring Ring Ring')
audio = open('Ring Ring Ring.mp3', 'rb')
st.audio(audio, format='audio/mp3')

# MV YÊU THÍCH
st.title('MV yêu thích')

st.write('Sorry Not Sorry')
video = 'https://www.youtube.com/watch?v=LSIOcCcEVaE'
st.video(video)

st.write('See You Again')
video = 'https://www.youtube.com/watch?v=TGgcC5xg9YI'
st.video(video)

st.write('Wharf Talk')
video = 'https://www.youtube.com/watch?v=27FswS3KESk'
st.video(video)

# ALBUM YÊU THÍCH
st.title('Album yêu thích')

st.write('Album Flower Boy (2017)')
image1 = 'https://i.pinimg.com/736x/f8/b4/17/f8b4171d6e522eeccfa1095ac5c56746.jpg'
st.image(image1, caption='Flower Boy')

st.write('Album Igor (2019)')
image2 = 'https://upload.wikimedia.org/wikipedia/en/5/51/Igor_-_Tyler%2C_the_Creator.jpg'
st.image(image2, caption='Igor')

st.write('Album Call Me If You Get Lost (2021)')
image3 = 'https://upload.wikimedia.org/wikipedia/en/3/39/Call_Me_If_You_Get_Lost_vinyl_cover.png'
st.image(image3, caption='Call Me If You Get Lost')
