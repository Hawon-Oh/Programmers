def solution(board, moves):
    answer = 0
    stack = []
    for m in moves:
        for c in range(len(board)):
            if board[c][m - 1] > 0:
                stack.append(board[c][m - 1])
                board[c][m - 1] = 0
                break
                
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack = stack[:-2]
            answer += 2
            
    return answer