#include<stdio.h>

int main()
{

    char name[20];   //[t][a][i][f][space][k]   taif k

    printf("Enter name: ");
    scanf(" %[^\n]",&name);   // scanf reads "space" and breaks the line as soon it gets "space" and gets to next line of the program -> taif[space]k output -> taif
    printf("%s",name);
    printf("\nHello");

    return 0;
}
//p enter name
//s taif \n k
//s k (coming from ln 16 bcuz of \n)
//p  hello
//p taif k