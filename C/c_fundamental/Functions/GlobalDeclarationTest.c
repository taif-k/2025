#include <stdio.h>

void sum()
{

    printf("\nSum is: %d ", a + b);
}

int a = 2;
int b = 2;                                                                                                                                 // a and b are declared outside main, so they are accesible from the line they are declared and below till end
                                                                                                                                           // thats why void sum(){} will have an error
// void sum();
int main()
{
    sum();
    return 0;
}
