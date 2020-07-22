#include<iostream>
#include<ctime>
#include<cstdlib>
using namespace std; //this program takes the output in cpp only comment it when needed in C ,31-01-20 18:51
int main()
{
long i;
clock_t start = clock();
for(i=1;i<1000000000;i++)
{
	
}
clock_t end = clock();
double  elapsed_secs= double (end - start)/ CLOCKS_PER_SEC;
cout<<"done using c++ in: ";
cout<<elapsed_secs;
cout<<"secs";
cout<<endl;
}

/*#include<time.h>  //and this program is in c language use it when needed in C
#include<stdio.h>
int main()
{
	long i;
	clock_t start = clock();
	for(i=1;i<1000000000;i++);
		
clock_t end = clock();
double  elapsed_secs= (double)(end - start)/ CLOCKS_PER_SEC;
printf("done in %f seconds \n",elapsed_secs);
return 0;
}*/
