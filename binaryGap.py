def solution(N):
    binaryText = "{0:b}".format(N)
    startCounter = False
    count = 0
    sequenceZero = []
    for i in binaryText :
        if(i=="1" and startCounter==False):
            count = 0
            startCounter = True
        elif(i=="0" and startCounter):
            count += 1
        elif(i=="1" and startCounter):
            startCounter = False
            sequenceZero.append(count)
    if not a:
        return 0

    return sequenceZero

print (solution(32))