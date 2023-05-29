"""
N 人の生徒それぞれの好きな色をリストアップしたものが与えられます。
色を表す文字列 T が与えられるので、色 T が好きな生徒の人数を答えてください。
"""

N, T = input().split()
N = int(N)

cnt = 0

for _ in range(N):
    student_like_color = list(input().split())
    for i in range(len(student_like_color)):
        if T == student_like_color[i]:
            cnt += 1

print(cnt)
