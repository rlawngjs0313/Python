import numpy as np
def initialize():
    plate = np.random.randint(low=1, high=10, size=162).reshape((9, 18))
    print(plate)
    return plate
def inputing():
    user = list(map(str, input("[?:?] : ").split()))
    if user[0].isdigit() == True and user[2].isdigit() == True:
        user = user[0], user[2]
        return user
    else:
        inputing()
def calculate(plate, user):
    score = 0
    user_pick = plate[user[0]:user[1]]
    sum_num = sum(user_pick)
    if sum_num == 10:
        score += len(user_pick)
        print(score)
        return [score, True]
    else:
        return [score, False]

plate = initialize()
user = inputing()
print(calculate(plate, user))