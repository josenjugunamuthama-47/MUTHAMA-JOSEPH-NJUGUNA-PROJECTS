/*
 * Inventory Stock Alert System (5 Products)
 * Computes item stock value and prints "Reorder Stock" if quantity < 10.
 */
#include <stdio.h>

int main() {
    int p, prodCode, quantity;
    double unitPrice, stockValue;

    for (p = 1; p <= 5; p++) {
        printf("\nProduct %d - Enter code, quantity, unit price: ", p);
        scanf("%d %d %lf", &prodCode, &quantity, &unitPrice);

        stockValue = quantity * unitPrice;
        printf("Code %d | Stock Value: %.2f", prodCode, stockValue);

        if (quantity < 10) {
            printf(" -> Reorder Stock\n");
        } else {
            printf(" -> Stock OK\n");
        }
    }
    return 0;
}