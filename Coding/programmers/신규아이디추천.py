def solution(new_id):
    answer = ''

    step1 = ''
    for upperchar in new_id:
        if upperchar.isupper():
            step1 += upperchar.lower()
        else:
            step1 += upperchar

    step2 = ''
    excepted_char = '-_.'
    for specialchar in step1:
        if specialchar.isalnum() or specialchar in excepted_char:
            step2 += specialchar
        else:
            step2 += ''

    step3 = ''
    prev_char = False
    for commas in step2:
        if commas == '.':
            if not prev_char:
                step3 += commas
                prev_char = True
        else:
            step3 += commas
            prev_char = False

    list_step3 = list(step3)
    for first_comma in list_step3:
        if list_step3[0] == '.':
            list_step3.pop(0)
        elif list_step3[-1] == '.':
            list_step3.pop(-1)
        else:
            list_step3 = list_step3
    step4 = ''.join(list_step3)

    # step5
    if step4 == '':
        step4 = 'a'
    else:
        step4 = step4

    step6 = step4[:15]

    # step7
    if len(step6) <= 2:
        while len(step6) < 3:
            step6 += step6[-1]
    else:
        step6 = step6

    final_step_list = list(step6)
    for last_comma in final_step_list:
        if final_step_list[0] == '.':
            final_step_list.pop(0)
        elif final_step_list[-1] == '.':
            final_step_list.pop(-1)
        else:
            final_step_list = final_step_list
    final_step = ''.join(final_step_list)

    answer = final_step




    return answer


# 다른 사람이 짠 코드 참고
# def solution(new_id):
#     answer = ''
#     # 1
#     new_id = new_id.lower()
#     # 2
#     for c in new_id:
#         if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
#             answer += c
#     # 3
#     while '..' in answer:
#         answer = answer.replace('..', '.')
#     # 4
#     if answer[0] == '.':
#         answer = answer[1:] if len(answer) > 1 else '.'
#     if answer[-1] == '.':
#         answer = answer[:-1]
#     # 5
#     if answer == '':
#         answer = 'a'
#     # 6
#     if len(answer) > 15:
#         answer = answer[:15]
#         if answer[-1] == '.':
#             answer = answer[:-1]
#     # 7
#     while len(answer) < 3:
#         answer += answer[-1]
#     return answer