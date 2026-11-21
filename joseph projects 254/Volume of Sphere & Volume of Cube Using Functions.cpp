#include <stdio.h>
#define PI 3.14159265

double sphereVol(double r) { return (4.0 / 3.0) * PI * r * r * r; }
double cubeVol(double side) { return side * side * side; }

int main() {
    double r, s;
    printf("Enter sphere radius and cube side: ");
    scanf("%lf %lf", &r, &s);
    printf("Sphere Volume: %.4f\nCube Volume: %.4f\n", sphereVol(r), cubeVol(s));
    return 0;
}