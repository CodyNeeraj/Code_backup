import java.util.Scanner;
import java.util.InputMismatchException;

class string
{
	public static void main(String [] args) 
	{
		String str = "abstraction, ambiguous, arithmetic , backslash , bitmap";
		//String vars can be altered
		String name [] = str.split( "," ); //putting adjacent strings in array name
		System.out.println("Enter the array index which you want to find hereby ");
		Scanner scr=new Scanner(System.in);
		int i = scr.nextInt();
		do
		{
		if(i>=name.length)//lenght of array here is a[5] or 4
		{
			System.out.println("You entered a Bigger size enter again");
			i = scr.nextInt();
		}
		
		else if(i<0)//negative index not allowed
		{
			System.out.println("You entered a Smaller size enter again");
			i = scr.nextInt();
		}
		
		}while(i>=name.length | i<0);
		System.out.println("string at  a "+i+" is " + name[i]);
	}
}