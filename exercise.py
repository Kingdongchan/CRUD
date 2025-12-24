# 운동을 해야하는 이유를 담을 곳

exercise_reason = []

# 사용자가 원하는 행동
user_input = input("(목록)/(추가)/(삭제)/(수정):")

#목록 선택
if user_input == "목록":
    print("--현재 들어있는 조언 목록들입니다.--")
    print(exercise_reason) 

# 추가 선택
elif user_input == "추가":
    user_input_reason= input("내용: ")
    user_input_name = input("작성자: ")
    
    def add_reason(user_input_reason, user_input_name):
        list_reason = {"번호":len(exercise_reason)+ 1, "조언": user_input_reason, "작성자":user_input_name}
        
        exercise_reason.append(list_reason)
        print("---등록 완료---")