#include<stdio.h>
int a,b;//global
int sum(int x, int y)
{
	return x+y;

}
int main()
{
	int a,b;
	printf("Enter value of a and b: ");
	scanf("%i%i", &a,&b);
	printf("sum=%i",sum(a,b));
	return 0;
}