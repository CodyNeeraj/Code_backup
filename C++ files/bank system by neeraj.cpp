#include <iostream>
#include <windows.h>
using namespace std;
int f1() {
	
	cout << "			  658148944848 \n\n 		  	is OTP ko note karle";
	Beep(1100,800);
	Beep(0,500);
	Beep(1100,800);
	
}


int main() {
	char input = 0;
	
	cout << "\n	   	     Bank OTP system me apka swagat hai !!.\n\n";
	cout << "     	     Press x to quit any time or press E for further details.\n";	
	while("!=0") {
		cin>>input;
		if(input == 'a') {
			f1();
			} 
			else if(input =='y')
			 {
			cout<<"         apka password load ho raha hai kripya pratiksha kare !!\n\n";
			Beep(0,5000);
			 f1();
	       	 }
	       	 else if(input =='n')
			 {
			cout<<"   		Apne parakirya rok di hai !!\n\t\t x daba kar band kare\n";
	       	 }
	       	 else if(input =='x')
			 {
			return 0;
	       	 }
	       	 else if(input =='e')
			 {
			cout<<"		   Apne E dabaya hai kya hum apka OTP pradan kare ?\n      				   Apna utar de\n\n      				   Y se ha hai\n      				   N se na hai \n";
	       	 }
	       	 
	}


}
