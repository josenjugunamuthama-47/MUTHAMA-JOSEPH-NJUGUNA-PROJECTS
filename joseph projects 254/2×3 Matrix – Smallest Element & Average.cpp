#include <stdio.h>

int main() {
    int matrix[2][3], i, j, smallest, sum = 0;
    float avg;

    printf("Enter 6 elements for a 2x3 matrix:\n");
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 3; j++) {
            scanf("%d", &matrix[i][j]);
            sum += matrix[i][j];
            if (i == 0 && j == 0 || matrix[i][j] < smallest)
                smallest = matrix[i][j];
        }
    }

    avg = (float)sum / 6.0;
    printf("Smallest: %d\nAverage: %.2f\n", smallest, avg);
    return 0;
}