import time
def kadanes(array):
    begin = time.time()
    # array = range(1000) #0.0009961128234863281
    size = len(array)
    currentMax, max_ = array[0],array[0]

    for idx in range(size-1):
        # print(currentMax,max_)
        max_ = max(max_,currentMax+array[idx+1])
        currentMax =max(array[idx+1], currentMax+array[idx+1])
    end = time.time()
    print("Time elapsed: ", end - begin)
    print(max_)
