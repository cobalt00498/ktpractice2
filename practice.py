def solution(numbers):
    set_numbers = set(numbers)
    result = 0
    for n in range(0, 10):
        if n not in set_numbers:
            result += n
    return result
print(solution([1,2,3,4,6,7,8,0]))