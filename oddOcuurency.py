def solution(N):
    distinctList = list(set(N.copy()))
    for number in distinct_list :
        if(N.count(number)==1):
            return number
    return ""
    pass