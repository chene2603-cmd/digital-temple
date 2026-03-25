# main.py
import os
import requests
from config import MODEL, PROMPT_TEMPLATE

# 这里用通义千问做示例，也可以换成其他模型
def search_web(query: str):
    """极简网页搜索（用 SerpAPI/百度/必应接口，这里先模拟，你可以换成真实 API）"""
    # 这里先模拟搜索结果，实际部署时换成真实搜索 API
    return f"模拟搜索结果：关于{query}的微信小游戏解决方案..."

def mini_game_helper(query: str):
    search_results = search_web(query)
    prompt = PROMPT_TEMPLATE.format(search_results=search_results, user_query=query)
    
    # 调用通义千问 API（需要你在 config.py 里配置 API Key）
    api_key = os.getenv("DASHSCOPE_API_KEY")
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {
        "model": MODEL,
        "input": {"messages": [{"role": "user", "content": prompt}]}
    }
    resp = requests.post("https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation",
                         headers=headers, json=data)
    return resp.json()["output"]["choices"][0]["message"]["content"]

if __name__ == "__main__":
    print(mini_game_helper("微信小游戏Failed to fetch怎么解决？"))
