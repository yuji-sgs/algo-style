"""
ある学校には N 人の生徒がおり、それぞれの生徒には 0 から N−1 までの整数が割り振られています。 
N 人が数学と英語のテストを受けたところ、生徒 i の数学と英語の点数はそれぞれ Ai[点]と Bi[点] でした。
2 つのデータ
A=(A0,A1,…,AN−1)
B=(B0,B1,…,BN−1)
について、それぞれの平均が近いとデータの関連性が高いと仮定して、データの関連度を求めてください。
具体的には、A,B の平均をそれぞれAˉ,Bˉとおいたときのmax(Aˉ,Bˉ) / min(Aˉ,Bˉ)の値を求めてください。
"""

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 平均値
mean_A = sum(A) / N
mean_B = sum(B) / N

# データ間の関係性
ans = min(mean_A, mean_B) / max(mean_A, mean_B)

print(ans)
