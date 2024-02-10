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

def printArray(number_list, number_elements):
    for i in range(number_elements):
        print(number_list[i], end=' ')
    print()

def selectionSort(number_list, n):
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if number_list[min_idx] < number_list[j]:
                min_idx = j
        number_list[i], number_list[min_idx] = number_list[min_idx], number_list[i]
        printArray(number_list, n)

elements = len(number_list)
printArray(number_list, elements)
