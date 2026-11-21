/*
 * Loan Qualification & Monthly Repayment Schedule
 * Checks income eligibility against loan amount and prints monthly repayments.
 */
#include <stdio.h>

int main() {
    double income, loanAmount, annualRate, totalInterest, totalPayable, monthlyRepayment;
    int months, m;

    printf("Enter monthly income, loan amount, annual interest rate (%%), and months: ");
    scanf("%lf %lf %lf %d", &income, &loanAmount, &annualRate, &months);

    // Qualify if loan amount is at most 3x annual income and monthly income >= 15,000
    if (income >= 15000.0 && loanAmount <= income * 12.0 * 3.0 && months > 0) {
        totalInterest = (loanAmount * annualRate * (months / 12.0)) / 100.0;
        totalPayable = loanAmount + totalInterest;
        monthlyRepayment = totalPayable / months;

        printf("Loan Approved! Total Payable: %.2f\n", totalPayable);
        for (m = 1; m <= months; m++) {
            printf("Month %d repayment: %.2f\n", m, monthlyRepayment);
        }
    } else {
        printf("Loan Not Approved.\n");
    }
    return 0;
}