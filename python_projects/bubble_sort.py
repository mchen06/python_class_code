list = [3, 4, 1, 1, 8]

def bubble_sort(list):
    # sorts in place
    length_list = len(list) - 1
    comparisons = 0
    x = 0
    has_swaped = True
    while has_swaped != False:
        has_swaped = False
        y = 0
        while y < length_list - x:
            comparisons = comparisons + 1
            if list[y] > list[y + 1]:
              swap_position(list, y, y + 1)
              has_swaped = True
            y = y + 1
        x = x + 1
    print(f"bubble sort has made {comparisons} comparisons.\n")
    return list

        
def swap_position(list, pos1, pos2):
    first_element = list[pos1]
    second_element = list[pos2]
    list[pos2] = first_element
    list[pos1] = second_element

print(bubble_sort(list))

