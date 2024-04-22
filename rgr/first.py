from random import randint

INF = 10**18


def run(x: int, y: int, now) -> int:
    global visited
    visited[x][y] = True
    now += mas[x][y]
    if x == n - 1 and y == n - 1:
        return now
    best_res = INF
    if x + 1 < n and not visited[x + 1][y]:
        best_res = min(best_res, run(x + 1, y, now))
    if 0 < x - 1 < n and not visited[x - 1][y]:
        best_res = min(best_res, run(x - 1, y, now))
    if y + 1 < n and not visited[x][y + 1]:
        best_res = min(best_res, run(x, y + 1, now))
    if 0 < y - 1 < n and not visited[x][y - 1]:
        best_res = min(best_res, run(x, y - 1, now))
    visited[x][y] = False
    return best_res


n = 5
mas = [[randint(1, 100) for _ in range(n)] for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

print('\n'.join(str(i) for i in mas))
print('\n'.join(str(i) for i in visited))
print(run(0, 0, 0))
