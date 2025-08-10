def solution(n, w, num):
    before_top_height, top_boxes_num = divmod(n, w)
    before_top_height -= 1
    
    if top_boxes_num == 0:
        top_boxes_num = w
        before_top_height -= 1
        
    num_box_height, num_box_pos = divmod(num, w)
    if num_box_pos == 0:
        num_box_pos = w
        num_box_height -= 1
        
    answer = 1 # 박스는 필요한 해당 박스를 빼는 것까지 포함하기에 1이 디폴트
    
    # top과 num층 방향이 다르다면
    if num_box_height % 2 != (before_top_height + 1) % 2:
        
        # w - top_boxes_num가 num_box_pos보다 작아야 top box도 빼야 함
        if w - top_boxes_num < num_box_pos:
            answer += 1
            
    # top과 num층 방향이 같다면
    else:
        
        # top_boxes_num가 num_box_pos보다 같거나 많아야 top box를 빼야 함
        if num_box_pos <= top_boxes_num:
            answer += 1
        
    answer += before_top_height - num_box_height
    return answer