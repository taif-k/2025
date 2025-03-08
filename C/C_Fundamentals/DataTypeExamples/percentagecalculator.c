#include <stdio.h>

int main()
{
    int hindimarks;
    int engmarks;
    int scimarks;

    printf("Enter Hindi Marks: ");
    scanf("%d", &hindimarks);
    printf("Enter English marks: ");
    scanf("%d", &engmarks);
    printf("Enter science marks: ");
    scanf("%d", &scimarks);
    float percentage = (float)(hindimarks + engmarks + scimarks) / 300 * 100;
    printf("Percentage is: %f",percentage);

    if (percentage >= 60)
    {
        printf("\nFirst Divison");
    }
    else
    {
       if(percentage>=45)
       {
       printf("\nSecond Divison");
       }
       else 
       {
        if(percentage>=33)
        {
            printf("\nThird Divison");
        }
        else 
        {
            printf("\nFailed, Try again");
        }
       }
    }
    return 0;
}