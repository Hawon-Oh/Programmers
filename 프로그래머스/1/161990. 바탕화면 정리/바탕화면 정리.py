def solution(wallpaper):
    
    # 4변으로부터 가장 가까운 파일의 좌표들을 찾는다 (총 4개이며 같은좌표 중복가능)
    # S(s_h, s_w), E(e_h, e_w) 구하기위해 총 4개의 변수가 필요하다
    #   s_h는 row min
    #   s_w는 col min
    #   e_h는 row max
    #   e_w는 col max
    # 2차원함수 돌면서 하나씩 찾으며 업데이트한다.
    # 이 알고리즘은 거리를 구할 필요가 없으니 그냥 
    #   return s_h, s_w, e_h + 1, e_w + 1
    
    # 초기값
    r_min, c_min, r_max, c_max = 9999, 9999, -9999, -9999
    
    for row in range(len(wallpaper)):
        for col in range(len(wallpaper[0])):
            
            # 파일이 없으면 패스
            if wallpaper[row][col] != '#': continue
            if row > r_max: r_max = row
            if row < r_min: r_min = row
            if col > c_max: c_max = col
            if col < c_min: c_min = col
    
    return r_min, c_min, r_max + 1, c_max + 1










