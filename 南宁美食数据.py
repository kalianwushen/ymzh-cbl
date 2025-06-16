# 导入库
import streamlit as st
import pandas as pd
import numpy as np
import random

st.set_page_config(page_title="南宁美食数据",page_icon="🧁")# 添加标题

st.title("🍔 南宁美食探索")
st.text("探索广西南宁最受欢迎的美食地点！选择你感兴趣的餐厅类型，查看评分和位置。")
# 餐厅数据
restaurants = pd.DataFrame({
    "餐厅": ["星艺会尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "西冷牛排店"],
    "类型": ["中餐", "中餐", "快餐", "自助餐", "西餐"],
    "评分": [4.2, 4.5, 4.0, 4.7, 4.3],
    "价格": [15, 20, 25, 35, 50],
    "latitude": [22.853838, 22.965046, 22.812200, 22.809105, 22.839699],
    "longitude": [108.222177, 108.353921, 108.266629, 108.378664, 108.245804]
})
st.subheader("💎南宁美食地图")
st.map(restaurants)
st.subheader("⭐餐厅评分")

# 创建条形图
st.bar_chart(restaurants, x='餐厅',y='评分')

# 创建折线图
st.subheader("💰不同类型餐厅价格")
st.line_chart(restaurants, x='类型',y='价格')

st.subheader("⏱用餐高峰时段")
# 构造模拟的用餐高峰时段数据，这里假设按时间点（11.0 - 19.0 间隔 0.5 ）统计各餐厅用餐量
time_points = np.arange(11.0, 19.5, 0.5)
peak_data = {
    "时间": time_points,
    "星艺会尝不忘": np.random.randint(30, 100, size=len(time_points)),
    "高峰柠檬鸭": np.random.randint(30, 100, size=len(time_points)),
    "复记老友粉": np.random.randint(30, 100, size=len(time_points))
}
peak_df = pd.DataFrame(peak_data)
peak_df = peak_df.set_index("时间")  # 设置时间为索引，方便绘图

# 使用st.area_chart绘制面积图
st.area_chart(peak_df)

import streamlit as st

restaurant_data = {
    "星艺会尝不忘": {
        "rating": "4.2/5.0",
        "average_cost": "15元",
        "recommended_dishes": ["桂林米粉", "瘦肉粉", "干拌粉"],
        "crowd_density":84
    },
    "高峰柠檬鸭": {
        "rating": "4.5/5.0",
        "average_cost": "20元",
        "recommended_dishes": ["特色套餐", "地方小吃","时令蔬菜"],
        "crowd_density":90
    },
    "复记老友粉": {
        "rating": "4.0/5.0",
        "average_cost": "25元",
        "recommended_dishes": ["老友牛肉", "老友猪肉","炒粉"],
        "crowd_density":80
    },
    "好有缘": {
        "rating": "4.7/5.0",
        "average_cost": "35元",
        "recommended_dishes": ["特色套餐", "地方小吃","时令蔬菜"],
        "crowd_density":94
    },
    "白妈螺蛳粉": {
        "rating": "4.3/5.0",
        "average_cost": "50元",
        "recommended_dishes": ["特色套餐", "地方小吃","时令蔬菜"],
        "crowd_density":86
    }
}

st.subheader("餐厅详情")
selected_restaurant = st.selectbox("选择餐厅查看详情", list(restaurant_data.keys()))

if selected_restaurant:
    data = restaurant_data[selected_restaurant]
      
    # 使用容器组织内容
    with st.container():
        st.markdown(f"### {selected_restaurant}")
        
        # 基本信息区域
        st.write(f"评分：{data['rating']}")
        st.write(f"人均消费：{data['average_cost']}")
        
        # 添加分隔线
        st.divider()
        
        # 推荐菜品区域
        st.subheader("推荐菜品")
        for dish in data["recommended_dishes"]:
            st.write(f"- {dish}")

    st.subheader("当前拥挤程度")
    crowd_percent = data['crowd_density']
    st.write(f"{crowd_percent}% 拥挤")
    progress_bar = st.progress(crowd_percent)
    
st.subheader("5个餐厅12个月价格走势折线图")
# 定义数据
data = {
    '月份':['01月', '02月', '03月','04月','05月','06月','07月','08月','09月','10月','11月','12月'],
    '星艺会尝不忘':[200, 150, 180,150,140,163,148,145,126,168,149,153],
    '高峰柠檬鸭':[120, 160, 123,145,125,148,169,142,125,145,165,154],
    '复记老友粉':[130, 120, 160,145,123,156,148,156,142,123,147,154],
    '好有缘':[150, 170, 160,141,145,141,156,124,157,184,142,152],
    '白妈螺蛳粉':[140, 160, 140,145,165,148,169,185,126,142,175,158],
}
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)

# 定义数据框所用的新索引
index = pd.Series([1, 2, 3,4,5], name='序号')

# 通过x指定月份所在这一列为折线图的x轴
st.line_chart(df, x='月份')

st.subheader("🎲今日午餐推荐")

# 餐厅数据
restaurants = [
    {"名称": "复记老友粉", "类型": "快餐"},
    {"名称": "星艺会尝不忘", "类型": "中餐"},
    {"名称": "高峰柠檬鸭", "类型": "中餐"},
    {"名称": "好友缘", "类型": "自助餐"},
    {"名称": "西冷牛排店", "类型": "西餐"}
]

# 按钮
if st.button("帮我选午餐"):
    selected_restaurant = random.choice(restaurants)
    st.success(f"今日推荐: {selected_restaurant['名称']}({selected_restaurant['类型']})")
    st.text('🍛🍙🥟🍧🍦🍹🥛美味午餐等着你！')
