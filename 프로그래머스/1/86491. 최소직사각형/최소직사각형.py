def solution(sizes):
    max_w, max_h=0,0
    
    for size in sizes:
        h,w=sorted(size)
        max_w=max(max_w,w)
        max_h=max(max_h,h)
    return max_w * max_h