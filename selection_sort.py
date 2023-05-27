def selection_sort(list):
    for i in range(len(list)):
        minIndex = i
        for j in range(i+1 , len(list)):
            if(list[j] < list[minIndex]):
                minIndex = j
        list[minIndex],list[i] = list[i],list[minIndex]
    return list

list = [9,8,7,6,5,4,2,1]
ans = selection_sort(list)
print(list)