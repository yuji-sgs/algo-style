"""
アルルの通う学校には N 人の生徒がいます。 それぞれの生徒には 0 から N−1 までの番号が割り振られています。
ある日 N 人が一斉に数学と英語のテストを受けたところ、順位表は次のようになりました。 順位は 2 教科の合計点が高い順に並んでおり、合計点が同じ場合はランダムに並んでいます。
アルルは数学の順位が気になったため、この表を次のように並び替えることにしました。
数学の点数が高い人が順位表の上に来るように並び替える。 ただし、数学の点数が同じ人同士の場合は合計点の低い人が上に来るようにする。 また、数学の点数も合計点も同じ人同士の場合はもとの順序関係を保つようにする。
順位表を並び替えた結果を出力してください。
"""

N = int(input())
S = [input().split() for i in range(N)]
S = [(s[0], int(s[1]), int(s[2])) for s in S]
 
S.sort(key=lambda s: (-s[1], s[1]+s[2]))

for s in S:
    print("{} {} {}".format(s[0], s[1], s[2]))
