cat > main.py <<'EOF'
def fix_failed_to_fetch():
    print("=== 微信小游戏 Failed to fetch 专业解决方案 ===")
    print("")
    print("1. 登录微信公众平台 → 开发管理 → 开发设置")
    print("2. 把你的接口域名加到【服务器域名】白名单")
    print("3. 接口必须用 https，不能用 http")
    print("4. 检查手机网络是否能访问该接口")
    print("5. 在微信开发者工具里点 Network 看具体报错")
    print("")
    print("只要做前3步，90% 的问题直接解决。")

if __name__ == "__main__":
    fix_failed_to_fetch()
EOF