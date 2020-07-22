# include <iostream>
#include  <stdio.h>
#include  <conio.h>
using namespace std;

int main()
{
    char op;
    float x,y;

    cout << "Enter operator either + or - or * or ,: ";
    cin >> op;

    cout << "Enter two operands: ";
    cin >> x >> y;

    switch(op)
    {
        case '+':
            cout << x+y;
            break;

        case '-':
            cout << x-y;
            break;

        case '*':
            cout << x*y;
            break;

        case ',':
            cout << x/y;
            break;
        
        default:
            // If the operator is other than +, -, * or /, error message is shown
            cout << "Error! operator is not correct";
            break;
    }

    getch();
}
