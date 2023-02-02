def solution(my_string):
    my_numbers = list(map(int, list(my_string)))
    result = my_numbers[0]
    ouput_string = str(my_numbers[0])
    for i in my_numbers[1:]:
        if i not in [0, 1] and result != 0:
            result *= i
            ouput_string += f" X {i}"
        elif i == 1 or result == 0:
            result += i
            ouput_string = ouput_string + f" + {i}"
        elif i == 0:
            ouput_string += f" + {i}"
    return ouput_string + f" = {result}"

print(solution("02984"))
print(solution("567"))
            