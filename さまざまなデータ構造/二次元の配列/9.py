"""
N 人が SNS を使用しています。各ユーザーは 0,1,…,N−1 と番号付けられています。
どのユーザーも誰もフォローしていない状態から開始して、Q 回のクエリが与えられました。 それぞれのクエリに答えてください。 各クエリは、次のいずれかです。
・　Follow(x,y)：ユーザー x がユーザー y をフォローします。このとき、ユーザー y がユーザー x をフォローするとは限りません。また、もともとフォローしている場合は何もしません
・　GetFollowers(z)：ユーザー z をフォローしているユーザーの番号を小さい順にすべて出力してください。ただしユーザー z が誰にもフォローされていない場合は "No" と出力してください
"""
N, Q = map(int, input().split())

# 各ユーザーがフォローしているユーザーを格納するリストを初期化
following = [[] for _ in range(N)]

for _ in range(Q):
    query = list(map(int, input().split()))
    
    if query[0] == 0: 
        x, y = query[1], query[2]
        # ユーザー x がユーザー y をフォロー
        if y not in following[x]:
            following[x].append(y)
            
    elif query[0] == 1:  
        z = query[1]
        followers = []

        # 各ユーザーが z をフォローしているかどうかを確認し、フォロワーリストに追加
        for i in range(N):
            if z in following[i]:
                followers.append(i)

        # 結果を出力
        if followers:
            print(" ".join(map(str, followers)))
        else:
            print("No")

