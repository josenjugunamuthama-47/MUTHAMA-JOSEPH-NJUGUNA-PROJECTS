/*
 * Library Fine System (10 Borrowers)
 * Charges KSh 20 per overdue day and warns if overdue days exceed 30.
 */
#include <stdio.h>

int main() {
    int i, borrowerNo, overdueDays;
    double fine;

    for (i = 1; i <= 10; i++) {
        printf("\nBorrower %d - Enter borrower number and overdue days: ", i);
        scanf("%d %d", &borrowerNo, &overdueDays);

        if (overdueDays < 0) overdueDays = 0;
        fine = overdueDays * 20.0;
        printf("Borrower %d Fine: KSh %.2f\n", borrowerNo, fine);

        if (overdueDays > 30) {
            printf("WARNING: Overdue period exceeds 30 days!\n");
        }
    }
    return 0;
}