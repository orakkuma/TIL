# 2차원 array에서 좌표값이 필요할 때 n칸 움직이게 하는 코드

ex) 달팽이 숫자

```python
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리
for tc in range(1, T + 1):
    # 각 테스트 케이스 시작
    N = int(input())

    # 시계방향 
    #     우 하 좌 상
    dr = [0, 1, 0, -1] # delta_row
    dc = [1, 0, -1, 0] # delta_column

    board = [[0] * N for _ in range(N)]
    # = [[0 for _ in range(N)] for _ in range(N)]

    row, col = 0, 0
    num = 1
    idx = 0  # 방향 초기화



    while num <= N ** 2:
        # 숫자를 채워야 한다면
        board[row][col] = num
        num += 1

        # 다음 위치
        n_row = row + dr[idx]
        n_col = col + dc[idx]

        if (n_row < 0 or n_row >= N or n_col < 0 or n_col >= N or board[n_row][n_col] != 0):
            # 턴을 해야 한다면 (idx 0 ~ 3) 계속 반복
            idx = (idx + 1) % 4
            n_row = row + dr[idx]
            n_col = col + dc[idx]

        row = n_row
        col = n_col



    print(f'#{tc}')
    for row in board:
        print(*row)
```

`dr = [0, 1, 0, -2]`

`dc = [1, 0, -1, 0]`

`idx = (idx + 1) % 4` => 여기가 중요

턴을 해야하므로 idx가 0~3을 반복하게 하는 코드