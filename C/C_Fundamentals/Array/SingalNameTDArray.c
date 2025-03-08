# include<stdio.h>

int main()
{
   char name[2][20];      // { "taif", "khan" }     or  { {'t','a','i','f','\0'}, {'k','h','a','n','\0'} }                                                                                                                                (we will get this from i=0 and then if a space is not given thn i=1's scanf wont consume it)

   for(int i=0;i<2;i++)
   {
    scanf("%[^\n]",&name[i]);
    getchar(); // pr spave before %[]
   }


   for(int i=0;i<2;i++)
   {
    printf("\nOutput is: %s",name[i]);
   }

    return 0;
}