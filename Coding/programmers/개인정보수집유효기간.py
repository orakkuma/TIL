    # 모든 달은 28일까지
    # today = 'yyyy.mm.dd'
    # 유효기간 = terms = 'char number'
    # privacies = 'yyyy.mm.dd char'
    
def solution(today, terms, privacies):
    answer = []

    today_year, today_month, today_day = map(int, today.split('.'))

    # 각 약관 별 유효기간 계산
    valid_period = {}
    for term in terms:
        term_char, term_period = term.split()
        valid_period[term_char] = int(term_period)

    # 개인정보 확인 및 처리
    for idx, info in enumerate(privacies):
        date, info_char = info.split()
        year, month, day = map(int, date.split('.'))

        # 유효기간 계산
        valid_year = year + (month + valid_period[info_char] - 1) // 12
        valid_month = (month + valid_period[info_char] - 1) % 12 + 1
        valid_day = min(day, 28)  # 모든 달은 28일까지 있다고 가정

        # 오늘 날짜와 유효기간을 비교하여 해당되면 answer에 추가
        if (today_year, today_month, today_day) >= (valid_year, valid_month, valid_day):
            answer.append(idx + 1)  # 번호는 1부터 시작하므로 +1 해줌

    return answer

# solution 함수 실행
result = solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
print("파기해야 할 개인정보 번호:", result)
