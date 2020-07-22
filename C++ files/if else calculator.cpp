#include<iostream>
#include<windows.h>
using namespace std;
int main()
            /* this program is made by neeraj and any complaint
        regarding this program is applicale to developer only i.e Neeraj*/
{  
    system("color f0");
    long double x,y,sub,mul,sum,div;
    
	
	char choice;
	cout<<"\t\tYOU JUST HAVE TO TYPE NUMBERS AND THEIR OPERATORS!!\n";
	cout<<"\n   Enter 1st number\t";
	cin>>x;
	cout<<"\n   Enter 2nd number\t";
	cin>>y;
	cout<<"\n   Enter your choice +  - * / \t";
	cin>> choice;
	if (choice == '+')
	{
		sum=x+y;
		cout<<"\n\t"<<sum<<"\n";
	}
	else if(choice == '-')
	{
		sub=x-y;
		cout<<"\n\t"<< sub<<"\n";
	}
	else if(choice == '*')
	{
		mul=x*y;
		cout <<"\n\t"<<mul<<"\n";
	}
	else if(choice == '/')
	{
		div=x/y;
		cout <<"\n\t"<< div<<"\n";
	}
	
	
	 return 0;
	 }
