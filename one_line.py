def toggle_dict(dict):
    ans = {}
    for i in dict :
        # ans[i.value] = i.key
        ans[dict[i]] = i
    return ans
my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}
print(toggle_dict(my_dict))
