"""
英小文字からなる文字列 S (長い) と T (短い) が与えられます。
文字列 S の中に、文字列 T が含まれるかどうかを判定してください。
"""

S = input()
T = input() 

# S, T の長さを取得する
N = len(S)
M = len(T)

# 線形探索 (0 から N-M まで) 
flag = False 
for i in range(N-M+1): 
    if S[i:i+M] == T:  
        flag = True 

# 答えを出力する
if flag: print("Yes")
else: print("No") 
