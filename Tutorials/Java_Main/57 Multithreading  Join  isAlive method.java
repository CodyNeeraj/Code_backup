
 class ThreadDemo 
{
	public static void main(String[] args) throws Exception
	{
		Thread t1 = new Thread(() ->
		{
			for(int i=1;i<=20;i++)
			{
				System.out.println("Thread 1 is Executing ");
				try {Thread.sleep(1000); } catch(Exception e){}
			}
		});
		Thread t2 = new Thread(() ->
		{
			for(int i=1;i<=20;i++)
			{
				System.out.println("Thread 2 is Executing");
				try {Thread.sleep(1000); } catch(Exception e) {}
			}
		 });
		
		t1.start();
		//try {Thread.sleep(10); } catch(Exception e) {}
		t2.start();
		try {Thread.sleep(10); } catch(Exception e) {}
		
		t1.join();
		t2.join();
		
		
		System.out.println("Thread 1 is alive : "+t1.isAlive());
		System.out.println("Thread 2 is alive : "+t2.isAlive());
		
		System.out.println("Bye");
	}
}