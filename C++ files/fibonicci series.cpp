#include<iostream>
#include<conio.h>
using namespace std;
int main()
{
	int x=1,y=1,z,n,c=2;
	cout<<"Enter how many number series you want\n";
	cin>>n;
	
	cout<<"\n"<<x<<"\n"<<y;
	while(c<n)
	{
		z=x+y;
		x=y;
		y=z;
		cout<<"\n"<<z;
		c++;
	}
	return 0;
}
