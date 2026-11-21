/*
 * Bank Account Qualification System
 * Checks if 10 applicants have age >= 18 AND monthly income >= KSh 20,000.
 */
#include <stdio.h>

int main() {
    int i, age;
    double income;

    for (i = 1; i <= 10; i++) {
        printf("\nApplicant %d - Enter age and monthly income: ", i);
        scanf("%d %lf", &age, &income);

        if (age >= 18 && income >= 20000.0) {
            printf("Status: Qualified\n");
        } else {
            printf("Status: Not Qualified\n");
        }
    }
    return 0;
}