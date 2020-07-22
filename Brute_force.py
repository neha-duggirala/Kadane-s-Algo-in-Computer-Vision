array =[-2, 1]
size = len(array)
max_ = array[0]
for idx1 in range(size):
    for idx2 in range(idx1+1,size+1):
        # print(sum(array[idx1:idx2]),(array[idx1:idx2]))
        max_ = max(sum(array[idx1:idx2]),max_)


print(max_)
