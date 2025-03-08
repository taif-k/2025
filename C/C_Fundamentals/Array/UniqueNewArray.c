#include <stdio.h>

int main()
{
    int array1[5] = {1,2,2,0,0};
    int array2[5]={2,18,19,20,1};
    int newarray[10]; //    {1,2,0,3,20,50 }  
    int counter = 0;
    int match=0;

    for (int i = 0; i < 5; i++)  //20
    {
        for (int k = 0; k < counter; k++)
        {
            if (array1[i] == newarray[k])
            {
                match = 1;
                break;
            }
        }

        if (match == 0)
        {
            newarray[counter] = array1[i];
            counter++;
        }

        match = 0;
        for (int k = 0; k < counter; k++)
        {
            if (array2[i] == newarray[k])
            {
                match = 1;
                break;
            }
        }

        if (match == 0)
        {
            newarray[counter] = array2[i];
            counter++;
        }
        match=0;
    }

    for (int z = 0; z < counter; z++)
    {
        printf(" %d ", newarray[z]);
    }

    return 0;
}