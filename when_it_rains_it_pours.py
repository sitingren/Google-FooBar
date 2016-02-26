def answer(heights):
    if len(heights) < 3:
        return 0
        
    # record the max num seen from left/right
    max_left = 0
    max_right = 0
    
    # two pointers
    left = 0
    right = len(heights) - 1
    
    volume = 0

    while left < right:
        if max_left < heights[left]:
            max_left = heights[left]
        if max_right < heights[right]:
            max_right = heights[right]
            
        if max_right >= max_left:
            volume += max_left - heights[left]
            left += 1
        else:
            volume += max_right - heights[right]
            right -= 1

    return volume