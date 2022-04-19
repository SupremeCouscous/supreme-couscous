scores = [95, 90, 85, 80, 75, 70]

def judge(x):
    if x >= 90:
        return 'A'
    elif x> 80:
        return 'B'
    elif x >= 70:
        return 'C'
    elif x >= 60:
        return 'D'
    else:
        return 'fail'

for score in scores:
    print(judge(score))