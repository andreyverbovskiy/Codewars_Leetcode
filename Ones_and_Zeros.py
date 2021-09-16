def binary_array_to_number(arr):
    count = len(arr) - 1
    answ = []
    for i in arr:
        i=i*(2**count)
        answ.append(i)
        count = count - 1
