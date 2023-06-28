"""
エディタにあらかじめ用意されている定数 LONG_SENTENCE は、英単語からなる長い文章です。
この文章は単語ごとに ' ' (空白) で区切られています。
それでは、この文章はいくつの単語から成り立っているか答えてください。
"""

# 長い文章
LONG_SENTENCE = "Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua Ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur Excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum"

# ここからコードを書いてください
cnt = 0

for char in LONG_SENTENCE:
    if char == " ":
        cnt += 1

print(cnt+1)
