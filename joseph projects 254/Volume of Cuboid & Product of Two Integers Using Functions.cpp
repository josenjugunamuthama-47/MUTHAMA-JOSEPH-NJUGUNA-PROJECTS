#include <stdio.h>

double cuboidVol(double l, double w, double h) { return l * w * h; }
int multiplyInts(int a, int b) { return a * b; }

int main() {
    double l, w, h;
    int x, y;
    printf("Enter cuboid length, width, height: ");
    scanf("%lf %lf %lf", &l, &w, &h);
    printf("Enter two integers: ");
    scanf("%d %d", &x, &y);
    printf("Cuboid Volume: %.4f\nProduct: %d\n", cuboidVol(l, w, h), multiplyInts(x, y));
    return 0;
}