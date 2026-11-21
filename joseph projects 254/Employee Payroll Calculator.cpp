/*
 * Employee Payroll Calculator (10 Employees)
 * Calculates overtime pay (KSh 500/hr above 40 hours) and gross salary.
 */
#include <stdio.h>

int main() {
    int emp;
    float basicSalary, hoursWorked, overtimeHours, overtimePay, grossSalary;

    for (emp = 1; emp <= 10; emp++) {
        printf("\nEmployee %d - Basic salary & hours worked: ", emp);
        scanf("%f %f", &basicSalary, &hoursWorked);

        if (hoursWorked > 40.0) {
            overtimeHours = hoursWorked - 40.0;
            overtimePay = overtimeHours * 500.0;
        } else {
            overtimeHours = 0.0;
            overtimePay = 0.0;
        }

        grossSalary = basicSalary + overtimePay;
        printf("Overtime Hrs: %.2f | Overtime Pay: %.2f | Gross Salary: %.2f\n",
               overtimeHours, overtimePay, grossSalary);
    }
    return 0;
}