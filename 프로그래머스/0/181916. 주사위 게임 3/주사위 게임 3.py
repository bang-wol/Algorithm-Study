def solution(a, b, c, d):
    
    dice=sorted([a,b,c,d])
    
    if dice[0]==dice[3]:
        return 1111*dice[0]
    
    if dice[0]==dice[2] or dice[1]==dice[3]:
        p=dice[1]
        q=dice[3] if dice[0]==dice[2] else dice[0]
        return (10*p+q)**2
    
    if dice[0]==dice[1] and dice[2] ==dice[3]:
        return (dice[0]+dice[2])*abs(dice[0]-dice[2])
    
    if dice[0]==dice[1]:
        return dice[2]*dice[3]
    if dice[1]==dice[2]:
        return dice[0]*dice[3]
    if dice[2]==dice[3]:
        return dice[0]*dice[1]
    
    return dice[0]