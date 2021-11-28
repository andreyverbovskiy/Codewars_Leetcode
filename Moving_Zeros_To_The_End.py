def move_zeros(array):
    
    for x in array:
        if (x == 0):
            array.pop(array.index(x))
            array.append(0)
    return array
