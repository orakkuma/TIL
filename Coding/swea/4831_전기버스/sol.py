import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    # 각 테스트 케이스 시작
    K, N, M = (map(int, input().split()))
    # K = 한번 충전으로 최대한 이동할 수 있는 정류장 수
    # N = 정류장 넘버
    # M = 충전기가 설치된 M개의 정류장 번호

    # board = []
    # for _ in range(N):
    #     line = (list(map(int, input().split())))
    #     board.append(line)
    # =
    board = list(map(int, input().split()))
    current_position = 0  # 현재 위치

    board.append(N)  # 종점도 충전소 목록에 추가

    print(board)

    remaining_battery = K
    count = 0
    can_reach = True

    for station in board:
        if station - current_position > K:  # 이동할 수 없는 거리일 때
            can_reach = False
            break

        if station > current_position + remaining_battery:  # 충전해야 할 때
            remaining_battery = K
            count += 1

        remaining_battery -= station - current_position
        current_position = station

    if can_reach:
        print(f"#{tc} {count}")
    else:
        print(f"#{tc} 0")