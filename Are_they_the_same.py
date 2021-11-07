def comp(array1, array2):
    
    score = 0
    
    if(array1 is None):
        return False
    if(array2 is None):
        return False
    
    
        
    if(len(array1) == len(array2)):    
        
        array1 = set(array1)
        array2 = set(array2)
    
    
        for x in array1:
            for y in array2:      
                if (y == x**2):
                    score = score + 1
    
    else:
        return False
    
    if (score == len(array2)):
        return True
    else:
        return False
	
