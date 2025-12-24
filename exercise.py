# 운동을 해야하는 이유를 담을 곳

exercise_reason = []

# 사용자가 원하는 행동
user_input = input("(목록)/(추가)/(삭제)/(수정)")

#목록을 원한다면


if user_input == "목록":
    print("현재 들어있는 조언 목록들입니다.")
    print(exercise_reason) 