/*
 * Supermarket Sales System (10 Customers)
 * - Input section: Reads item price and quantity for each customer.
 * - Calculation & Discount section: Computes total, applies 10% discount if total > 5000.
 * - Output section: Displays discount and final payable amount per customer.
 */
#include <stdio.h>

int main() {
    int i, quantity;
    float price, total, discount, finalCost;

    for (i = 1; i <= 10; i++) {
        printf("\nCustomer %d - Enter price and quantity: ", i);
        scanf("%f %d", &price, &quantity);

        total = price * quantity;
        if (total > 5000.0) {
            discount = total * 0.10;
        } else {
            discount = 0.0;
        }
        finalCost = total - discount;

        printf("Total: %.2f | Discount: %.2f | Final Cost: %.2f\n",
               total, discount, finalCost);
    }
    return 0;
}