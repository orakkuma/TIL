# def solution(array, commands):
#     answer = []
#
#     i = commands[0]
#     j = commands[1]
#     k = commands[2]
#
#     s_array = array[int(i)-1:int(j)-1]
#
#     s_array.sort()
#
#     answer = s_array[k-1]
#
#     return answer
#
# print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
# # [5, 6, 3]


# def solution(array, commands):
#     answer = []
#
#     for command in commands:
#         i, j, k = command  # 각각의 명령을 i, j, k로 할당
#
#         s_array = array[i - 1 : j]  # 인덱스 범위로 슬라이싱
#
#         s_array.sort()  # 부분 배열 정렬
#
#         answer.append(s_array[k - 1])  # k번째 숫자를 answer에 추가
#
#     return answer
#
# print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
# # [5, 6, 3]


def solution(array, commands):
    answer = []

    for i, j, k in commands:
        part = (array[i-1:j])
        part.sort()

        answer.append(part[k-1])
    return answer
print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))