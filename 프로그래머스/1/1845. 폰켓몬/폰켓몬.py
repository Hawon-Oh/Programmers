def solution(nums):
    nums.sort()
    prev = nums[0]
    count = 1       # prev에 하나넣으니까 1 카운트
    pick = int(len(nums) / 2)
    
    
    # print(nums)
    for n in nums[1:]:
        # 폰켓몬이 두마리일 때 count는 1이어야 하니까 count체크를 맨앞에 둬야함.
        if  count >= pick:
            break
            
        if n != prev:
            count += 1
        
        
        
        prev = n
        
    return count