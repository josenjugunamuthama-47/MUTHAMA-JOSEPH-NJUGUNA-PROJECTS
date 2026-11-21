#include <stdio.h>

int main() {
    int matrix[3][4];
    int i, j, smallest, sum = 0;
    float average;

    printf("Enter elements for a 3x4 matrix:\n");
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 4; j++) {
            printf("Element [%d][%d]: ", i, j);
            scanf("%d", &matrix[i][j]);
            sum += matrix[i][j];
            if (i == 0 && j == 0) {
                smallest = matrix[i][j];
            } else if (matrix[i][j] < smallest) {
                smallest = matrix[i][j];
            }
        }
    }

    average = (float)sum / (3 * 4);
    printf("Smallest element: %d\n", smallest);
    printf("Average of all elements: %.2f\n", average);
    return 0;
}