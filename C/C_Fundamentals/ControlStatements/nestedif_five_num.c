#include <stdio.h>

int main()
{
  int num1;
  int num2;
  int num3;
  int num4;
  int num5;

  printf("Enter numbers: ");

  scanf("%d", &num1);
  scanf("%d", &num2);
  scanf("%d", &num3);
  scanf("%d", &num4);
  scanf("%d", &num5);

  printf("\nEnter num 1: %d", num1);
  printf("\nEnter num 2: %d", num2);
  printf("\nEnter num 3: %d", num3);
  printf("\nEnter num 4: %d", num4);
  printf("\nEnter num 5: %d", num5);

  if (num1 > num2)
  {
    if (num1 > num3)
    {
      if (num1 > num4)
      {
        if (num1 > num5)
        {
          printf("\nNumber 1 is largest: %d", num1);
        }
        else
        {
          printf("\nNumber 5 is largest: %d", num5);
        }
      }
      else // num4>num1
      {
        if (num4 > num5)
        {
          printf("\nNumber 4 is largest: %d", num4);
        }
        else
        {
          printf("\nNumber 5 is largest: %d", num5);
        }
      }
    }
    else // num3>num1
    {
      if (num3 > num4)
      {
        if (num3 > num5)
        {
          printf("\nNumber 3 is largest: %d", num3);
        }
        else
        {
          printf("\nNumber 5 is largest: %d", num5);
        }
      }
      else // num4>num3
      {
        if (num4 > num5)
        {
          printf("\nNumber 4 is largest: %d", num4);
        }
        else
        {
          printf("\nNumber 5 is largest: %d", num5);
        }
      }
    }
  }
  else // num2 >num1
  {
    if (num2 > num3)
    {
      if (num2 > num4)
      {
        if (num2 > num5)
        {
          printf("\nNumber 2 is largest: %d", num2);
        }
        else
        {
          printf("\nNumber 5 is largest: %d", num5);
        }
      }
      else // num4>num2
      {
        if (num4 > num5)
        {
          printf("\nNumber 4 is largest: %d", num4);
        }
        else
        {
          printf("\nNumber 5 i largest: %d", num5);
        }
      }
    }
    else // num3>num2
    {
      if (num3 > num4)
      {
        if (num3 > num5)
        {
          printf("\nNumber 3 is largest: %d", num3);
        }
        else
        {
          printf("\nNumber 5 is largest: %d", num5);
        }
      }
      else // num4>num3
      {
        if (num4 > num5)
        {
          printf("\nNumber 4 is largest: %d", num4);
        }
        else
        {
          printf("\nNumber 5 is largest: %d", num5);
        }
      }
    }
  }

  return 0;
}