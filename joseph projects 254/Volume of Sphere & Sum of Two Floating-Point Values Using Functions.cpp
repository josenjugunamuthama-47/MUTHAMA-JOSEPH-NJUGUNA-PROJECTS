#include <stdio.h>
#define PI 3.14159265

double sphereVol(double r) { return (4.0 / 3.0) * PI * r * r * r; }
double sumFloat(double a, double b) { return a + b; }

int main() {
    double r, x, y;
    printf("Enter sphere radius: ");
    scanf("%lf", &r);
    printf("Enter two floating-point numbers: ");
    scanf("%lf %lf", &x, &y);
    printf("Sphere Volume: %.4f\nSum: %.4f\n", sphereVol(r), sumFloat(x, y));
    return 0;
}