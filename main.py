cat > main.py <<'EOF'
import requests
import sys
# 强制编码 UTF-8
sys.stdout.reconfigure(encoding='utf-8')

from config import API_KEY, MODEL

def help_me():
    prompt = "微信小游戏Failed to fetch怎么解决，给3条简单步骤"

    url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"
    headers = {
        "Authorization": "Bearer " + API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL,
        "input": {
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    }

    try:
        res = requests.post(url, json=data, headers=headers)
        res.raise_for_status()
        j = res.json()
        print(j["output"]["choices"][0]["message"]["content"])
    except Exception as e:
        print("出错:", str(e))
        print("\n解决Failed to fetch：")
        print("1. 去微信公众平台加域名白名单")
        print("2. 接口必须用https，不能用http")
        print("3. 检查网络能不能访问接口")

if __name__ == "__main__":
    help_me()
EOF
