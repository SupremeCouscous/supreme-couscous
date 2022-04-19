def judge(inputScore):
    return 'good' if inputScore >= 80 else 'bad'

def judge2(inputScore):
    return ('bad','good')[inputScore >= 80]

scores [95, 90, 85, 80, 75, 70]

for s in scores:
    print("%d score =%s, %s" % (s, judge(s), judge2(s)))