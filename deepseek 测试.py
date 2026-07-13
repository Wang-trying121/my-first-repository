import os
from openai import OpenAI
#创建客户端
client = OpenAI(api_key=os.environ.get("DEEPSEEK_API_KEY"),base_url="https://api.deepseek.com")
#与AI大模型交互
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "你是一名AI助手，你的名字是小玉，请用温柔可爱的语气回答用户的问题"},
        {"role": "user", "content": "世界杯八强是谁？"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "disabled"}}
)

#回答问题
print(response.choices[0].message.content)
#AI的提示词工程
'''1.给大模型设定角色和能力
   2.明确核心请求与任务
   3.按步骤拆解复杂任务
   4.指定风格和语气
   5.明确要求输出格式
   6.提供可供参考的样例'''