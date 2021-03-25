def merge(list1, list2):
    list1_length = len(list1)
    list2_length = len(list2)
    total_list_length = list1_length + list2_length
    merged_list = []
    comparisons = 0
    while len(merged_list) != total_list_length:
        val1 = list1[0]
        val2 = list2[0]
        comparisons = comparisons + 1
        if val1 > val2:
            merged_list = merged_list + [val2]
            list2.pop(0)
        else:
            merged_list = merged_list + [val1]
            list1.pop(0)
        if len(list1) == 0:
            for element in list2:
                merged_list = merged_list + [element]
        if len(list2) == 0:
            for element in list1:
                merged_list = merged_list + [element]
    return merged_list, comparisons

def merge_sort(list_0):
    if len(list_0) == 1:
        return list_0
    list1, list2 = split_list(list_0)
    merged_list, comparisons = merge(merge_sort(list1), merge_sort(list2))
    print(f"{comparisons} comparisons were made.")
    return merged_list

def split_list(list_0):
    return list_0[::2], list_0[1::2]




