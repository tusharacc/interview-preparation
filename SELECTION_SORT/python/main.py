from typing import TypeVar, List

# Define a generic type variable that can be any type supporting comparison operators
T = TypeVar('T')

def selection_sort(arr: List[T]) -> List[T]:
    n = len(arr)
    
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element of the unsorted part
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

# Example usage:
if __name__ == "__main__":
    number_list = [64, 25, 12, 22, 11]
    char_list = ['d', 'a', 'c', 'b', 'e']

    print("Sorted number list:", selection_sort(number_list))
    print("Sorted character list:", selection_sort(char_list))
