def f(lst, start, end):
    sub_list = lst[start:end+1:2]
    return sub_list

result = f([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41], 2, 9)
print(result)