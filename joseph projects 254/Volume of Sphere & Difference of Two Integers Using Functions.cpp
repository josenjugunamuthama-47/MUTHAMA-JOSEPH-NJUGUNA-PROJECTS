#include <stdio.h>
#define PI 3.14159265

double sphereVol(double r) { return (4.0 / 3.0) * PI * r * r * r; }
int diffInt(int a, int b) { return a - b; }

int main() {
    double r;
    int a, b;
    printf("Enter sphere radius: ");
    scanf("%lf", &r);
    printf("Enter two integers: ");
    scanf("%d %d", &a, &b);
    printf("Sphere Volume: %.4f\nDifference: %d\n", sphereVol(r), diffInt(a, b));
    return 0;
}