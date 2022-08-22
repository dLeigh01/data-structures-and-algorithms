def insertion_sort(num_list):
    """
    Sorts a list of numbers in ascending order with the insertion method
    """
    for index, item in enumerate(num_list):
        if index > 0:
            check = index - 1
            temp = num_list[index]

            while check >= 0 and temp < num_list[check]:
                num_list[check + 1] = num_list[check]
                check -= 1

            num_list[check + 1] = temp

    return num_list
