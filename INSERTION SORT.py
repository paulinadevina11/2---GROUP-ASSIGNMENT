array = []

#STRING TYPE ELEMENT
str_element = []

#INTEGER TYPE ELEMENT
int_element = []

#PROCESSING ELEMENT
number_of_elements = int(input(f"How much element you want to sort?: "))
for element in range(number_of_elements):
    putting_element = input(f"Enter element {element+1}: ")
    try:
        int_element.append(int(putting_element))
    except ValueError:
        str_element.append(str(putting_element))

def printArray(arr, n):
    for index in range(n):
        print (arr[index], end = " ")
    print()

def insertionSort(arr,n):
    for index in range(1, n):
        key = arr[index]
        last_element = index-1
        while last_element >= 0 and key < arr[last_element]:
            arr[last_element + 1] = arr[last_element]
            last_element -= 1
        arr[last_element + 1] = key
        printArray(arr,n)

print("Integer elements before sorting:", int_element)
insertionSort(int_element, len(int_element))
print("Integer elements after sorting:", int_element)

print("String elements before sorting:", str_element)
insertionSort(str_element, len(str_element))
print("String elements after sorting:", str_element)