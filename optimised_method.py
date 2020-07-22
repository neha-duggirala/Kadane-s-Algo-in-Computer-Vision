import time
begin = time.time()
array = [100,
    8,
    5,
    -9,
    1,
    3,
    -2,
    3,
    4,
    7,
    2,
    -18,
    6,
    3,
    1,
    -5,
    6,
    20,
    -23,
    15,
    1,
    -3,
    4
  ]
size = len(array)
currentMax, max_ = array[0],array[0]

for idx in range(size-1):
    # print(currentMax,max_)
    max_ = max(max_,currentMax+array[idx+1])
    currentMax =max(array[idx+1], currentMax+array[idx+1])
end = time.time()
print("Time elapsed: ", end - begin)
print(max_)
