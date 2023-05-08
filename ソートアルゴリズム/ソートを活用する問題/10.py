"""
アルルの通う学校には N 人の生徒がいます。 それぞれの生徒には 0 から N−1 までの番号が割り振られています。
ある日、N 人の中から学校の生徒会長を決めることになり、各々の生徒は自分を含む生徒のうち 1 人に投票することになりました。 その結果、生徒 i は生徒 Aiに投票しました。
投票結果を集計し、生徒の番号を投票人数が多い順に出力してください。 ただし、投票人数が等しい生徒については番号が小さい順に出力してください。
"""

N = int(input())
A = list(map(int, input().split()))

# Aiが獲得した投票結果を配列として作成
Voting_Result = [0] * N
for i in range(N):
    Voting_Result[A[i]] += 1

Voting_Count = [(i, Vote) for i, Vote in enumerate(Voting_Result)]
Voting_Count.sort(key=lambda x:x[1], reverse = True)

for item in Voting_Count:
    print("{} {}".format(item[0], item[1]))
