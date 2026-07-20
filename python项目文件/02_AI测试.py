
#第一部分，引入
import streamlit as st #制作界面
import os #文件操作
from openai import OpenAI #调用AI
import json #数据处理
from datetime import datetime #时间处理


#界面的初始设置
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


#保存会话的函数
def save_session():
    if st.session_state.current_time:
        session_data = {
            "time": st.session_state.current_time,
            "messages": st.session_state.messages,
            "new_name": st.session_state.new_name,
            "new_character": st.session_state.new_character
        }
        #如果目录不存在，则创建
        if not os.path.exists("session"):
            os.makedirs("session")
        #保存会话数据
        with open("session/%s_session_data.json" % st.session_state.current_time, "w", encoding="utf-8") as f:
                json.dump(session_data, f, ensure_ascii=False, indent=2)


#生成文件名的函数
def generate_filename():
    return datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

#加载会话列表信息的函数
def load_session_list():
    # 加载会话列表信息
    session_list = []
    # 遍历session目录下的所有文件
    if os.path.exists("session"):
        for filename in os.listdir("session"):
            if filename.endswith("_session_data.json"):
                session_list.append(filename.replace("_session_data.json", ""))
    return session_list

#加载会话的函数
def load_session(session_name):
    try:
        if os.path.exists("session/%s_session_data.json" % session_name):
            with open("session/%s_session_data.json" % session_name, "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.messages = session_data["messages"]
                st.session_state.new_name = session_data["new_name"]
                st.session_state.new_character = session_data["new_character"]
                st.session_state.current_time = session_name

    except Exception:
        st.error("会话加载失败")
#删除会话的函数
def delete_session(session_name):
    if os.path.exists("session/%s_session_data.json" % session_name):
        os.remove("session/%s_session_data.json" % session_name)

        #如果删除当前对话，更新消息列表
        if session_name == st.session_state.current_time:
            st.session_state.messages = []
            st.session_state.current_time = generate_filename()
    else:
        st.error("会话删除失败")





#初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state.messages = []
#初始化伴侣信息
if 'new_name' not in st.session_state:
    st.session_state.new_name = ""
if 'new_character' not in st.session_state:
    st.session_state.new_character = ""
#初始化时间
if 'current_time' not in st.session_state:
    st.session_state.current_time = generate_filename()




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
    st.write('会话信息')
    if st.button("保存并新建会话", width='stretch',icon="💾"):
        save_session()
        st.write('会话已保存')
        # 新建会话
        if st.session_state.messages:
            st.session_state.messages = []
            st.session_state.new_name = "小玉"
            st.session_state.new_character = "大学生"
            st.session_state.current_time = generate_filename()

            st.rerun()

    #展示会话历史
    st.text("会话历史")
    session_list = load_session_list()
    for session in session_list:
        col1,col2 = st.columns([9,1])
        with col1:
            # 会话名称
            #三元运算符的用法
            if st.button(session, width='stretch', key=session + "_load", icon="📄", type="primary" if session == st.session_state.current_time else "secondary"):
                # 加载会话
                load_session(session)
                st.rerun()
        with col2:
            # 会话删除
            if st.button("", key=session + "_delete", width='stretch',icon = "🗑️"):
                # 删除会话
                delete_session(session)
                st.rerun()






    st.header('伴侣信息')

    # 昵称
    new_name = st.text_input('昵称', placeholder='请输入伴侣的昵称', value=st.session_state.new_name)
    st.session_state.new_name = new_name
    # 人设

    new_character = st.text_area('人设', placeholder='请输入伴侣的人设', value=st.session_state.new_character)
    st.session_state.new_character = new_character






#交互效果
prompt = st.chat_input('请输入你的问题')
#星号可以将列表展开,将列表中的元素逐个传入
if prompt:
    if st.session_state.new_name and st.session_state.new_character:



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
    else:
        st.text('请输入伴侣的昵称和人设')

#模拟
