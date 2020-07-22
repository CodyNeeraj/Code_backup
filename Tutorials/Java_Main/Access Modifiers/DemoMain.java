
public class DemoMain 
{
	public static void main(String[] args)
	{
		Student s = new Student();
		s.rollno=9;
		s.marks=99;
		s.age=30;
		System.out.println(" rollno is "+s.age);
	}
}
class Student
{
	int rollno;
	int marks;
	int age;
}