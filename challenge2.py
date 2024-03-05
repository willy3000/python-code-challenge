def solution(A):
    sums_dict = {}

    max_sum = -1

    for num in A:
        current_sum = sum(int(digit) for digit in str(num))

        if current_sum in sums_dict:
            max_sum = max(max_sum, num + sums_dict[current_sum])

        sums_dict[current_sum] = max(sums_dict.get(current_sum, 0), num)

    return max_sum

# Tests
print(solution([51, 71, 17, 42]))
print(solution([42, 33, 60]))
print(solution([51, 32, 43]))