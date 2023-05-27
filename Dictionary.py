def get_file_type(extension_type_string, file_list):
    extension_type_list = extension_type_string.split(';')
    print(extension_type_list)
    extension_type_dict = {}
    for item in extension_type_list:
        extension, file_type = item.split(',')
        extension_type_dict[extension] = file_type
    
    file_type_dict = {}
    for file in file_list:
        if('.' in file):
            filename, extension = file.split('.')
            file_type = extension_type_dict.get(extension, 'unknown')
            file_type_dict[file] = file_type
        else:
            filename = file
            file_type_dict[file] = 'unknown'
        
    
    return file_type_dict

extension_type_string = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
file_list = ["abc.jpg", "xyz.xls", "text.csv","123"]
file_type_dict = get_file_type(extension_type_string, file_list)
print(file_type_dict)
