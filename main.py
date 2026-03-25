# main.py
from autorde import AutoResearch
from config import MODEL, SEARCH_ENGINES, PROMPT_TEMPLATE

def mini_game_helper(query: str):
    ar = AutoResearch(model=MODEL, search_engines=SEARCH_ENGINES)
    results = ar.search(query, max_results=5)
    return ar.summarize(results, prompt_template=PROMPT_TEMPLATE)

if __name__ == "__main__":
    print(mini_game_helper("微信小游戏提示Failed to fetch怎么解决？"))