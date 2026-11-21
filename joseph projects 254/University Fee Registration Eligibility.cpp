/*
 * University Fee Registration Eligibility (10 Students)
 * Allows unit registration if at least 60% of total fees is paid.
 */
#include <stdio.h>

int main() {
    int i, studentNo;
    double totalFees, amountPaid, balance, percentPaid;

    for (i = 1; i <= 10; i++) {
        printf("\nStudent %d - Enter student no, total fees, amount paid: ", i);
        scanf("%d %lf %lf", &studentNo, &totalFees, &amountPaid);

        balance = totalFees - amountPaid;
        percentPaid = (totalFees > 0) ? (amountPaid / totalFees) * 100.0 : 0.0;

        printf("Student %d | Paid: %.1f%% | Balance: %.2f -> ",
               studentNo, percentPaid, balance);

        if (percentPaid >= 60.0) {
            printf("Eligible to register for units\n");
        } else {
            printf("Not eligible to register for units\n");
        }
    }
    return 0;
}