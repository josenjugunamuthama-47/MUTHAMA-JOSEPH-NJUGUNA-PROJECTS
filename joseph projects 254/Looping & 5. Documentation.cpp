/*
 * Program: Student Pass/Fail Counter
 * Purpose: Processes marks for 10 students and counts passes vs. failures.
 * Inputs: 10 floating-point student marks (pass mark >= 50).
 * Processing: Loops 10 times, checks each mark against 50, increments pass/fail counters.
 * Outputs: Total number of students who passed and failed.
 */
#include <stdio.h>

int main() {
    int i, passed = 0, failed = 0;
    float mark;

    for (i = 1; i <= 10; i++) {
        printf("Enter mark for student %d: ", i);
        scanf("%f", &mark);

        if (mark >= 50) {
            passed++;
        } else {
            failed++;
        }
    }

    printf("Passed: %d\n", passed);
    printf("Failed: %d\n", failed);
    return 0;
}