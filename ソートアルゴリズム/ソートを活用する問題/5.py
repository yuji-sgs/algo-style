"""
カメのアルルはごはんを買いにお店にきました。 お店には 0 から N−1 までの番号が振られた N 種類のごはんが売られています。 ごはん i の価格はAi円で、在庫がBi個あります。
アルルが合計で K 個のごはんを買うには最低何円払う必要がありますか。
"""

N, K = map(int, input().split())

food_list = []
for i in range(N):
    A, B = map(int, input().split())
    food_list.append((A, B))

food_list.sort(key=lambda x: x[0]) # 価格の安い順にソート
total_cost = 0

for price, stock in food_list:
    buy_amount = min(stock, K)
    total_cost += price * buy_amount
    K -= buy_amount
    if K == 0:
        break

print(total_cost)
