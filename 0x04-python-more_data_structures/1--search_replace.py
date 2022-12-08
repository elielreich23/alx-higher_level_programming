#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is not None:
        list = []
        for i, j in enumerate(my_list):
            if my_list[i] == search:
                list.append(replace)
            else:
                list.append(my_list[i])
            return list