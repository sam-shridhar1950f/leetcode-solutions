def rotation(steps, arr, size):
    for num in range(0,steps):
        f = arr.pop(-1)
        arr.insert(0, f)
    listToStr = ' '.join(map(str, arr))
    return  listToStr

print(rotation(2, [1,2,3,4,5], 5))
