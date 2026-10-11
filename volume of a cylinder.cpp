// muthama joseph njuguna
// PA106/G/33585/26

#include<stdio.h>
int main()

{
	
	float Pie,Radius,Length,Volume;
	
	printf("Enter your Pie: ");
	scanf("%f", &Pie);
	
	printf("Enter your Length: ");
	scanf("%f", &Length);
	
	printf("Enter your Radius: ");
	scanf("%f", &Radius);
	
	Volume = Pie * Length * Radius * Radius;
	printf("Volume= %f", Volume);
	
	return 0;
}