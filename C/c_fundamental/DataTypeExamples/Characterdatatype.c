#include<stdio.h>

int main()
{

 char status;
 printf("Enter 'Y' to see Salary : %c",status);
 scanf("%c",&status);

 float yearly_salary = 500000;
 float monthly_salary = yearly_salary/12;
 float perday_salary = monthly_salary/30;

 printf("\nYearly salary is: %f",yearly_salary);
 printf("\nMonthly salary is: %f",monthly_salary);
 printf("\nPer Day salary is: %f",perday_salary);
 return 0;

}