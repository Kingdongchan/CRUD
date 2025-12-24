# 운동을 해야하는 이유를 담을 곳

exercise_reason = []

def write_reason(reason, wirter):
    add_reaon = f"{reason} - {wirter}"
    exercise_reason.append(add_reaon)
    

def watch_reason():
    print("--현재 들어 있는 이유--")
    print(exercise_reason)

