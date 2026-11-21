#include <stdio.h>

int main() {
    int scores[10], i, smallest, sum = 0;
    printf("Enter 10 student scores:\n");
    for (i = 0; i < 10; i++) {
        scanf("%d", &scores[i]);
        sum += scores[i];
        if (i == 0 || scores[i] < smallest) smallest = scores[i];
    }
    printf("Smallest score: %d\nAverage score: %.2f\n", smallest, sum / 10.0);
    return 0;
}