def get_index(data_list: list, a_string: str) -> int:
    """
    A simple hash function that takes a string and returns an index within the bounds of the provided list i.e,
    the index will be between 0 and len(data_list) - 1.

    Args: data_list: List in which the index is to be found
          a_string: String to be hashed

    Returns: An integer index within the bounds of data_list
    """
    result = 0 # Variable to store the result (updated after each iteration)

    for a_character in a_string:
        # Convert the character to a number
        a_number = ord(a_character)
        # Update result by adding the number
        result += a_number

    # Take the remainder of the result with the size of the data list
    list_index = result % len(data_list)
    return list_index

if __name__ == "__main__":
    data_list: list = [None] * 4096 # Example list of size 4096
    print("check for the length of data_list: {}".format(len(data_list) == 4096))
    print("check for an element of data_list: {}".format(data_list[99] is None))

    print("check for get_index function for empty string: {}".format(get_index(data_list, "") == 0))
    print("check for get_index function for character 'a': {}".format(get_index(data_list, "a") == 97))
    print("check for get_index function for string 'Aakash': {}".format(get_index(data_list, "Aakash") == 585))

    # Testing with a different size of data_list
    data_list2: list = [None] * 48
    print("check for get_index function for same string 'Aakash' with different list size: {}".format(
        get_index(data_list2, "Aakash") == 9))

    check: int = ord("A") + ord("a") + ord("k") + ord("a") + ord("s") + ord("h") # 65 + 97 + 107 + 97 + 115 + 104 = 585
    print("check for manual calculation: {}".format(check % 48 == 9))

    # Storing a value in data_list at the index returned by get_index
    key, value = "Aakash", "78787878" # Tuple of key and value
    index: int = get_index(data_list, key)
    data_list[index]: tuple = key, value
    print("check for storing value in data_list: {}".format(data_list[index]))

    # Same operation expressed in one line
    data_list[get_index(data_list, "Hemanth")]: tuple = "Hemanth", "99999999"

    # Retrieving the value from data_list using the key
    key_to_find = "Aakash"
    index = get_index(data_list, key_to_find)
    stored_key, stored_value = data_list[index]

    if stored_key == key_to_find:
        print("Value found for {}: {}".format(key_to_find, stored_value))
    else:
        print("Value not found for {}".format(key_to_find))

    # List comprehension to show all key value pairs stored in data_list
    stored_items = [item[0] for item in data_list if item is not None]
    print("All stored items in data_list: {}".format(stored_items))