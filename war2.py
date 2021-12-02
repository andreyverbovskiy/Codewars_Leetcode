def alphabet_war(fight):
    
    arr_letters = ['w','p','b','s','t','m','q','d','z','j']
    arr_numbers = [4,3,2,1,0,-4,-3,-2,-1,0]
    
    score = []
    word = []
    
    for x in fight:
        word.append(x)
        
        
    for x in word:
        if (x in arr_letters):
            if (x == 't' and word.index(x) > 0 and (word[word.index(x) - 1] in arr_numbers[5:-1])):
                if(len(word) > word.index(x) and (word[word.index(x) + 2] == 'j' or word[word.index(x) + 2] == 't')):
                    pass
                else:
                    word[word.index(x) - 1] = arr_letters[arr_letters.index(x) - 5]
            elif(x == 'j' and word.index(x) > 0 and (word[word.index(x) - 1] in arr_numbers[:4])):
                if(len(word) > word.index(x) and (word[word.index(x) + 2] == 'j' or word[word.index(x) + 2] == 't')):
                    pass
                else:
                    word[word.index(x) - 1] = arr_letters[arr_letters.index(x) + 5]
            elif():
            
                
        
    for x in word:
        if (x in arr_letters):
            score.append(arr_numbers[arr_letters.index(x)])
    
    
    
    
            
    if(sum(score) > 0):
        return 'Left side wins!'
    elif(sum(score) < 0):
        return 'Right side wins!'
    else:
        return "Let's fight again!"
     
