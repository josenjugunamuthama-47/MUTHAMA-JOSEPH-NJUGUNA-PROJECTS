// muthama joseph njuguna
// PA106/G/33585/26

#include<stdio.h>
int main ()
{
	int Age;
	float Income;
	
	printf("Enter your age: ");
	scanf("%i", &Age);
	
	printf("Enter your monthly Income: ");
	scanf("%f", &Income);
	
	if(Age >=30 && Income >=40000)
	{
		printf("Congratulations you qualify for the loan");
	}
	else
	{
		printf("unfortunately you don't qualify for the loan");
	}
	return 0;
}