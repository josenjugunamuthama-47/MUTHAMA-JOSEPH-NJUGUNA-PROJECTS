#include <stdio.h>

int main(void) 
{
    float average;

    printf("Enter student's average mark: ");
    scanf("%f", &average);

    if (average >= 70.0f && average <= 100.0f) {
        printf("Grade: A\n");
    } else if (average >= 60.0f && average < 70.0f) {
        printf("Grade: B\n");
    } else if (average >= 50.0f && average < 60.0f) {
        printf("Grade: C\n");
    } else if (average >= 40.0f && average < 50.0f) {
        printf("Grade: D\n");
    } else if (average >= 0.0f && average < 40.0f) {
        printf("Grade: F\n");
    } else {
        printf("Invalid mark entered. Please enter a value between 0 and 100.\n");
    }

    return 0;
}