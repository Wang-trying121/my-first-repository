import streamlit as st
import random


# ---------- 页面配置 ----------

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


st.title("这是一个测试！")
st.write('乱七八糟什么都有')
st.image("./资源/图片1.png",width = 300)
st.image("./资源/图片2.png",width = 300)
st.video("./资源/01.mp4",width = 400)
st.audio("./资源/菊谷知樹 - ガンガン結束バンド.flac")
st.logo("./资源/Logo.png",size = "large")
ta = {
    "这是":["一个",'表格','哇'],
    '一个':["表格","哇",'这是'],
    '表格':["哇",'这是','一个']
}
st.table(ta)
comment = st.text_input("请评价这个网站")
st.write(f"你的评价是{comment}")
choice = st.radio("关键选择,你的MBTI第一个字母是什么：",['E','I'])
st.write(f"原来你是{choice}人！")
num = random.randint(456,98435)
st.write(f'已有{num}朵鲜花送给你！')