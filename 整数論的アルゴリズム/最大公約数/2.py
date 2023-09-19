"""
縦の長さが A、横の長さが B であるような長方形の紙があります。
この紙を、なるべくあまりが出ないように、同じ大きさの正方形に切り分けようとしています。
切り分けられた正方形の一辺の長さとして考えられる最大値を求めてください。
"""

def gcd(A, B):
    if B == 0:
        return A
    else:
        return gcd(B, A%B)

A, B = map(int, input().split())
print(gcd(A, B))
