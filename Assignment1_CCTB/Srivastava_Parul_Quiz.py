# quiz_2.py

def reverse_list(lst):
    # Reverse the list in place
    lst.reverse()
    return lst

def replace_value(lst, old_value, new_value):
       for i in range(len(lst)):
        if lst[i] == old_value:
            lst[i] = new_value
            break
        return lst

def count_number_duplicates(lst):
    # Count the number of duplicate items in the list
    duplicates_count = 0
    item_count = {}

    for item in lst:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1

    for count in item_count.values():
        if count > 1:
            duplicates_count += count - 1

    return duplicates_count

if __name__ == "__main__":
    lst = [1, 2, 2, 5, 8, 4, 4, 8, 2, 1, 6]
    print("Original list:", lst)
    print("Reversed list:", reverse_list(lst.copy()))
    print("Modified list:", replace_value(lst.copy(), 5, 10))
    print("Number of duplicated items:", count_number_duplicates(lst))
