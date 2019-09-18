# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    arrayLenght = len(A)
    numberOfRotate = K%arrayLenght
    arrayRotatedSlice = A[-numberOfRotate:]

    del A[-numberOfRotate:]
    return arrayRotatedSlice + A
    pass

print(solution([3, 8, 9, 7, 6],3))