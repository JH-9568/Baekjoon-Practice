def solution(a, b):
    ab = int(str(a) + str(b))
    mul = 2 * a * b
    
    if ab >= mul:
        return ab
    else:
        return mul