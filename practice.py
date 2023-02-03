def solution(store, customer):
    return list(map(lambda x: x in store, customer))

print(solution([2,3,7,8,9], [7,5,9]))