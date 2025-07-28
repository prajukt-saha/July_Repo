#include <stdio.h>

int linearSearch(int arr[], int size, int target) {
	int i;
    for (i = 0; i < size; i++) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}

int main() {
    int numbers[] = {10, 20, 30, 40, 50};
    int size = sizeof(numbers) / sizeof(numbers[0]);
    int searchTarget = 30;

    int result = linearSearch(numbers, size, searchTarget);

    if (result != -1) {
        printf("Element %d found at index %d.\n", searchTarget, result);
    } else {
        printf("Element %d not found in the array.\n", searchTarget);
    }

    return 0;
}