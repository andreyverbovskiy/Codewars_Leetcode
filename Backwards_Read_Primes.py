Backwards Read Primes

def backwards_prime(start, stop):
    
    answ = []
    answ1 = []

    ques = range(start,stop+1,1)
    
    for x in ques:
        a = range(1,x+1,1)
        arr = []
        for y in a:
            if(x%y ==0):
                arr.append(y)
        if(len(arr)==2):
            answ.append(x)
                
    for k in answ:
        reversed = int(str(k)[::-1])
        answ1.append(reversed)
        
    answ = []  
    
    for s in answ1:
        a1 = range(1,s+1,1)
        arr = []
        for y in a1:
            if(s%y ==0):
                arr.append(y)
        if(len(arr)==2):
            answ.append(s)
    
    answ1 = []
    
    for k in answ:
        reversed = int(str(k)[::-1])
        answ1.append(reversed)
        
    return answ1
