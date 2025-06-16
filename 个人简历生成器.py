import streamlit as st# 导入库

st.set_page_config(page_title='个人简历生成器', page_icon='📝',layout='wide')
# 添加标题
st.title("🎨个人简历生成器")
st.text("使用Streamlit创建您的个性化简历")
    
c1,c2=st.columns([1,2])
with c1:
    st.subheader("个人信息表单")
    st.markdown('<hr style="border: none; border-top: 2px solid #007bff; margin: 0;">', unsafe_allow_html=True)

     # 表单组件
    name = st.text_input("姓名", "")
    position = st.text_input("职位", "")
    phone = st.text_input("电话", "")
    email = st.text_input("邮箱", "")
    birth_date = st.date_input("出生日期", value=None)
    gender = st.radio("性别", ["男", "女", "其他"],horizontal=True)
    education = st.selectbox("学历", ["高中", "专科", "本科", "硕士", "博士"])
    # 语言能力（可多选） - 下拉选择框
    language_ability = st.multiselect(
        "语言能力",
        options=["汉语", "英语", "日语", "俄语",'法语','德语','西班牙语'],
        default=[]  # 默认选中项
    )

    language_text = "、".join(language_ability)
    
    # 技能（可多选）- 下拉多选框
    skills = st.multiselect(
        "技能 (可多选)",
        options=["Python", "Java", "JaveScript","HTML/CSS","SQL","数据分析", "机器学习", "深度学习","项目管理","UI/UX设计"],
        default=[]  # 默认选中项
    )

    # 工作经验（年）- 滑块
    work_experience = st.slider(
        "工作经验（年）",
        min_value=0,
        max_value=30,
        value=0,  # 默认值
        step=1  # 步长
    )

    # 期望薪资范围（元）- 双滑块
    salary_min, salary_max = st.slider(
        "期望薪资范围（元）",
        min_value=5000,
        max_value=50000,
        value=(10000, 20000),  # 默认的区间值
        step=1  # 步长
    )
    # 显示当前选择的薪资区间
    st.write(f"当前选择：{salary_min} - {salary_max} 元")

    # 个人简介 - 文本框
    personal_intro = st.text_area(
        label="个人简介",
        height=150,  
        placeholder="请简要介绍您的专业背景、职业目标和个人特点..."
    )

    # 每日最佳联系时间段 - 下拉选择框
    time_options = []
    for hour in range(0, 24):  # 小时范围 0~1
        for minute in [0, 15, 30, 45]:
            time_str = f"{hour:02d}:{minute:02d}"
            time_options.append(time_str)
    best_contact_time = st.selectbox(
        "每日最佳联系时间段",
        options=time_options,
        index=32 # 默认的时间段
    )

    # 上传个人照片 - 文件上传组件
    uploaded_file = st.file_uploader(
        "上传个人照片",
        type=["jpg", "jpeg", "png"],  # 允许上传的文件类型
        accept_multiple_files=False  # 是否允许上传多个文件
    )
    # 如果有文件上传，简单显示文件名（预览图片，可结合 st.image 实现）
    if uploaded_file:
        st.write(f"已上传照片：{uploaded_file.name}")
with c2:
    st.subheader("简历实时预览")
    st.markdown('<hr style="border: none; border-top: 2px solid #007bff; margin: 0;">', unsafe_allow_html=True)
    
    c1,c2=st.columns([1,2])
    with c1:
        st.write(f"{name}")
        if uploaded_file:
            st.image(uploaded_file)
        st.write(f"**职位**：{position}")
        st.write(f"**电话**：{phone}")
        st.write(f"**邮箱**：{email}")
        if birth_date:
            st.write(f"**出生日期**：{birth_date.strftime('%Y/%m/%d')}")
    with c2:
         st.write(f"**性别**：{gender}")
         st.write(f"**学历**：{education}")
         st.write(f"**工作经验**：{work_experience}年")
         st.write(f"**期望薪资**：{salary_min} - {salary_max} 元")
         st.write(f"**最佳联系时间**：{best_contact_time}")
         if language_text:
             st.write(f"**语言能力**：{language_text}")

    st.markdown("---")
    st.write(f"### 个人简介")
    if personal_intro:
        st.write(personal_intro)
    else:
        st.text("这个人很神秘，没有留下任何介绍……")
    if skills:
        if skills:
            st.write(f"### 专业技能")
            st.write('\n'.join([f"* **{skill}**" for skill in skills]))
