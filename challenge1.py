def solution(A):
    moves = 0
    length = len(A)
    
    for i in range(length-1):
        difference = A[i] - 10
        
        if difference > 0:
            A[i] -= difference
            A[i+1] += difference
            moves += difference
        
        elif difference < 0:
            difference = abs(difference)
            if difference > A[i+1]:
                return -1
            A[i] += difference
            A[i+1] -= difference
            moves += difference
    
    if A[-1] != 10:
        return -1
    
    return moves

# Tests
print(solution([7, 15, 10, 8]))
print(solution([11, 10, 8, 12, 8, 10, 11]))
print(solution([7, 14, 10]))