def coloum_sort(lst, sort_key):
    sorted_list = sorted(lst, key=lambda x: x[sort_key])
    return sorted_list

# Example usage
data = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]

sorted_data = coloum_sort(data, "fruit")
print(sorted_data)

sorted_data = coloum_sort(data, "color")
print(sorted_data)
