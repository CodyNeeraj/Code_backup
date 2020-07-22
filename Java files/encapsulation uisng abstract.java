//package java;

import java.util.Scanner;
//import java

/**
 *
 * @author Neeraj
 */
class Java
{
    public static void main(String[] args) 
    {
   
		int counter=0;
		do
		{
		System.out.println("Enter a no which you want to Set as no !");
		c obj1 =new c();
		Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        obj1.setNo(n);
		//System.out.println("the number entered by you is "+obj1.getNo());
        //obj1.getNo();
		
        System.out.println("Enter a name to which you want to set as name !");
        c obj2 =new c();
		Scanner sc2 = new Scanner(System.in);
        String name =sc2.nextLine();
        obj2.setName(name);
		//System.out.println("The string entered by you is "+obj2.getName());
        //obj2.getName();
		System.out.println(obj2.getName()+ " The number entered by you is " +obj1.getNo());
		new c().neeraj();
        new c().moma();//anonymous object
		
		
		System.out.println("enter 1 key for exit or any other key to continue....");
		Scanner sc3 =new Scanner(System.in);
		counter= sc3.nextInt();
		/* BufferedReader br1 = new BufferedReader(new InputStreamReader(System.in));
		counter = br1.IntegerParsetoint(); */
		}while(counter!=1);
        
        
        
    }
    
}
abstract class A
{
    private int no;
    private String name;

    public int getNo()
    {
        return no;
    }

    public void setNo(int no)
    {
        this.no = no;
    }

    public String getName()
    {
        return "Hello " +name;
    }

    public void setName(String name)
    {
        this.name = name;
    }  
    
    public abstract void neeraj();   
}
 class B extends A
{

    @Override
    public void neeraj() 
    {
        System.out.println("Abstarct from A is executed in B !");
    }
    
}
 class c extends B 
{

    public void moma()       
    {
        System.out.println("Class C !");
    }
    
}

