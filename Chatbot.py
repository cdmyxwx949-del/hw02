#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install python-dotenv')


# In[6]:


from dotenv import load_dotenv
import os
load_dotenv()
print("API Key:", os.getenv("DASHSCOPE_API_KEY")[:10] + "...")  # 只打印前10位


# In[8]:


import os
import requests
import json

# 🔒 从环境变量读取 API Key（脱敏核心）
API_KEY = os.getenv("DASHSCOPE_API_KEY")
if not API_KEY:
    raise ValueError("❌ 请设置环境变量 DASHSCOPE_API_KEY（参考 README.md）")

ENDPOINT = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"
MODEL_NAME = "qwen-plus"

def chat_with_qwen(user_input):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL_NAME,
        "input": {
            "messages": [
                {"role": "user", "content": user_input}
            ]
        },
        "parameters": {
            "result_format": "message" 
        }
    }

    try:
        response = requests.post(ENDPOINT, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  
        result = response.json()

        if "output" in result and "choices" in result["output"]:
            assistant_message = result["output"]["choices"][0]["message"]["content"]
            return assistant_message
        else:
            return "❌ 未收到有效回复，请检查 API 响应结构。"

    except Exception as e:
        return f"❌ 请求失败：{str(e)}"

if __name__ == "__main__":
    print(" 欢迎使用 Chatbot！输入 'quit' 退出。\n")
    while True:
        user_input = input(" 你：").strip()
        if user_input.lower() in ["quit", "exit", "q"]:
            print("再见！")
            break
        if not user_input:
            continue
        print("思考...")
        reply = chat_with_qwen(user_input)
        print(f"千问：{reply}\n")


# In[ ]:




