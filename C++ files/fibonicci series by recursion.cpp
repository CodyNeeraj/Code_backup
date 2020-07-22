#include<iostream>
#include<conio.h>
using namespace std;
int main()
{
	for(;;)
	
	{
	unsigned long int a[2000];
	int i;
	int l;
	cout<<" Enter a limit upto which you want output\n\n";
	cin>>l;
	
	for(i=1;i<=l;i++)
	{
		if(i<=1)
		{
			a[i]=1;
		}
		else
		{
			a[i]=a[i-1]+a[i-2]	;
		}
    
		cout<<"\n"<<i<<"th is "<<a[i];	
		
	}
	
		cout<<"\n\nDO you wanna stop this program enter Y\n";
		char x;
		cin>> x;
		if(x=='y'||x=='Y')
		break;
}
	
	return 0;
}
