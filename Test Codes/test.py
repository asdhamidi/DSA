def count_luck(arr, x, y, turns, visited):
    visited[x][y] = True
    increments = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    next_points = []

    for inc_x, inc_y in increments:
        if valid(x + inc_x, y + inc_y, len(arr[0]), len(arr), visited):
            next_points.append([x + inc_x, y + inc_y])
    
    if len(next_points) == 0:
        return None
    elif len(next_points) > 1:
        for newx, newy in next_points:
            if arr[newx][newy] == "*":
                return turns
            res = count_luck(arr, newx, newy, turns+1, visited)
            if not res:
                continue
    else:
        if arr[next_points[0][0]][next_points[0][1]] == "*":
            return turns
        res = count_luck(arr, next_points[0][0], next_points[0][1], turns, visited)
        if not res:
            return res
    
def valid(x, y, m, n, visited):
    return 0 <= x < n and 0 <= y < m and arr[x][y] != "X" and not visited[x][y]

if __name__ == "__main__":
    for _ in range(int(input())):
        m, n = map(int, input().split())
        start = None
        arr = []
        for r in range(m):
            new_row = list(input())
            arr.append(new_row)
            if start is None:
                for i in range(len(new_row)):
                    if new_row[i] == "M":
                        start = [r, i]
        guess = int(input())
        ans = count_luck(arr, start[0], start[1], 0, visited=[[False] * n for r in range(m)])
        if ans == guess:
            print("Impressed")
        else:
            print("Oops!")

