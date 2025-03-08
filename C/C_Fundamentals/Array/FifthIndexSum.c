#include <stdio.h>

int main()
{
    int first[10] =  {1, 2, 3, 4, 5, 4, 7, 11, 40, 50};
    int second[10] = {1, 2, 3, 4, 5, -2, 7, 11, 40, 50};
    int third[10] =  {1, 2, 3, 4, 5, 3, 7, 11, 40, 50};
    int sum;

    sum = first[5] + second[5] + third[5];
    printf(" Sum is: %d ", sum);

    return 0;
}










// int main()
// {
//     int first[10] =  {1, 2, 3, 4, 5, 4, 7, 11, 40, 50};
//     int second[10] = {1, 2, 3, 4, 5, -2, 7, 11, 40, 50};
//     int third[10] =  {1, 2, 3, 4, 5, 'a', 7, 11, 40, 50};
//     int sum;

//     sum = first[5] + second[5] + third[5];  //  99, a takes ascii value
//     printf(" Sum is: %d ", sum);

//     return 0;
// }