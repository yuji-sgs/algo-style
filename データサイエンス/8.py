"""
N 人がテストを受けたところ、それぞれの点数は A0,A1,…,AN−1点でした。 
あなたはこのデータを扱いやすくするために、平均点が 0 点となるように補正をかけることにしました。 
具体的には、全員の点数が補正をかける前の平均点  
Aˉだけ低くなるように補正をかけます。
補正をかけたあとの N 人の点数を求めるプログラムを作成してください。
"""

N = int(input())
A = list(map(int, input().split()))
mean = sum(A) / N  # 平均
B = [] * N

for i in range(N):
    B.append(A[i] - mean)

print(*B)
