import streamlit as st
import os
from openai import OpenAI
st.set_page_config(
    page_title="AI智能伴侣小玉",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={

    }
)
#大标题
st.title('AI智能伴侣小玉')
st.write('欢迎使用AI智能伴侣小玉')
st.write('本AI智能伴侣小玉可以进行对话，也可以进行一些简单的计算')
#LOGO
st.logo("./资源/可爱小人LOGO设计 无背景.png")
#初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state.messages = []
#展示聊天信息
for message in st.session_state.messages:
     st.chat_message(message["role"]).write(message["content"])
#设置AI
#创建客户端
client = OpenAI(api_key=os.environ.get("DEEPSEEK_API_KEY"),base_url="https://api.deepseek.com")
#设定
setting = "你是一名AI助手，你的名字是小玉，请用温柔可爱的语气回答用户的问题,语言要生动活泼，结尾有语气词,回答时禁止短横线或波浪号。"
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
            {"role": "system", "content":setting},
            *st.session_state.messages
        ],
        stream=True,

        extra_body={"thinking": {"type": "disabled"}}
    )

    #这是非流式输出的AI回复
    # print(f'这是用户输入：{prompt}')
    # print(f'这是AI输出：{response.choices[0].message.content}')
    # st.chat_message('assistant').write(response.choices[0].message.content)
    #这是流式输出的AI回复
    # ... existing code ...
    # 这是流式输出的AI回复
    responce_messages = st.empty()
    full_response = ''
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            full_response += chunk.choices[0].delta.content
            responce_messages.chat_message('assistant').write(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})

#这是一次修改
#这是二次修改
#这是三次修改
#这是四次修改
#这是第五次修改
#这是第六次修
#这是第七次修改
