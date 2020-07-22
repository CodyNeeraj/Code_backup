#include <iostream>
#include <conio.h>
using namespace std;
int main()
{
	
	for(;;)
{
	
	int x;
	float temp,c,f;
	char ch;
	cout<<"Welcome to my temperature converter v2.6\n\n";
	cout<<"Enter the following according to your needs!\n\n";
	cout<<" 1 -> Celsius to Fahrenheit\n";
	cout<<" 2 -> Fahrenheit to Celsius \t";
	cin>> x;
	switch (x)
	{
		case 1:
			cout<<"  \nEnter temperture in Celsius \n";
			cin>> c;
			temp=(1.8*c)+32;
			cout<<"The answer is "<< temp<< " degree fahrenhiet\n";
			break;
			case 2:
			cout<<"  \nEnter temperture in Fahrenhiet\n";
			cin>> f;
			temp=(f-32)*0.555;
			cout<<"The answer is "<< temp<< " degree celsius\n";
			break;
				
		
		
	}
		cout<<"\n\nDO you wanna stop this program enter Y\n";
		
		cin>> ch;
		if(ch=='y'|| ch=='Y')
		break;
	return 0;
	system("pause");
}


}

	
	

