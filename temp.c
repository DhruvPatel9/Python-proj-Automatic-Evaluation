#include <stdio.h>

// Function for binary search
int binarySearch(int arr[], int low, int high, int target) {
    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (arr[mid] == target) {
            return 1; // Element found
        } else if (arr[mid] <= target) {
            low = mid + 1; // Search in the right half
        } else {
            high = mid - 1; // Search in the left half
        }
    }

    return 0; // Element not found
}

int main() {
    // Input: Number of elements
    int n;

    scanf("%d", &n);

    // Input: Sorted array
    int arr[n];
  
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    // Input: Target element
    int target;
   
    scanf("%d", &target);

    // Perform binary search
    int result = binarySearch(arr, 0, n - 1, target);

    // Output
    if (result) {
        printf("found\n");
    } else {
        printf("notfound\n");
    }

    return 0;
}
