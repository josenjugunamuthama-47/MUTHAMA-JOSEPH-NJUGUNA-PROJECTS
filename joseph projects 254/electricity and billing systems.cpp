/*
 * Program: Electricity Billing System (5 Customers)
 * Purpose: Calculates electricity bills based on consumption slabs for 5 customers.
 * Inputs: Customer number and units consumed for each customer.
 * Processing: Uses if-else to select the unit rate and a for loop over 5 customers.
 * Outputs: Individual and total electricity bills.
 */
#include <stdio.h>

int main() {
    int customer, i;
    float unitsConsumed, ratePerUnit, electricityBill;

    for (i = 1; i <= 5; i++) {
        printf("\n--- Customer %d ---\n", i);
        printf("Enter customer number: ");
        scanf("%d", &customer);
        printf("Enter units consumed: ");
        scanf("%f", &unitsConsumed);

        if (unitsConsumed >= 0 && unitsConsumed <= 50) {
            ratePerUnit = 10.0;
        } else if (unitsConsumed > 50 && unitsConsumed <= 100) {
            ratePerUnit = 15.0;
        } else if (unitsConsumed > 100) {
            ratePerUnit = 20.0;
        } else {
            printf("Invalid units.\n");
            continue;
        }

        electricityBill = unitsConsumed * ratePerUnit;
        printf("Customer %d Bill: KSh %.2f\n", customer, electricityBill);
    }
    return 0;
}