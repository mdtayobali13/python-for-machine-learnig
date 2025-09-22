def remove_duplicates(input_list):
    unique_list = []

    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list

input_list = [1,2,3,4,2,3,2,7,8]
remove_duplicates(input_list)

print(f'Real list : {input_list} ')
print(f'uniq list : {remove_duplicates(input_list)} ')