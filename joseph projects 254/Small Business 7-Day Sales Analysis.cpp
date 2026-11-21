/*
 * Small Business 7-Day Sales Analysis
 * - totalSales: accumulates revenue across 7 days
 * - salesTarget: benchmark revenue to evaluate performance
 * - averageSales: mean daily revenue over the 7-day period
 */
#include <stdio.h>

int main() {
    int day;
    double dailySales, salesTarget, totalSales = 0.0, averageSales;

    printf("Enter daily sales target: ");
    scanf("%lf", &salesTarget);

    for (day = 1; day <= 7; day++) {
        printf("Enter sales for Day %d: ", day);
        scanf("%lf", &dailySales);
        totalSales += dailySales;

        if (dailySales >= salesTarget) {
            printf("  Day %d: Target achieved\n", day);
        } else {
            printf("  Day %d: Target not achieved\n", day);
        }
    }

    averageSales = totalSales / 7.0;
    printf("\nTotal 7-Day Sales: %.2f\nAverage Daily Sales: %.2f\n",
           totalSales, averageSales);
    if (totalSales >= salesTarget * 7.0) {
        printf("Weekly target achieved!\n");
    } else {
        printf("Weekly target not achieved.\n");
    }
    return 0;
}