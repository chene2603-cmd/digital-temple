# main.py
import os
import requests
from config import MODEL, PROMPT_TEMPLATE, API_KEY

def mini_game_helper(query: str):
    """微信小游戏提审助手"""
    # 模拟搜索结果（后面可以换成真实搜索 API）
    search_results = f"关于「{query}」的微信小游戏常见解决方案："
    search_results += "\n1. 检查域名是否在微信公众平台白名单"
    search_results += "\n2. 确认接口使用 HTTPS 协议"
    search_results += "\n3. 查看开发者工具 Network 面板定位具体错误"
    search_results += "\n4. 检查本地网络是否能正常访问接口"

    # 拼接提示词
    prompt = PROMPT_TEMPLATE.format(
        search_results=search_results,
        user_query=query
    )

    # 调用通义千问 API
    url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL,
        "input": {
            "messages": [{"role": "user", "content": prompt}]
        },
        "parameters": {"temperature": 0.3}
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result["output"]["choices"][0]["message"]["content"]
    except Exception as e:
        return f"调用大模型失败：{str(e)}\n\n先按搜索结果手动排查：\n{search_results}"

if __name__ == "__main__":
    # 你可以把问题换成自己遇到的真实报错
    question = "微信小游戏提示 Failed to fetch 怎么解决？"
    print("🤖 慧凌AI 小游戏助手正在处理...")
    print(mini_game_helper(question))
