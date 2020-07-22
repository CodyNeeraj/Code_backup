//program to convert decimel to octal
#include<iostream>
using namespace std;
int main()

{
	for(;;)
	{
		
	int num,rem;
	cout<<"\nPlease enter a no=>\t";
	cin>>num;
	
	while(num >= 8)
	{
	rem = num % 8;
    num = num / 8;
    
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
