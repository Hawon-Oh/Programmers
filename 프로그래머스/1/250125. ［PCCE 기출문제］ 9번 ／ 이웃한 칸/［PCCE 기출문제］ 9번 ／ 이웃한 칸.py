def solution(board, h, w):
    answer = 0
    color = board[h][w]
    
    for dh, dw in zip([0, 1, -1, 0], [1, 0, 0, -1]):
        if -1 < h + dh < len(board) and -1 < w + dw < len(board[0]):
            if color == board[h + dh][w + dw]:
                answer += 1
    
    return answer