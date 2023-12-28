def solution(fees, records):
    answer = []
    # fees = [180, 5000, 10, 600], [120, 0, 60, 591], [1, 461, 1, 10]
    # records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"], ["00:00 1234 IN"]
    # result = [14600, 34400, 5000], [0, 591], 	[14841]
    # 주차 요금을 나타내는 정수 배열 fees, 자동차의 입/출차 내역을 나타내는 문자열 배열 records가 매개변수로 주어집니다. 차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return 하도록 solution 함수를 완성해주세요.

    # 1. 입력값 분석 : 문제에서 제시한 주차 시간과 기본 시간, 기본 요금, 단위 시간, 단위 요금을 변수로 설정
    # 2. 주차 시간 계산 : 차량의 주차 시작 및 종료 시간을 받아온다. 주차한 시간을 계산하고, 이를 기본 시간과 비교하여 초과 주차 시간을 구한다.
    # 3. 주차 요금 계산 : 주차한 총 시간을 기준으로 기본 시간과 추과 주차 시간에 대한 요금을 계산한다.
    # 4. 결과 출력 : 최종 주차 요금을 출력.

    basic_time, basic_fee, unit_time, unit_fee = fees

    in_records = {}
    out_records = {}

    for record in records:
        time, car_num, status = record.split()
        if status == 'IN':
            if car_num not in in_records:
                in_records[car_num] = []
            in_records[car_num].append(time)
        else:
            if car_num not in out_records:
                out_records[car_num] = []
            out_records[car_num].append(time)


    parking_time = {}
    for car_num, in_time_list in in_records.items():
        out_time_list = out_records.get(car_num, [])  # 해당 차량의 출차 시간 리스트 가져오기, 없으면 빈 리스트 반환
        total_parking_time = 0

        # 각 입차 시간과 출차 시간을 순회하며 주차 시간 계산
        for i in range(len(in_time_list)):
            in_time = in_time_list[i]
            out_time = out_time_list[i] if i < len(out_time_list) else "23:59"  # 출차 기록이 없으면 23:59로 처리

            # 시간 계산을 위해 시간 문자열을 시각으로 변환
            in_hour, in_minute = map(int, in_time.split(':'))
            out_hour, out_minute = map(int, out_time.split(':'))

            # 주차 시간 계산 (분 단위)
            parking_duration = (out_hour * 60 + out_minute) - (in_hour * 60 + in_minute)
            total_parking_time += parking_duration

        parking_time[car_num] = total_parking_time

    for car_num, time in parking_time.items():
        # 주차한 시간이 기본 시간 이내인 경우
        if time <= basic_time:
            answer.append(basic_fee)
        else:
            # 초과된 시간 계산 후 요금 계산
            exceeding_time = time - basic_time
            extra_fee = (exceeding_time // unit_time) * unit_fee
            if exceeding_time % unit_time != 0:
                extra_fee += unit_fee
            total_fee = basic_fee + extra_fee
            answer.append(total_fee)

    return answer