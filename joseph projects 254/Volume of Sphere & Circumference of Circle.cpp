#include <stdio.h>
#define PI 3.14159265

double sphereVol(double r) { return (4.0 / 3.0) * PI * r * r * r; }
double circleCircumference(double r) { return 2.0 * PI * r; }

int main() {
    double rSphere, rCircle;
    printf("Enter sphere radius and circle radius: ");
    scanf("%lf %lf", &rSphere, &rCircle);
    printf("Sphere Volume: %.4f\nCircle Circumference: %.4f\n",
           sphereVol(rSphere), circleCircumference(rCircle));
    return 0;
}