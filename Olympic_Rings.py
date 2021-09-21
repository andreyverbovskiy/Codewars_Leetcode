def olympic_ring(string):
    count = 0
    for x in string:
        if (x == "q" or x =='Q' or x =='R' or x =='o' or x =='O' or x =='p' or x =='P' or x =='a' or x =='d'or x =='D' or x =='g' or x =='b' or x =='e' or x == 'A'):
            count = count +1
        elif(x == 'B'):
            count = count +2
    result = int(count/2)
    
    if(result>3):
        return 'Gold!'
    elif(result==3):
        return 'Silver!'
    elif(result==2):
        return 'Bronze!'
    else:
        return 'Not even a medal!'
