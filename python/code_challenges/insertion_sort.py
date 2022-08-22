def insertion_sort(num_list):
    if len(num_list) <= 1:
        return num_list
    for index, item in enumerate(num_list):
        if index > 0:
            check = index - 1
            temp = num_list[index]

            while check >= 0 and temp < num_list[check]:
                num_list[check + 1] = num_list[check]
                check -= 1

            num_list[check + 1] = temp

    return num_list
