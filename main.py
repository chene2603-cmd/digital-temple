cat > main.py <<'EOF'
import requests
from config import API_KEY, MODEL

def help_me():
    prompt = "How to fix 'Failed to fetch' in WeChat mini game? Give 3 simple steps."

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
        result = res.json()
        print(result["output"]["choices"][0]["message"]["content"])
    except Exception as e:
        print("Error:", repr(e))
        print("\nQuick fix for Failed to fetch:")
        print("1. Add domain to WeChat public platform whitelist")
        print("2. Use HTTPS, not HTTP")
        print("3. Check network and API availability")

if __name__ == "__main__":
    help_me()
EOF