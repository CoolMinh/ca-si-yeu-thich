import streamlit as st

# SIDEBAR
with st.sidebar:
    image = 'https://media.cnn.com/api/v1/images/stellar/prod/200127063956-tyler-the-creator-grammy.jpg?q=x_3,y_3,h_1684,w_2993,c_crop/h_653,w_1160/f_avif'
    st.image(image, caption='Tyler, The Creator')
    st.write("Tên: Tyler Gregory Okonma")
    st.write("Nghệ danh: Tyler, The Creator")
    
st.title("Tyler, The Creator")
st.write("""
TYLER, THE CREATOR

Sự nghiệp của Tyler, The Creator là một hành trình lột xác đầy ngoạn mục, từ một rapper nổi loạn gây tranh cãi cho đến một nghệ sĩ được giới phê bình nể trọng và giành nhiều giải Grammy danh giá.

Tyler bắt đầu sự nghiệp với vai trò thủ lĩnh nhóm hip-hop Odd Future, nổi bật với những album đầu tay như Goblin và Wolf. Giai đoạn này, âm nhạc của anh mang phong cách u ám, lofi, lời rap thẳng thắn, thậm chí gây sốc, thường xuyên đả kích xã hội và truyền thông.

Bước ngoặt lớn nhất đến với album Flower Boy (2017), khi Tyler chuyển sang phong cách nhẹ nhàng, giàu cảm xúc hơn, pha trộn soul, jazz và R&B. Album khám phá những chủ đề sâu sắc như cô đơn, tình yêu và sự tìm kiếm bản thân, khẳng định anh không chỉ là rapper gây sốc mà còn là nghệ sĩ có chiều sâu.

Đỉnh cao nghệ thuật là IGOR (2019) – một tác phẩm đột phá tập trung vào hát và sản xuất, kể câu chuyện tình yêu phức tạp qua một nhân vật hư cấu. Với giai điệu synth-pop, R&B ma mị và độc đáo, IGOR mang về cho Tyler giải Grammy Album Rap Xuất sắc nhất, nâng tầm anh thành nhà sản xuất và nghệ sĩ hàng đầu.

Call Me If You Get Lost (2021) đánh dấu sự trở lại với rap trưởng thành, tự tin, theo phong cách mixtape old-school, kể hành trình một “doanh nhân” thành đạt đi khắp thế giới. Album này cũng giúp Tyler giành giải Grammy Album Rap Xuất sắc nhất lần thứ hai.

Mới đây, Tyler tiếp tục gây ấn tượng với hai album mới: Chromakopia (2024) – một tác phẩm thử nghiệm kết hợp hip-hop, jazz, neo-soul và funk, mang tính tự sự sâu sắc; và Don't Tap the Glass (2025) – album mang âm hưởng dance, house, funk và techno, ngắn gọn nhưng đầy năng lượng, thể hiện sự đa dạng không ngừng trong âm nhạc của Tyler.

Tóm lại, Tyler, The Creator là nghệ sĩ không ngừng thay đổi, thử nghiệm và định hình lại bản thân qua mỗi album. Anh không chỉ là rapper, mà còn là nhà sản xuất tài ba, đạo diễn MV sáng tạo và biểu tượng thời trang cá tính.


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

st.write('Are we still friends')
audio = open('Tyler, The Creator - ARE WE STILL FRIENDS-.mp3', 'rb')
st.audio(audio, format='audio/mp3')

st.write('Sweet/I thought you wanted to dance')
audio = open('SWEET - I THOUGHT YOU WANTED TO DANCE (Audio).mp3', 'rb')
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
video = 'https://www.youtube.com/watch?v=Qer3lwd5hyA&list=RDQer3lwd5hyA&start_radio=1'
st.video(video)
st.write('A boy is a gun(2019)')
video = 'https://www.youtube.com/watch?v=9JQDPjpfiGw&list=RD9JQDPjpfiGw&start_radio=1'
st.video(video)
# ALBUM YÊU THÍCH
st.title('Một số album nổi tiếng')

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


