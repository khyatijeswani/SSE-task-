#include <stdio.h>
int main()
{
    char data ;
    printf("Enter a character: " );
    scanf("%c", &data);
    if ( data>=65 && data<=90 )
        printf("Character is a capital letter");
    else if (data>=97 && data<=122)
        printf("Character is a small case letter");
    else
        printf("Character is neither a capital nor a small case letter");

}
