import sys
#이 파일의 입력(input())을 파일로 대체
sys.stdin = open('./input.txt')
## 위의 두 줄은 제출할 때는 뺴고 제출


T = int(input())

for tc in range(1, T+1):

    # 각 테스트 케이스 시작
    N, M = map(int, input().split())
    # board = []
    # for _ in range(N):
    #     line = (list(map(int, input().split())))
    #     board.append(line)
    # =
    board = [list(map(int, input().split())) for _ in range(N)]
    print(board)
    maximum = 0
    n = N-M+1

    for row in range(n):
        for col in range(n):
            sum_num = 0
            for i in range(M):
                for j in range(M):
                    sum_num += board[row + i][col + j]

            maximum = max(maximum, sum_num)



    print(f'#{tc} {maximum}')