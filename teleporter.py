N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))

visited = [-1] * (N+1)
visited[1] = 0

move_cnt = 0
now_city = 1

for i in range(10**6):
    move_cnt += 1
    moved_city = A[now_city]

    if move_cnt == K:
        print(moved_city)
        exit()

    if visited[moved_city] == -1:
        visited[moved_city] = move_cnt
        now_city = moved_city
    else:
        cycle = move_cnt - visited[moved_city]
        break

K -= visited[moved_city]

dest = K % cycle

for i in range(dest):
    moved_city = A[moved_city]

print(moved_city)


