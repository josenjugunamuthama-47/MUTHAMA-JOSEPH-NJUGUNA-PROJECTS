/*
 * Public Transport Fare System (10 Passengers)
 * Applies a 20% senior discount for passengers aged 60 or older.
 */
#include <stdio.h>

int main() {
    int i, age;
    double distance, ratePerKm = 15.0, fare;

    for (i = 1; i <= 10; i++) {
        printf("\nPassenger %d - Enter age and distance (km): ", i);
        scanf("%d %lf", &age, &distance);

        fare = distance * ratePerKm;
        if (age >= 60) {
            fare = fare * 0.80; // 20% senior discount
        }

        printf("Passenger %d Fare: KSh %.2f\n", i, fare);
    }
    return 0;
}