def alphabet_war(fight):
    
    arr_letters = ['w','p','b','s','t','m','q','d','z','j']
    arr_numbers = [4,3,2,1,0,-4,-3,-2,-1,0]
    
    score = []
    last_letter = ''
    
    for x in fight:
        if (x in arr_letters):           
            if (arr_letters[arr_letters.index(x)] == 't' and len(score) > 0 and arr_letters.index(last_letter) > arr_letters.index('t')):
                
                if(fight[fight.index(x)-2] == 'j' and len(fight) > 2):
                    score.append(arr_numbers[arr_letters.index(x)])
                    last_letter = x
                else:
                    score[-1] = score[-1] * (-1)
                    last_letter = x
            elif (arr_letters[arr_letters.index(x)] == 'j' and len(score) > 0 and arr_letters.index(last_letter) < arr_letters.index('t')):
                
                if(fight[fight.index(x)-2] == 't' and len(fight) > 2):
                    score.append(arr_numbers[arr_letters.index(x)])
                    last_letter = x
                else:
                    score[-1] = score[-1] * (-1)
                    last_letter = x
                
            elif (last_letter == 't' and arr_letters.index(x) > arr_letters.index('t')):   #future values
                score.append(arr_numbers[arr_letters.index(x)] * (-1))   
                last_letter = x
                
            elif (last_letter == 'j' and arr_letters.index(x) < arr_letters.index('t')):   #future values
                score.append(arr_numbers[arr_letters.index(x)] * (-1))   
                last_letter = x
            elif(len(fight) > 2 and arr_letters[arr_letters.index(x)] == 't' and len(score) > 0 and fight[fight.index(x)-2] == 'j' and arr_letters.index(fight[fight.index(x)-1]) < arr_letters.index('t')):
                score[-1] = score[-1] * (-1)
                score.append(arr_numbers[arr_letters.index(x)])
                last_letter = x
            elif(len(fight) > 2 and arr_letters[arr_letters.index(x)] == 'j' and len(score) > 0 and fight[fight.index(x)-2] == 't' and arr_letters.index(fight[fight.index(x)-1]) > arr_letters.index('t')):
                score[-1] = score[-1] * (-1)
                score.append(arr_numbers[arr_letters.index(x)])
                last_letter = x
            else:
                score.append(arr_numbers[arr_letters.index(x)])
                last_letter = x
            
    if(sum(score) > 0):
        return 'Left side wins!'
    elif(sum(score) < 0):
        return 'Right side wins!'
    else:
        return "Let's fight again!"
     
