#include<iostream>
#include<conio.h>
using namespace std;
int main()
{
	int x,y;
	void swap(int &,int &);
	x=10;
	y=20;
	swap(x,y); 
	cout<<"x="<<x;
	cout<<"y="<<y;
	getch();
}
void swap(int &a,int &b)
{
int c;
c=a;
a=b;
b=c;

	
}

