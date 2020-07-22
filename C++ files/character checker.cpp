#include<iostream>
using namespace std;
int main()
{
char ch;
cout<<"Enter a keyword\t";
cin>>ch;
	if (ch>=65 && ch<=90)
	{
		cout<<"\nYou entered a capital alphabet\n";
	}
	
	else if (ch>=48 && ch<=57)
	{
		cout<<"\nYou entered a number\n";
	}
	
	else if (ch>=97 && ch<=122)
	{
		cout<<"\nYou entered a small alphabet\n";
	}
	else
	{
		cout<<"\nYou entered a symbol\n";
	}
	
	return 0;
}
