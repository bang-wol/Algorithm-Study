def solution(babbling):
    answer = 0
    
    available=["aya","ye","woo","ma"]
    
    for word in babbling:
        prev=""
        i=0
        
        while i < len(word):
            found=False
            
            for babble in available:
                if word[i:i+len(babble)]==babble and babble!=prev:
                    prev=babble
                    i+=len(babble)
                    found=True
                    break
            if not found:
                break
        if i==len(word):
                answer+=1
    
    
    return answer