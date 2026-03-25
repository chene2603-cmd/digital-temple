# config.py
import os
os.environ["DASHSCOPE_API_KEY"] = "你的通义千问API Key"  # 替换成你的真实 Key

MODEL = "qwen-max"
PROMPT_TEMPLATE = """
你是微信小游戏提审专家，只回答和微信小游戏审核、广告接入、报错相关的问题。
请根据以下搜索结果，用简洁的中文给出解决方案，不要无关信息：
{search_results}

用户问题：{user_query}
"""