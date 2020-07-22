#include<iostream>
#include<stdio.h>
#include<conio.h>
using namespace std;
int main()
{
   
	int x,y,c,t,a,b;
	float first,temp;
	
    		cout <<"                 Enter the code in no. to convert into further\n                    But not add any decimals in your code\n\n";
    		cout<<"                   Enter 0 anytime to terminate the program\n\n";
        	cout<<"1. Kms to Miles\n";  
  	    	cout<<"2. Miles to Kms\n";
  	    	cout<<"3. Kmph to Knots\n";  
  	    	cout<<"4. Kgs to Pound\n";   
  	    	cout<<"5. Kgs to Ounce\n";  
  	    	cout<<"6. Ltrs to Gallons\n";  
			cout<<"7. Celsius to Fahreheit\n";
		    cout<<"8. Fahrenheit to Celsius\n";
			cout<<"9. Celsius to Kelvin\n";
			cout<<"10. Kelvin to Celsius\n";
			cout<<"11. Kelvin to Fahrenheit\n";
			cout<<"12. Fahrenheit to Kelvin\n\t\t\t";
  	    	cin >> y;
  	    	switch(y)
  	    	
  	      {
  	    	case 1:
  	    		cout<<"\n\nEnter kilometres\n";
  	    		cin >> t;
  	    		first=t*0.625;
  	    		cout<< first <<" Miles are in " << t <<" kms\n";
  	    		break;
  	    		
  	    	case 2:
			  cout<<"\n\nEnter Miles";
			  cin >> t;
			  first=t/0.625;
			  cout<<"There are "<< first <<"kms in" << t <<"miles\n";
			  break;
			  
			 case 3:
			 	cout<<"Enter speed in kmph\n";
			 	cin>> t;
			 	first=t*0.5;
			 	cout<< first <<" knots\n";
			 	break;
			 	
		    case 4:
			    cout<<"Enter weight in kgs\n";
			  	cin>> t;
				first=t*2.25;
				cout<< first <<" lbs\n";
				break;
				
			case 5:
			 	cout<<"Enter weight in kgs\n";
			 	cin>> t;
			 	first=t*35.3;
			 	cout<< first <<" oz\n";
			 	break;
			 	
			case 6:
			 	cout<<"Enter vol. in ltrs\n";
			 	cin>> t;
			 	first=t/3.89;
			 	cout<< first <<" Gallons\n";
			 	break;
			 	
		
            case 7:
				cout<<"\n\nEnter Celsius value\n";
				cin >> t;
				first=(1.8*t)+32;
				cout << first <<" degree fahrenhiet\n\n";
				break;
				
			case 8:
				cout <<"\n\nEnter Fahrenheit value\n";
				cin>>t;
				first=(t-32)*0.5555;
				cout << first <<" degree celsius\n\n";
				break;
				
			case 9:
				cout <<"\n\nEnter Celsius value\n";
				cin>>t;
				first=t+273.15;
				cout << first <<" degree kelvin\n\n";
				break;
		    case 10:
				cout <<"\n\nEnter Kelvin value\n";
				cin>>t;
				first=t-273.15;
				cout << first <<" degree celsius\n\n";
				break;
				
		    case 11:
				cout <<"\n\nEnter Kelvin value\n";
				cin>>t;
				first=t-273.15;
				temp=(first*1.8)+32;
				cout << temp <<" degree fahrenheit\n\n";
				break;
				
			case 12:
				cout <<"\n\nEnter Fahrenheit value\n";
				cin>>t;
				first=(t-32)*0.5555;
				temp=first+273.15;
				cout << temp <<" degree kelvin\n\n";
				break;	
		    case 0:
			return 0;
	     	}
		
	    
   
	return 0;
}
