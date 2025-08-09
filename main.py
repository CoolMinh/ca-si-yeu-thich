import streamlit as st

# SIDEBAR
with st.sidebar:
    image = 'https://media.cnn.com/api/v1/images/stellar/prod/200127063956-tyler-the-creator-grammy.jpg?q=x_3,y_3,h_1684,w_2993,c_crop/h_653,w_1160/f_avif'
    st.image(image, caption='Tyler, The Creator')
    st.write("Tên: Tyler Gregory Okonma")
    st.write("Nghệ danh: Tyler, The Creator")
    st.write("""
TYLER, THE CREATOR

Sự nghiệp của Tyler, the Creator là một hành trình lột xác đầy ngoạn mục, từ một rapper nổi loạn gây tranh cãi cho đến một nghệ sĩ được giới phê bình nể trọng và giành nhiều giải Grammy danh giá.

Tyler bắt đầu sự nghiệp với vai trò thủ lĩnh của nhóm nhạc hip-hop Odd Future. Giai đoạn này được định hình bởi những album đầu tay như Goblin và Wolf. Âm nhạc của anh mang phong cách u ám, lofi, với ca từ gây sốc, thường xuyên đả kích xã hội và truyền thông.

Bước ngoặt lớn nhất đến với album Flower Boy (2017). Tyler đã thay đổi hoàn toàn phong cách, chuyển sang một âm hưởng nhẹ nhàng, giàu cảm xúc hơn với sự pha trộn của soul, jazz và R&B. Album này khám phá những chủ đề sâu lắng như sự cô đơn, tình yêu và việc tìm kiếm bản thân, chứng tỏ Tyler không chỉ là một rapper gây sốc mà còn là một nghệ sĩ có chiều sâu.

Đỉnh cao nghệ thuật đến với album IGOR (2019). Đây là một sự đột phá hoàn toàn, nơi Tyler tập trung vào hát và sản xuất, tạo nên một câu chuyện tình yêu phức tạp qua một nhân vật hư cấu. Với những giai điệu synth-pop, R&B đầy ma mị và khác lạ, IGOR đã giành giải Grammy Album Rap Xuất sắc nhất, khẳng định vị thế của anh như một nhà sản xuất và nghệ sĩ hàng đầu.

Với CALL ME IF YOU GET LOST (2021), Tyler trở lại với rap, nhưng là một phiên bản trưởng thành, tự tin hơn bao giờ hết. Album mang phong cách mixtape old-school, kể về hành trình của một "doanh nhân" thành đạt đi khắp thế giới. Album này cũng đã mang về cho anh giải Grammy Album Rap Xuất sắc nhất lần thứ hai.

Tóm lại, Tyler, the Creator là một nghệ sĩ không ngừng thay đổi, không ngại thử nghiệm và luôn biết cách định hình lại bản thân qua mỗi album. Anh không chỉ là một rapper mà còn là một nhà sản xuất tài ba, một đạo diễn MV sáng tạo và một biểu tượng thời trang đầy cá tính.
""")

# BÀI HÁT YÊU THÍCH
st.title('Bài hát yêu thích')

st.write('Like Him(2024)')
audio = open('Like Him.mp3', 'rb')
st.audio(audio, format='audio/mp3')

st.write('Glitter(2017)')
audio = open('Glitter.mp3', 'rb')
st.audio(audio, format='audio/mp3')

st.write('Ring Ring Ring(2025)')
audio = open('Ring Ring Ring.mp3', 'rb')
st.audio(audio, format='audio/mp3')

# MV YÊU THÍCH
st.title('MV yêu thích')

st.write('Sorry Not Sorry(2023)')
video = 'https://www.youtube.com/watch?v=LSIOcCcEVaE'
st.video(video)

st.write('See You Again(2017)')
video = 'https://www.youtube.com/watch?v=TGgcC5xg9YI'
st.video(video)

st.write('Wharf Talk(2023)')
video = 'https://www.youtube.com/watch?v=27FswS3KESk'
st.video(video)
st.write('Noid(2024)')
video = 'https://www.youtube.com/watch?v=Qer3lwd5hyA'
st.video(video)
# ALBUM YÊU THÍCH
st.title('Album yêu thích')

st.write('Album Flower Boy (2017)')
st.markdown(' link=https://open.spotify.com/album/2nkto6YNI4rUYTLqEwWJ3o', unsafe_allow_html=True)

image1 = 'https://i.pinimg.com/736x/f8/b4/17/f8b4171d6e522eeccfa1095ac5c56746.jpg'
st.image(image1, caption='Flower Boy')

st.write('Album Igor (2019)')
st.markdown(' link=https://open.spotify.com/album/5zi7WsKlIiUXv09tbGLKsE', unsafe_allow_html=True)
image2 = 'https://i.pinimg.com/736x/ce/0e/b3/ce0eb36ab9cfb0039e1c46f20b69dcfa.jpg'
st.image(image2, caption='Igor')

st.write('Album Call Me If You Get Lost (2021)')
st.markdown(' link=https://open.spotify.com/album/1GG6U2SSJPHO6XsFiBzxYv', unsafe_allow_html=True)
image3 = 'https://i.pinimg.com/1200x/52/b4/9a/52b49ad421bdc5accaf5dd9aaf3d99fc.jpg'
st.image(image3, caption='Call Me If You Get Lost')
