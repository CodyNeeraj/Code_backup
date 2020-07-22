/*Program to print table of any input number*/

#include<stdio.h>
#include<conio.h>
int main()
{
int num,i,mul,range;
i=1;


printf("\nKoi number dabakar enter kare:- ");
scanf("%d",&num);
printf("Enter your range now!!");
scanf("%d",&range);

  //for clear screen

printf("\n-------------------------------");
printf("\nNumber entered is: %d",num);
printf("\n-------------------------------");
printf("\nTable of %d is",num);
printf("\n---------------------------------------\n");

while(i<=range)
{
if(num==0)
{
printf("\nZero entered");
break;
}
mul=num*i;
printf("\n %d x %d = %d ",num,i,mul);

i++;
}

printf("\n--------------------------------------");


getch();
} 
