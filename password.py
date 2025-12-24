# 관리자를 구별하는 패스워드를 확인하고 싶음

password = "1234"

user_password = input("비밀번호를 입력하세요:")

if user_password == password:
    print("로그인 완료")
else:
    print("다시 입력해주세요")