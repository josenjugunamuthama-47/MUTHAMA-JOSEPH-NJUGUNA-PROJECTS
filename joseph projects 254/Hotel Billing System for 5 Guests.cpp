/*
 * Hotel Billing System for 5 Guests
 * Applies a 10% discount on accommodation when stay exceeds 7 nights.
 */
#include <stdio.h>

int main() {
    int guest, nights;
    double roomRate, foodCharges, roomCost, totalBill;

    for (guest = 1; guest <= 5; guest++) {
        printf("\nGuest %d - Enter nights, room rate, food charges: ", guest);
        scanf("%d %lf %lf", &nights, &roomRate, &foodCharges);

        roomCost = nights * roomRate;
        if (nights > 7) {
            roomCost = roomCost * 0.90; // 10% discount on stay
        }
        totalBill = roomCost + foodCharges;

        printf("Guest %d Total Bill: KSh %.2f\n", guest, totalBill);
    }
    return 0;
}