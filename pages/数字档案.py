import streamlit as st  # 导入streamlit并用st代替
import pandas as pd   # 导入Pandas并用pd代替

st.title("🕶️学生 KQ-数字档案") # 创建一个标题
st.header("🔑基础信息") # 创建一个章节
st.text("学生ID：23051170127") # 创建一个文本
st.markdown("注册时间："':green[2023-09-09 10:30:24]'" |精神状态：✅正常")# 绿色文本
st.markdown("当前教室："':green[6号实验实训楼301室]'" |安全等级："':green[绝密]')

st.header("📊学习情况") # 创建一个章节
c1, c2, c3 = st.columns(3) # 定义列布局，分成3列
c1.metric(label="数据挖掘与数据分析",help='有一点小退步', value="78%",delta="-10%")
c2.metric(label="深度学习技术", value="88%",delta="1%")
c3.metric(label="云计算与大数据",help='接近瓶颈', value="98%",delta="2%")

st.subheader("Streamlit课程进度")  # 显示进度条
st.progress(value=33,text="Streamlit课程进度")

st.header("📝任务日志") # 创建一个章节
# 定义数据,以便创建数据框
data = {
    '日期':['2025-05-28','2025-05-31','2025-06-03'],
    '任务':['学生数字档案','课程管理系统','数据图表展示'],
    '状态':['✔️完成','🕒进行中','❌未完成'],
    '难度':['⭐⭐⛤⛤⛤','⭐⛤⛤⛤⛤','⭐⭐⭐⛤⛤']
}
# 定义数据框所用的索引
index = pd.Series([0,1,2])
# 根据上面创建的data和index，创建数据框
df = pd.DataFrame(data, index=index)
st.table(df)

st.subheader("🔐最新代码成果") # 创建一个子章节
# 创建要显示的Java代码块的内容
python_code = '''def klws():
    while True：
        if detect_vulnerability():
            exploit()
            return "ACCESS GRANTED"
        else:
            stealth_evade()
'''
st.code(python_code,line_numbers=True)  # 设置line_numbers为True，即该代码块有行号

st.markdown('***')  # 分割线
st.markdown(':green[>>SYSTEM MESSAGE:] ''下一个任务目标已解锁…') # 绿色文本
st.markdown(':green[>>TARGERT:] ''课程管理系统')
st.markdown(':green[>>COUNTDOWN:] ''2025-06-02 13:14:52')
st.markdown('系统状态：在线   连续状态：已加密')