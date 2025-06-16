import streamlit as st# 导入库

st.set_page_config(page_title='Streamlit视频播放器', page_icon='📽')

# 添加标题
st.title("🎬Streamlit视频播放器")
st.text("点击下方视频封面选择要播放的视频")
st.subheader("视频播放")

# 初始化会话状态，用于跟踪当前选中的视频
if 'selected_video' not in st.session_state:
    st.session_state.selected_video = None

# 定义视频数据
videos = {
    "自然风光": {
        "title": "自然风光",
        "description": "美丽的自然景观，山川湖海",
        "duration": "0:27",
        "category": "自然",
        "url": "https://cdn.pixabay.com/video/2025/04/10/271161_large.mp4"
    },
    "城市夜景": {
        "title": "城市夜景",
        "description": "高楼大厦，灯光明亮",
        "duration": "0:30",
        "category": "城市",
        "url": "https://cdn.pixabay.com/video/2022/08/31/129716-745174979_large.mp4"
    },
    "野生动物": {
        "title": "野生动物",
        "description": "活泼可爱",
        "duration": "0:49",
        "category": "动物",
        "url": "https://cdn.pixabay.com/video/2023/09/19/181314-866094614_large.mp4"
    }
}

# 在顶部显示选中的视频
if st.session_state.selected_video:
    video = videos[st.session_state.selected_video]
    st.subheader(f"正在播放: {video['title']}")
    st.text(f"描述：{video['description']}")
    st.text(f"时长{video['duration']}：|分类：{video['category']}")
    st.video(video["url"])
    st.write("---")  # 添加分隔线

# 创建分类选择下拉菜单
st.subheader("视频库")
st.text("点击图片选择视频")
st.text("按分类筛选")
selected_category = st.selectbox(
    '全部',
    ['全部', '自然风光', '城市夜景', '野生动物'],
    label_visibility='collapsed'
)

# 根据选择的分类显示视频
if selected_category == "全部":
    # 显示所有分类的视频
    for category, video in videos.items():
        # 创建一个按钮，点击时更新选中的视频
        col1, col2 = st.columns([1, 11])  # 创建两列布局
        with col1:
            if st.button(f"▶️", key=f"play_{category}"):
                st.session_state.selected_video = category
                
        with col2:
            st.subheader(video["title"])
            st.text(f"描述：{video['description']}")
            st.text(f"时长{video['duration']}：|分类：{video['category']}")
            st.video(video["url"])
else:
    # 只显示所选分类的视频
    video = videos.get(selected_category)
    if video:
        # 创建一个按钮，点击时更新选中的视频
        col1, col2 = st.columns([1, 11])  # 创建两列布局
        with col1:
            if st.button(f"▶️", key=f"play_{selected_category}"):
                st.session_state.selected_video = selected_category
                
        with col2:
            st.subheader(video["title"])
            st.text(f"描述：{video['description']}")
            st.text(f"时长{video['duration']}：|分类：{video['category']}")
            st.video(video["url"])
