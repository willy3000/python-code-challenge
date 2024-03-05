def solution(N):
    alphabet = 'abcdefghijklmno'
    length = len(alphabet)
    result = ""

    for i in range(N):
        result += alphabet[i % length]

    return result

# Test
print(solution(3))  
print(solution(5))   
print(solution(30))  