#include<iostream>
using namespace std;
int main()
{
	int d,m,y,x,num1,num2,num3,sum1=0,sum2=0,sum3=0;
	cout<<"\n---------------------- Astrologer Pro by Neeraj Ver:1.00 -----------------------";
	cout<<"\n Enter date (range 1 - 31) ";
	cin>>d;
	
	while(d>=32)
	{
	cout<<"\nThere is not such a date don't think I'm fool\n\nEnter your date again ";
	cin>>d;	
	}
	if(d>=10)
	{
		
		num1=d;
		while (num1!= 0)
		{
			sum1=sum1+num1%10;
			num1=num1 /10;
		}
		
	}
	
	
	cout<<"\n\n Now enter Month Number as shown\n\n 1. January\n 2. February\n 3. March\n 4. April\n 5. May \n 6. June \n 7. July \n 8. August \n 9. September \n10. October \n11. November \n12. December           ";
	cin>>x;
	while(x>=13)
	{
		cout<<"\n\nEnter within range........";
		cin>>x;
	}
	switch(x)
	{
		case 1:
	    cout<<"\nYou entered January\n";
	    m=1;
	    break;
	    
	    case 2:
	    cout<<"\nYou entered February\n";
	    m=2;
	    break;
	    
	    case 3:
	    cout<<"\nYou entered March\n";
	    m=3;
	    break;
	    
	    case 4:
	    cout<<"\nYou entered April\n";
	    m=4;
	    break;
	    
	    case 5:
	    cout<<"\nYou entered May\n";
	    m=5;
	    break;
	    
	    case 6:
	    cout<<"\nYou entered June\n";
	    m=6;
	    break;
	    
	    case 7:
	    cout<<"\nYou entered July\n";
	    m=7;
	    break;
	    
	    case 8:
	    cout<<"\nYou entered August\n";
	    m=8;
	    break;
	    
	    case 9:
	    cout<<"\nYou entered September\n";
	    m=9;
	    break;
	    
	    case 10:
	    cout<<"\nYou entered October\n";
	    m=10;
	    break;
	    
	    case 11:
	    cout<<"\nYou entered November\n";
	    m=11;
	    break;
	    
	    case 12:
	    cout<<"\nYou entered December\n";
	    m=12;
	    break;
	    
	    default:
	    cout<<"There is not a month like that !!!!!";
	    
	}
	if(m>=10)
	{
		
		num2=m;
		while (num2!= 0)
		{
			sum2=sum2+num2%10;
			num2=num2 /10;
		}
	}
	
	cout<<"\n\nNow enter your birth year\t";
	cin>>y;
	
		num3=y;
		while (num3!= 0)
		{
			sum3=sum3+num3%10;
			num3=num3 /10;
		}
	
	cout<<"\n\nBirth date is\t"<<d<<"/"<<m<<"/"<<y<<"\n\n";
	
	
	if(d>=10)
	{
	int a = sum1+m+sum3;
	cout<<"\n Your Bhagyaank is\t"<<a;
	cout<<"\n Your Mulyaank is\t"<<sum1;
	}
	else if(m>=10)
	{
		int a =d+sum2+sum3;
		cout<<"\n Your Bhagyaank is\t"<<a;
		cout<<"\n Your Mulyaank is\t"<<d;
	}
	
	else if(m , d>=10 )
	{
		int a =sum1+sum2+sum3;
		cout<<"\n\nsorry but under development may be corrected in the next update stay tuned.........";
	    //	sorry but under development may be corrected in the next update stay tuned.........
	}
	else
	{
		int a =d+m+sum3;
		cout<<"\n Your Bhagyaank is\t"<<a;
		cout<<"\n Your Mulyaank is\t"<<d;
	}
	
	
return 0;
}
