"""
N 個の整数 A0,A1,…,AN−1が与えられます。
これらの整数の中から重複しないように 2 つ選んで積をとります。 
2 つの整数の選び方は  NC2通りありますので、それぞれに対応した積が得られます。
これらNC2個の積の総和を求めてください。
"""

N = int(input())
A = list(map(int,input().split()))
B = sum(A)
ans = B**2
for i in A:
    ans -= i**2
ans //= 2
print(ans)
