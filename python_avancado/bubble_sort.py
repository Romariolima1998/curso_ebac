

def bubble_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        for j in range(len(unsorted_list) - 1):

            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
          
    return unsorted_list


lista = [70, 60, 50, 40, 30, 20, 10]

print(bubble_sort(lista))
