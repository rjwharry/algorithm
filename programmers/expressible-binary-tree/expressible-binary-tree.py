def decimal_to_binary(number):
    binary = ""
    while (number != 0):
        div, mod = divmod(number, 2)
        binary = str(mod) + binary
        number = div
    return binary

def is_expressible(binary):
    length = len(binary)
    if length == 1 or length == 2:
        return True
    center = int((length - 1) / 2)
    if binary[center] == '0':
        return False
    else:
        return is_expressible(binary[0:center]) and is_expressible(binary[center+1:])

def solution(numbers):
    answer = []
    for number in numbers:
        binary = decimal_to_binary(number)
        print(binary)
        if is_expressible(binary):
            answer.append(1)
        else:
            answer.append(0)
    return answer

if __name__ == "__main__":
    print(solution([1000000000000000]))