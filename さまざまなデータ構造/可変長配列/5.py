"""
1 から N までの整数を右回りに円状に並べて、 1 から始めて右回りに、1 つおきに取り除いていきます
最後に残る整数を答えてください。
たとえば N=12 の場合、取り除かれるカードは1,3,5,7,9,11,2,6,10,4,12となって、最後に 8 が残ります。
"""

from collections import deque

def mamakodate(N):
    numbers = deque(range(1, N + 1))
    while len(numbers) > 1:
        numbers.popleft()
        numbers.rotate(-1)

    return numbers[0]

N = int(input())
result = mamakodate(N)
print(result)
