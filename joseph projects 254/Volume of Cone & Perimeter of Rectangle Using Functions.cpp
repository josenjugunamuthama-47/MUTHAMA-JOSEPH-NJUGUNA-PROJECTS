#include <stdio.h>
#define PI 3.14159265

double coneVol(double r, double h) { return (1.0 / 3.0) * PI * r * r * h; }
double rectPerimeter(double l, double w) { return 2.0 * (l + w); }

int main() {
    double r, h, l, w;
    printf("Enter cone radius and height: ");
    scanf("%lf %lf", &r, &h);
    printf("Enter rectangle length and width: ");
    scanf("%lf %lf", &l, &w);
    printf("Cone Volume: %.4f\nRectangle Perimeter: %.4f\n",
           coneVol(r, h), rectPerimeter(l, w));
    return 0;
}
