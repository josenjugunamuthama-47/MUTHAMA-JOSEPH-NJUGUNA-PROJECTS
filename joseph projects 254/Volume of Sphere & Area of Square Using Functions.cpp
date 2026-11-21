#include <stdio.h>
#define PI 3.14159265

double sphereVol(double r) { return (4.0 / 3.0) * PI * r * r * r; }
double squareArea(double side) { return side * side; }

int main() {
    double r, s;
    printf("Enter sphere radius and square side: ");
    scanf("%lf %lf", &r, &s);
    printf("Sphere Volume: %.4f\nSquare Area: %.4f\n", sphereVol(r), squareArea(s));
    return 0;
}