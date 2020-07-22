#include<iostream>
#include<conio.h>
#include<stdio.h>
using namespace std;
int main()

{
	for(;;)
	{
		
	int num,rem;
	cout<<"\nPlease enter a no=>\t";
	cin>>num;
	
	while(num !=0)
	{
	rem=num%2;
    num/=2;
    
	cout<<rem;
	}
	
	cout<<endl<<"DO you want to run the program again ?"<<endl;
	char ch;
	cin>>ch;
	if(ch== 'y' || ch== 'Y')
		continue;
	else
		break;
	}
	
	system("pause");

return 0;

}
