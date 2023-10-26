def find_max(num_list):
    # Check if the list is empty
    if not num_list:
        return None

    # If the list has only one element, return that element
    elif len(num_list) == 1:
        return num_list[0]

    # Convert the first element to an integer
    first_num = int(num_list[0])

    # Recursively find the maximum value in the remaining list
    remaining_max = find_max(num_list[1:])

    # If there is a valid maximum value in the remaining list, compare it with the first number
    if remaining_max is not None:
        return first_num if int(first_num )> int(remaining_max) else remaining_max

    # If the remaining list is empty, return the first number
    else:
        return first_num

num_list = ['34', '56', '1', '31', '52', '45', '23', '89', '56', '10', '1230', '15']
print(find_max(num_list))