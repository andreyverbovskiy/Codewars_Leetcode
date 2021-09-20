def create_phone_number(n):
    st=str(n) 
    s = st[1]+ st[4]+ st[7]
    s = '('+s+') '    
    t = st[10]+st[13]+st[16]+'-'+st[19]+st[22]+st[25]+st[28]
    return s+t
        
