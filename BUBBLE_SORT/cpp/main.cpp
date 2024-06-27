#include <iostream>
#include <vector>
#include <algorithm> // For std::swap

using namespace std;

vector<int> bubbleSort(vector<int>& arr) {
    for (size_t i = 0; i < arr.size() - 1; i++) {

        for (size_t j = arr.size()-1; j >=i  ; j--) {
            if (arr[j] > arr[j-1]) {
                swap(arr[j], arr[j-1]);
            }
        }
        
    }
    return arr;
}

int main() {
    vector<int> arr = {5, -3, -1, 0, 1, 3, 5};
    vector<int> arr1 = bubbleSort(arr);

    for (int item : arr1) {
        cout << item << "\n";
    }

    return 0;
}