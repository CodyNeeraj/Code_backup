#include<iostream>
using namespace std;
class daddy
{
	private:
		
		int no;
		char name[30];
		float salary;
		
	public:
		
	void get_data()
	{
		cout<<endl<<"Enter your no. please"<<endl;
		cin>>no;
		cin.ignore();
		cout<<endl<<"Enter your name please"<<endl;
		cin.get(name,30);
		cin.ignore();
		cout<<endl<<"Enter your salary please"<<endl;
		cin>>salary;
		cin.ignore();
	}	
		
	void display_data()
	{
		cout<<endl<<"Your number is:\t";
		cout<<no;
		cout<<endl<<"User name is:  \t";
		cout<<name;
		cout<<endl<<"Your salary is:\t";
		cout<<salary<<endl;
			
	}	
		
		daddy()
		{
			cout<<"hey its me a constructor im called in this program"<<endl;	
		}
		
		~daddy()
		{
			cout<<"hey its me a destructor im called in this program"<<endl;	
		}
};
class son : public daddy
{
	public:
	son()
	{
	cout<<"\nderived class constructor called\n";
	}
};
int main()
{
son o1,o2,o3,o4;

cout<<endl<<"Enter details for person 1";
o1.get_data();
cout<<endl<<"Enter details for person 2";
o2.get_data();
cout<<endl<<"Enter details for person 3";
o3.get_data();
cout<<endl<<"Enter details for person 4";
o4.get_data();

o1.display_data();
o2.display_data();
o3.display_data();
o4.display_data();

system("pause");
return 0;
}
