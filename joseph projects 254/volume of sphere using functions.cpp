#include <stdio.h>
#define PI 3.14159265

double sphereVol(double r) {
    return (4.0 / 3.0) * PI * r * r * r;
}

int main() {
    double r;
    printf("Enter radius of sphere: ");
    scanf("%lf", &r);
    printf("Volume of sphere: %.4f\n", sphereVol(r));
    return 0;
}