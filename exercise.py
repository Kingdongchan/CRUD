# 운동을 해야하는 이유를 담을 곳

exercise_reason = []

# 사용자가 원하는 행동
user_input = input("(목록)/(추가)/(삭제)/(수정):")

#목록 선택
if user_input == "목록":
    print("--현재 들어있는 조언 게시물 목록들 입니다.--")
    print(exercise_reason) 

# 추가 선택
elif user_input == "추가":
    user_input_reason= input("내용: ")
    user_input_name = input("작성자: ")
    #입력한 것들을 목록에 넣기
    def add_reason(user_input_reason, user_input_name):
        list_reason = {"번호":len(exercise_reason)+ 1, "조언": user_input_reason, "작성자":user_input_name}
        
        exercise_reason.append(list_reason)
        print("---등록 완료---")

# 삭제 선택
elif user_input == "삭제":
        reason_number = len(exercise_reason)+1
        #목록 불러오기
        for j in range(len(exercise_reason)):
            print(f"-{reason_number}.", exercise_reason)
        
        user_choose_number = int(input("삭제할 게시물의 번호: "))
        
        # 목록에 있는 것들 나열하기
        for i in range(len(exercise_reason)):
             exercise_number = exercise_reason[i]
            # 목록에 잇는 것들 나열 후 사용자의 입력과 맞는지 비교 후 삭제하기
             if user_choose_number == exercise_number:
                  del exercise_number[i]

                  print(f"{user_choose_number}번 삭제 완료")

# 수정 선택
elif user_input == "수정":
    reason_number = len(exercise_reason)+1
        #목록 불러오기
    for j in range(len(exercise_reason)):
        print(f"-{reason_number}.", exercise_reason)
        
    user_choose_number = int(input("수정할 게시물의 번호: "))
    #운동 조언 목록 가져오기
    for i in range(len(exercise_reason)):
         exercise_number = exercise_reason[i]
        # 유저가 고른 번호와 맞는지 확인
         if user_choose_number == exercise_number:
              #수정
              user_repost = input("수정 할 내용: ")
              exercise_reason[i]["조언"] = user_repost
