
//             0%          5%            20%              30%
//         0        2.5L           5L              10L
//                         12500        100000

#include <stdio.h>

int main()
{
  int income;
  printf("Enter Income: ");
  scanf("%d", &income);
  
  if (income <= 250000)
  {
    printf("No need to pay Tax");
  }
  else
  {
    if (income <= 500000)
    {
      float tax1 = (income - 250000) * 5 / 100;
      printf("Tax above 2.5L till 5L is: %f", tax1);
    }
    else
    {
      if (income <= 1000000)
      {
        float tax2 = (income - 500000) * 20 / 100 + 12500;
        printf("Tax above 5L till 10L: %f", tax2);
      }
      else
      {
        float tax3 = (income - 1000000) * 30 / 100 + 100000 + 12500;
        printf("Tax above 10L is: %f", tax3);
      }
    }
  }
  // int income;
  // printf("Enter Income: ");
  // scanf("%d", &income);

  // if(income<=250000)
  // {
  //  printf("No need to pay Tax");
  // }
  // else if(income<=500000)
  // {
  //   float tax1 = (float)(income - 250000) * 5/100 + 0;
  //   printf("Tax is: %f",tax1);
  // }
  // else if(income<=1000000){
  //  float tax2 = (float)(income - 500000) * 20/100 + 12500 + 0;
  //  printf("Tax is: %f",tax2);
  // }
  // else
  // {
  //     float tax3 = (float)(income - 1000000) * 30/100 + 100000 + 12500 + 0;
  //     printf("Tax is: %f",tax3);
  // }
  return 0;
}