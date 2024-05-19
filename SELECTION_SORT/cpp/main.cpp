#include <iostream>
#include <vector>
#include <algorithm> // For std::swap

using namespace std;

vector<int> selection_sort(vector<int>& arr) {
    for (size_t i = 0; i < arr.size() - 1; i++) {
        size_t min_index = i;
        for (size_t j = i + 1; j < arr.size(); j++) {
            if (arr[j] < arr[min_index]) {
                min_index = j;
            }
        }
        if (min_index != i) {
            swap(arr[i], arr[min_index]);
        }
    }
    return arr;
}

int main() {
    vector<int> arr = {5, -3, -1, 0, 1, 3, 5};
    vector<int> arr1 = selection_sort(arr);

    for (int item : arr1) {
        cout << item << "\n";
    }

    return 0;
}