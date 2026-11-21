/*
 * Mobile Data Usage Monitor (5 Customers)
 * Calculates remaining data and flags "Low Data" when < 10% remains.
 */
#include <stdio.h>

int main() {
    int i, custNo;
    double allocatedData, usedData, balance;

    for (i = 1; i <= 5; i++) {
        printf("\nCustomer %d - Enter customer no, allocated MB, used MB: ", i);
        scanf("%d %lf %lf", &custNo, &allocatedData, &usedData);

        balance = allocatedData - usedData;
        printf("Customer %d Remaining: %.2f MB - ", custNo, balance);

        if (allocatedData > 0 && balance < (0.10 * allocatedData)) {
            printf("Low Data\n");
        } else {
            printf("Sufficient Data\n");
        }
    }
    return 0;
}