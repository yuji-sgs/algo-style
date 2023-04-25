# データを受け取る
N, V = map(int, input().split())
A = list(map(int, input().split())) 

# 線形探索
pos = -1
for i in range(N): 
    if A[i] == V:  
        pos = i

# 答えを出力する
print(pos) 
