#include <stdio.h>
#define PI 3.14159265

double sphereVol(double r) { return (4.0 / 3.0) * PI * r * r * r; }
double cylinderVol(double r, double h) { return PI * r * r * h; }

int main() {
    double rs, rc, hc;
    printf("Enter sphere radius: ");
    scanf("%lf", &rs);
    printf("Enter cylinder radius and height: ");
    scanf("%lf %lf", &rc, &hc);
    printf("Sphere Volume: %.4f\nCylinder Volume: %.4f\n",
           sphereVol(rs), cylinderVol(rc, hc));
    return 0;
}