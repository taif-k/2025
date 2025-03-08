#include <stdio.h>

int main()
{
    int number[7] = {9, 4, 1, 7, 4, 1, 1};
    int number2[7] = {0};
    int match = 0;
    int counter = 0;
    int flag = 0;

    //                                           [0] [1] [2] [3] [4] [5] [6]
    for (int i = 0; i < 7; i++) //                9   4   1   7   6   1   1
    {
        for (int j = i + 1; j < 7; j++)
        { //           2  ==        5/6
            if (number[i] == number[j])
            {
                match = 1;
                for (int y = 0; y < 7; y++)
                {
                    if (number[i] == number2[y])
                    {
                        flag = 1;
                    }
                }
            }
        }
        if (match == 1 && flag == 0)
        {
            number2[counter] = number[i];
            counter++;
        }
        match = 0;
        flag = 0;
    }

    for (int z = 0; z < counter; z++)
    {
        printf(" %d ", number2[z]);
    }
    return 0;
}