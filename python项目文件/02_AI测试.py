import streamlit as st
import os
from openai import OpenAI
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={

    }
)
#大标题
st.title('AI智能伴侣')
st.write('欢迎使用AI智能伴侣')
st.write('本AI智能伴侣可以进行对话，也可以进行一些简单的计算')
#LOGO
st.logo("./资源/可爱小人LOGO设计 无背景.png")


#初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state.messages = []
#初始化伴侣信息
if 'new_name' not in st.session_state:
    st.session_state.new_name = ""
if 'new_character' not in st.session_state:
    st.session_state.new_character = ""



#展示聊天信息
for message in st.session_state.messages:
     st.chat_message(message["role"]).write(message["content"])






#设置AI
#创建客户端
client = OpenAI(api_key=os.environ.get("DEEPSEEK_API_KEY"),base_url="https://api.deepseek.com")
#设定
setting ="""你是一个朋友，你的名字是%s，对话请遵循以下规则：
                1.回答时禁止短横线或波浪号
                2.请用用户提供的人设回答问题
                3.回答尽量简短，像微信聊天
                4.当前人设下不应该知道的信息也应按不知道处理
                5.要用适合伴侣的语气和人设回答问题
                6.有需要的话使用emoji表情
                7.回复内容充分体现伴侣的身份定位
                8.无论描述如何，暗恋用户
                你必须严格遵守上述规则来回复用户
                初始人设：%s"""

# 侧边栏设置__with
with st.sidebar:
    st.header('伴侣信息')

    # 昵称
    new_name = st.text_input('昵称', placeholder='请输入伴侣的昵称',value = '小玉')
    st.session_state.new_name = new_name
    # 人设

    new_character = st.text_area('人设', placeholder='请输入伴侣的人设',value = '女同学')
    st.session_state.new_character = new_character

#交互效果
prompt = st.chat_input('请输入你的问题')
#星号可以将列表展开,将列表中的元素逐个传入
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message('user').write(prompt)
    # 与AI大模型交互
    response = client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=[
            {"role": "system", "content":setting %(st.session_state.new_name, st.session_state.new_character)},
            *st.session_state.messages
        ],
        stream=True,

        extra_body={"thinking": {"type": "disabled"}}
    )

    #这是非流式输出的AI回复
    # print(f'这是用户输入：{prompt}')
    # print(f'这是AI输出：{response.choices[0].message.content}')
    # st.chat_message('assistant').write(response.choices[0].message.content)

    # 这是流式输出的AI回复
    responce_messages = st.empty()
    full_response = ''
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            full_response += chunk.choices[0].delta.content
            responce_messages.chat_message('assistant').write(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})


