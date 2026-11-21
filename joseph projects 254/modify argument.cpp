#include<stdio.h>
int a,b;
int sum(int x,int y);
int main()
int sum(int x, int y)
{
	return x+y;

}
{
	int a,b;
	printf("Enter value of a and b: ");
	scanf("%i%i", &a,&b);
	printf("sum=%i",sum(a+5,b-1));
	return 0;
}