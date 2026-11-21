#include <stdio.h>

double diffFloat(double a, double b) { return a - b; }
double prodFloat(double a, double b) { return a * b; }

int main() {
    double x, y;
    printf("Enter two floating-point numbers: ");
    scanf("%lf %lf", &x, &y);
    printf("Difference: %.4f\nProduct: %.4f\n", diffFloat(x, y), prodFloat(x, y));
    return 0;
}