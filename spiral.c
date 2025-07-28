#include <stdio.h>
#include <stdlib.h>

void spirallyTraverse(int** mat, int r, int c) {
    int top = 0, bottom = r - 1, left = 0, right = c - 1;

    printf("Spiral Traversal: ");
    while (top <= bottom && left <= right) {
        for (int i = left; i <= right; i++)
            printf("%d ", mat[top][i]);
        top++;
     
        for (int i = top; i <= bottom; i++)
            printf("%d ", mat[i][right]);
        right--;

        if (top <= bottom) {
            for (int i = right; i >= left; i--)
                printf("%d ", mat[bottom][i]);
            bottom--;
        }

        if (left <= right) {
            for (int i = bottom; i >= top; i--)
                printf("%d ", mat[i][left]);
            left++;
        }
    }
    printf("\n");
}

int main() {
    int r, c;
    printf("Enter number of rows: ");
    scanf("%d", &r);
    printf("Enter number of columns: ");
    scanf("%d", &c);

    int** mat = (int**)malloc(r * sizeof(int*));
    for (int i = 0; i < r; i++) {
        mat[i] = (int*)malloc(c * sizeof(int));
    }

    printf("Enter the matrix elements:\n");
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            scanf("%d", &mat[i][j]);
        }
    }

    spirallyTraverse(mat, r, c);

    for (int i = 0; i < r; i++) {
        free(mat[i]);
    }
    free(mat);

    return 0;
}
