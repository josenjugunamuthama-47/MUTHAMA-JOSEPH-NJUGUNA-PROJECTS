#include <stdio.h>
#define PI 3.14159265

double sphereVol(double r) { return (4.0 / 3.0) * PI * r * r * r; }
double trianglePerimeter(double a, double b, double c) { return a + b + c; }

int main() {
    double r, a, b, c;
    printf("Enter sphere radius: ");
    scanf("%lf", &r);
    printf("Enter 3 sides of triangle: ");
    scanf("%lf %lf %lf", &a, &b, &c);
    printf("Sphere Volume: %.4f\nTriangle Perimeter: %.4f\n",
           sphereVol(r), trianglePerimeter(a, b, c));
    return 0;
}