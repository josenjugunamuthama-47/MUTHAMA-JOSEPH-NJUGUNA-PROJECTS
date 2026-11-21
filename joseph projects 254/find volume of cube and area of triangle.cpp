#include<stdio.h>
float volume(float y)
{
	return y*y*y;
}
float area(float b, float h)
{
	return 0.5*b*h;
}
int main()
{
	float a,b,c;
	printf("enter value of a ,b ,c ");
	scanf("%a%b%c",&a,&b,&c);
	printf("volume=%f", volume(a));
	printf("area=%f",area(b,c));6
	return 0;
}