import java.util.Scanner;
class ex
{
	public static void main(String [] args)
	{
		Scanner scr = new Scanner(System.in);
		
		int arr[] = {0,5,4,8,7,8};//can be modified in unlimited number of elements
		try
			{
				int i = scr.nextInt();
				System.out.println("Value at index "+i+" is "+arr[i]);
			}
			
		catch(ArrayIndexOutOfBoundsException e)
		{
			System.out.println("array index exception !");//cheked exception
		}
		
		catch(Exception e)
		{
			System.out.println("saare exceptions a gae bro! ");
		}
	}
}