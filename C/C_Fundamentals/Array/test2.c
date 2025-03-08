#include <stdio.h>

int main()
{                                                                        //  0123  0123
    char name1[2][5]; //= {{'t', 'a', 'i', 'f'}, {'k', 'h', 'a', 'n'}};  //   taif  khan
// take column size more to store name plus null terminator              //    0      1
    for(int i=0;i<2;i++)
    {
        scanf(" %[^\n]",&name1[i]);
    }   
    
    for(int i=0;i<2;i++)
    {
        printf("%s\n",name1[i]); 
    }
    
    return 0;
}