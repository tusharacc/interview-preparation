### SELECTION SORT

*Selection Sort* follows a brute force strategy to sort the given array.

## ALGORITHM

1. Create two index, `i` & `j` such that `i = 0` and `j = i + 1`
2. Loop through the array from `i = 0` till `i < array.length - 1`
3. Create an inner loop that will scan from `j` till `j < array.length`
    4. If `array[i] < array[j]`, either swap the elements. The main goal of this step is for any `i` and `j`, identify the minimum value