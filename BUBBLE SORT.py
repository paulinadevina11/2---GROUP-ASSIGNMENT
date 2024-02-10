number_elements = int(input(f"Input the number you want to sort: "))
number_list = []

#BUBBLE SORT FOR NUMBER
for element in range(number_elements):
    putting_element = int(input(f"Enter number element {element + 1}: "))
    if putting_element > 10:
        print(f"Maximum number is 10")
    else:
        pass
    number_list.append(putting_element)

def bubble_sort(number_in_list):
    length_of_list = len(number_in_list)
    for i in range(length_of_list):
        for j in range(0, length_of_list - i - 1):
            if number_in_list[j] < number_in_list[j + 1]:
                number_in_list[j], number_in_list[j + 1] = number_in_list[j + 1], number_in_list[j]
    return number_in_list
bubble_sort(number_list)
print(bubble_sort(number_list))

#BUBBLE SORT FOR STRING
for element in range(number_elements):
    putting_element = str(input(f"Enter number element {element + 1}: "))
    number_list.append(putting_element)
def bubble_sort(number_in_list):
    length_of_list = len(number_in_list)
    for i in range(length_of_list):
        for j in range(0, length_of_list - i - 1):
            if number_in_list[j] < number_in_list[j + 1]:
                number_in_list[j], number_in_list[j + 1] = number_in_list[j + 1], number_in_list[j]
    return number_in_list


bubble_sort(number_list)
print(bubble_sort(number_list))