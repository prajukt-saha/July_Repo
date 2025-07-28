#include<stdio.h>
int main(){
    int a[5] = {1, 2, 3, 4, 5};
    int b[5] = {5, 6, 7, 8, 9};
    int c[10];
    int k = 0;
    int isDuplicate;

    for(int i = 0; i < 5; i++) {
        isDuplicate = 0;
        for(int j = 0; j < 5; j++) {
            if(a[i] == b[j]) {
                isDuplicate = 1;
                break;
            }
        }
        if(!isDuplicate) {
            c[k++] = a[i];
        }
    }


    for(int i = 0; i < 5; i++) {
        isDuplicate = 0;
        for(int j = 0; j < 5; j++) {
            if(b[i] == a[j]) {
                isDuplicate = 1;
                break;
            }
        }
        if(!isDuplicate) {
            c[k++] = b[i];
        }
    }

    printf("Non-duplicate elements: ");
    for(int i = 0; i < k; i++) {
        printf("%d ", c[i]);
    }
    printf("\n");
    return 0;
}