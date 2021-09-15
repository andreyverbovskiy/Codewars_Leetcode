import string

def is_pangram(s):
    letters = string.ascii_letters
    arr = [0] * 26
    answer = []
    
    for x in s:
        if(x in letters):
            
            try:
                i=answer.index(x)
            except:
                answer.append(x)
            else:
                pass
    if(len(answer) >=26):
        return True
    else:
        return False
