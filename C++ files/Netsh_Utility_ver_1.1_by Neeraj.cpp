#include<iostream>
#include<windows.h>
using namespace std;

void drivercheck();//to check driver supports or not?
void wireless_Starter();//to start the hotspot
void wireless_Stopper();//to stop the hotspot
void wireless_restarter();//to restart the hotspot

int main() 
{ 
int choice_of_option,exit_button;
char drivercode_controller = 'y';
while(drivercode_controller == 'y' || drivercode_controller == 'Y')//for refreshing the main
{
	system("cls");
	cout<<"\n\t\t\t***Welcome to NETSH Utility***\n\n";
	cout<<"Press [1] (Important) Check If your system supports Hotspot connectivity ?\n";
	cout<<"Press [2] Start Wireless Hotspot NOW ?\n";
	cout<<"Press [3] Stop the Wireless Hotspot right now ?\n";
	cout<<"Press [4] Restart the Wireless Hotspot ?\n";
	cout<<"Press [5] Exit now?\n\t";
	cin>>choice_of_option;

switch(choice_of_option)
{
	case 1:
	drivercheck();
	break;
	
	case 2:
	wireless_Starter();
	break;
	
	case 3:
	wireless_Stopper();
	break;
	
	case 4:
	wireless_restarter();
	break;
	
	case 5:
	system("cls");
	cout<<"Are you sure to EXIT ?\nPress [1] for YES \nPress [2] for NO\n\t";
	cin>>exit_button;
		switch(exit_button)//for exiting as the choice of user
	 	 {
			case 1:
			system("cls");
			return 0;
			break;
		
			case 2:
			main();
			break;
		
			default:
			cout<<"Wrong Option !\n";
			main();
		
	     }
	     
	break;
	// switches ended here !
	default:
	cout<<"Invalid option !\n";
	cout<<"Press [y] or [Y] to start again";
	cin>>drivercode_controller;
		
}
	//system("Pause");
	system("cls");
	cout<<"\n\n\t\t***THANKS FOR USING THIS APP BY NEERAJ***";	
}

}
   
   //driver codes for each above functions
	void drivercheck() 
	 {
	 	cout<<"It is must to check that your system supports Hotspot functionality or not ?\nChecking right now, Look for the HOSTED_NETWORK_SUPPORTED is Marked as YES !\nIf yes than congrats you can use this program seamlessly !!!\n";
		system("cls");
		system("C:\\Windows\\System32\\netsh wlan show driver");
		//do not even try to edit the above code due to fact that this can render your system unusable permanently !! 
		system("Pause");
 	 }
	void wireless_Starter()
	 {
	 	system("cls");
	 	system("C:\\Windows\\System32\\netsh wlan set hostednetwork mode=allow ssid=UserAlpha  key=9316203676 ");
		system("C:\\Windows\\System32\\netsh wlan start hostednetwork");
		system("Pause");
		/* char hostname[19];
		char passkey[25];
		char passchoice; //user input for suing password or not?
		
		cout<<"Specify the SSID (Hostname name)\n";
		cin.get(hostname,25);
		cout<<"If you want to secure it with password then type Y/N \n";
		cin>>passchoice;
			if (passchoice=='n' || passchoice=='N')
			{
				cout<<"Well this is not recommended to do so !";
				cout<<"\n Starting your Hotspot..... named"<<hostname;
				system("C:\\Windows\\System32\\netsh wlan set hostednetwork mode=allow ssid=UserAlpha");
				system("C:\\Windows\\System32\\netsh wlan start hostednetwork");
				//this driver code needs debugging coz i don't know how to do use manual coomands as input parameters from primative types !
				//also the default hostnmae is set Useralpha always due to this problem !!
			}
			else if(passchoice=='y'|| passchoice=='Y')
			{
			cout<<"Enter the password to secure it !\nYour passkey must be strong and minimum eight words in length.\n"; 
			cin.getline(passkey,25);
			cout<<"\n Starting your Hotspot.....named "<<hostname<<" password.. "<<passkey;
			system("C:\\Windows\\System32\\netsh wlan set hostednetwork mode=allow ssid=UserAlpha  key=9316203676 ");
			system("C:\\Windows\\System32\\netsh wlan start hostednetwork");
			system("Pause");
			//specify an ssid name and password acc to the user choice !
			//this ssid name and password will be set by default if no user requested to change it !
		}
		
	*/		
	}
	void wireless_Stopper()
     {
     		system("cls");
			cout<<"Stopping your hotspot right now.....\n";
			system("C:\\Windows\\System32\\netsh wlan stop hostednetwork");
			system("Pause");
			//code to stop the hostednetwork
	 }
	void wireless_restarter()
	 {
	 		system("cls");
			cout<<"Restarting your connection right now.....\n";
			system("C:\\Windows\\System32\\netsh wlan stop hostednetwork");
			Sleep(2500);//for system cooling time
			system("C:\\Windows\\System32\\netsh wlan start hostednetwork");
			system("Pause");
			//code to restart the hostednetwork
	 }
