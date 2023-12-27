import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())  # 테스트 케이스의 수

for test_case in range(1, T + 1):
    laser = input()
    piece = 0
    stick_num = []
    for i in range(len(laser)):
        if laser[i] == '(':
            stick_num.append('(')
        else:
            if laser[i-1] == '(':
                stick_num.pop()
                piece += len(stick_num)
            else:
                stick_num.pop()
                piece += 1
    print(f'#{test_case} {piece}')