#include <stdio.h>

int main()
{

    int arr1[5] = {5, 0, 0, 2, 1};
    int arr2[5] = {2, 5, 6, 0, 7};
    int arr3[10]; //  5 3 2 1
    int match = 0;
    int flag = 0;
    int counter = 0;

    for (int i = 0; i < 5; i++)
    { //    1
        for (int j = i + 1; j < 7; j++)
        { //    2
            if (arr1[i] == arr1[j])
            {
                flag = 1;
                for (int k = 0; k < 10; k++)
                {
                    if (arr1[i] == arr3[k])
                    {
                        match = 1;
                    }
                }
            }
            else if (arr1[i] != arr1[j])
            {
                flag = 2;
                for (int k = 0; k < 10; k++)
                {
                    if (arr1[i] == arr3[k])
                    {
                        match = 2;
                    }
                }
            }
        }

        if (flag == 1 && match == 0)
        {
            arr3[counter] = arr1[i];
            counter++;
        }

        if (flag == 2 && match == 0)
        {
            arr3[counter] = arr1[i];
            counter++;
        }
        match = 0;
        flag = 0;
    }

    for (int i = 0; i < 5; i++)
    { //    1
        for (int j = i + 1; j < 7; j++)
        { //    2
            if (arr2[i] == arr2[j])
            {
                flag = 1;
                for (int k = 0; k < 10; k++)
                {
                    if (arr2[i] == arr3[k])
                    {
                        match = 1;
                    }
                }
            }
            else if (arr2[i] != arr2[j])
            {
                flag = 2;
                for (int k = 0; k < 10; k++)
                {
                    if (arr2[i] == arr3[k])
                    {
                        match = 2;
                    }
                }
            }
        }

        if (flag == 1 && match == 0)
        {
            arr3[counter] = arr2[i];
            counter++;
        }

        if (flag == 2 && match == 0)
        {
            arr3[counter] = arr2[i];
            counter++;
        }
        match = 0;
        flag = 0;
    }

    for (int k = 0; k < counter; k++)
    {
        printf(" %d ", arr3[k]);
    }

    // int num[50];

    // for (int i = 0; i < 50; i++)
    // {
    //     num[i] = i;
    //     printf("\n%d", num[i]);

    // }

    // for (int i = 0; i < 7; i++)
    // {
    //     printf("\n%d", num[0]=9);
    //     printf("\n%d", num[1]=10);
    //     printf("\n%d", num[2]=11);
    //     printf("\n%d", num[3]=12);
    //     printf("\n%d", num[4]=8);
    //     printf("\n%d", num[5]=9);
    //     printf("\n%d", num[6]=10);
    // }

    // for(int i=0;i<7;i++)
    // {
    //     printf("\n%d",num[i]);
    // }

    // int x = 0;
    // printf("%d", x++);

    // int numbers[50]; // [49] [50][51]..........[99]

    // for (int i = 0; i < 50; i++)
    // {
    //     numbers[i]=i;
    //     printf("\n%d", numbers[i]);
    // }

    return 0;
}
