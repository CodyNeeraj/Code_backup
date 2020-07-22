class Array
{
    public static void main(String[] args)
    {
		int i,n=20;//n is te total no of elements in the array
		int a[] = new int [n]; //object of the array of integer type
			for ( i=0 ; i<n ; i++ ) //loop for assigning the values of array
			{
				
				a[i]=i+1; //incrementing the value to plus 1 till loop
			}
			
			for ( i=0 ; i<n; i++ )
			{
				/* if(a[i] == 2 || a[i] == 5) //jumping of values in loop
				{
					continue;
					//break; //to brak the loop for this condition
				}
				else
				{
					System.out.println("arr at "+i+("th postion is ")+a[i]);
				} */
				System.out.println("arr at "+i+("th postion is ")+a[i]);
			}
			
			System.out.println("that how 1D array works !");
	
	}
}

