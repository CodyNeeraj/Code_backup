//Program to count the number of objects in the array using the static counter inh the constructor
//pls note the java files having class structur i.e this file can be saved with different names also
 class objectCounter
{
	static int id = 0; //resides the value of the variable in memory
	objectCounter() //default constructor
	{
		System.out.print("Default constructor called !");
		id++; //increenting static counter of variable id
	}
	
	static public void main(String ... args)//Varargs
	{
		int a[] = new int [21];
		for(int i=1;i<21;i++)
		{
			objectCounter obj = new objectCounter();
			System.out.println(id+" times");//calling counter var id
		}
	}
}