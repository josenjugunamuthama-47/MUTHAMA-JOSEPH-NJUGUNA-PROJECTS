/*
 * Hospital Billing System (5 Patients)
 * Applies a 10% discount when total bill exceeds KSh 10,000.
 */
#include <stdio.h>

int main() {
    int p, patientId;
    double consultFee, medCost, totalBill, finalBill;

    for (p = 1; p <= 5; p++) {
        printf("\nPatient %d - Enter ID, consultation fee, medicine cost: ", p);
        scanf("%d %lf %lf", &patientId, &consultFee, &medCost);

        totalBill = consultFee + medCost;
        if (totalBill > 10000.0) {
            finalBill = totalBill * 0.90;
        } else {
            finalBill = totalBill;
        }

        printf("Patient %d Final Bill: KSh %.2f\n", patientId, finalBill);
    }
    return 0;
}