#include <stdio.h>
#define PI 3.14159265

double sphereVol(double r) { return (4.0 / 3.0) * PI * r * r * r; }
double coneVol(double r, double h) { return (1.0 / 3.0) * PI * r * r * h; }

int main() {
    double rs, rc, h;
    printf("Enter sphere radius: ");
    scanf("%lf", &rs);
    printf("Enter cone radius and height: ");
    scanf("%lf %lf", &rc, &h);
    printf("Sphere Volume: %.4f\nCone Volume: %.4f\n", sphereVol(rs), coneVol(rc, h));
    return 0;
}