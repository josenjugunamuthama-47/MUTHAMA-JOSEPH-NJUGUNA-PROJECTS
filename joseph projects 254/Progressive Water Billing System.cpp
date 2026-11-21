
 * Progressive Water Billing System (5 Customers)
 * Slabs: 1-20 @ 30, 21-50 @ 40, >50 @ 50.
 */
#include <stdio.h>

int main() {
    int c, custNo;
    double units, bill;

    for (c = 1; c <= 5; c++) {
        printf("\nCustomer %d - Enter customer number and units consumed: ", c);
        scanf("%d %lf", &custNo, &units);

        if (units <= 20) {
            bill = units * 30.0;
        } else if (units <= 50) {
            bill = (20 * 30.0) + ((units - 20) * 40.0);
        } else {
            bill = (20 * 30.0) + (30 * 40.0) + ((units - 50) * 50.0);
        }

        printf("Customer %d Bill: KSh %.2f\n", custNo, bill);
    }
    return 0;
}