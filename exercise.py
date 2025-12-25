# 운동을 해야하는 이유를 담을 곳

exercise_reason = []

print("---운동 조언 게시판---")
# 사용자가 원하는 행동

end_ = "종료"
list_ = "목록"
add_ = "추가"
del_ = "삭제"
modify_ = "수정"
num_ = "번호"
advice_ = "조언"
writer_ = "작성자"
password_ = "비밀번호"

#계속 작동할 수 있도록 추가
while True:
    user_input = input(f"({list_})/({add_})/({del_})/({modify_})/({end_}):")

    #종료 선택
    if user_input == end_:
        print(f"프로그램을 {end_}합니다.")
        break

    #목록 선택
    elif user_input == list_:
        print(f"--현재 들어있는 {advice_} 게시물 {list_}들 입니다.--")
        for z in exercise_reason:
            print(f"{z[num_]}. {z[advice_]} - {z[writer_]}") 
        #목록 나열하기
    # 추가 선택
    elif user_input == add_:
        user_input_reason = input("내용: ")
        user_input_name = input(f"{writer_}: ")
        user_password = input(f"{password_}를 입력하세요: ")
        #입력한 것들을 목록에 넣기
        def add_reason(user_input_reason, user_input_name, user_password):
            list_reason = {num_:len(exercise_reason)+ 1, advice_: user_input_reason, writer_:user_input_name, password_:user_password}
            
            exercise_reason.append(list_reason)
            print("---등록 완료---")
        # 추가 실행 위치 설정 
        add_reason(user_input_reason, user_input_name, user_password)
        

    # 수정 선택
    elif user_input == modify_:
        reason_number = len(exercise_reason)+1
            #목록 불러오기
        for j in exercise_reason:
            print(f"-{j[num_]}. {j[advice_]}")
        
        user_choose_number = int(input(f"{modify_}할 게시물의 {num_}: "))
        #운동 조언 목록 가져오기
        for i in range(len(exercise_reason)):
            exercise_number = exercise_reason[i]

            if user_choose_number == exercise_number[num_]:
                #수정
                user_repost = input(f"{modify_} 할 내용: ")
                exercise_reason[i][advice_] = user_repost
                
                print(f"{modify_} 완료 했습니다.")
    
    # 삭제 선택
    elif user_input == del_:
            reason_number = len(exercise_reason)+1
            #목록 불러오기
            
            for j in exercise_reason:
                print(f"-{j[num_]}. {j[advice_]}")
            
            user_choose_number = int(input(f"{del_}할 게시물의 {num_}: "))
            #패스워드 판단
                # 목록에 있는 것들 나열하기
            for i in range(len(exercise_reason)):
                exercise_number = exercise_reason[i]
                exercise_password = exercise_reason[i][password_]
                
                if user_choose_number == exercise_number[num_]:
                    
                    while True:
                        password_input = input(f"{del_}를 원한다면 {password_}를 입력하세요: ")

                        if password_input == end_:
                            print(f"{end_}하겠습니다.")
                            break
                        
                        # 목록에 잇는 것들 나열 후 사용자의 입력과 맞는지 비교 후 삭제하기
                        if password_input == exercise_password:
                            del exercise_reason[i]

                            print(f"{user_choose_number}번 {del_} 완료")
                            break
                            
                        else:
                            print("다시 입력해주세요.")
                                
                    break
