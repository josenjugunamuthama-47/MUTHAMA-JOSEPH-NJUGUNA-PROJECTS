#include<stdio.h>
const float pi=3.14;
float area(float r)
{
	return pi*r*r;
}
int main()
{
float radius,area;
printf("enter radius= ");
scanf("%f", &radius);
printf("area=%f", area);
return 0;
}

