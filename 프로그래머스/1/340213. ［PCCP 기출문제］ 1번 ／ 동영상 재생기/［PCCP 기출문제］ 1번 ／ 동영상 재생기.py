def solution(video_len, pos, op_start, op_end, commands):
    video_len = int(video_len[:-3]) * 60 + int(video_len[-2:])
    pos = int(pos[:-3]) * 60 + int(pos[-2:])
    op_start = int(op_start[:-3]) * 60 + int(op_start[-2:])
    op_end = int(op_end[:-3]) * 60 + int(op_end[-2:])
    
    # 커맨드 수행
    for c in commands:
    
        # 오프닝 안 -> 오프닝 끝으로 이동
        if c == "prev":
            pos -= 10
            
            if pos < 0:
                pos = 0
                
            if op_start <= pos <= op_end:
                pos = op_end
                
        # 오프닝 안 -> 오프닝 끝나고 10초 후
        # 오프닝 근처 -> 오프닝 끝
        # 영상 초과길이 -> 영상 끝
        elif c == "next":
            if op_start <= pos <= op_end:
                pos = op_end + 10
                
            elif op_start <= pos + 10 <= op_end:
                pos = op_end
            
            else: pos += 10
            
            if pos > video_len:
                pos = video_len
    
    return f"{pos // 60:02}:{pos % 60:02}"  









