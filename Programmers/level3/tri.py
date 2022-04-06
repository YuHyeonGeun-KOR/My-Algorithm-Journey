def solution(triangle):
    answer = 0
    board =[[0]* len(triangle) for _ in range(len(triangle))]
    board[0][0] = triangle[0][0]
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                board[i][j] = board[i-1][0] + triangle[i][0]
            else:
                board[i][j] = max(board[i-1][j]+triangle[i][j] , board[i-1][j-1]+triangle[i][j])
    answer = max(board[-1])
    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))