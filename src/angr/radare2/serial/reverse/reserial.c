/*
Reverse Engineered serial

This is a mini simplified version EZVA should print success
I have tried to create the C code that would look like the reversed binary
*/
# include <stdio.h>
# include <string.h>

int main()
{
    char *input;
    printf("Enter input: ");
    scanf("%s", input);

    if (strlen(input) != 4) {
        return 0;
    }
    if (input[0] != 69) {
        return 0;
    }
    if(input[0] + input[3] != 155) {
        return 0;
    }
    if(input[1] != 90) {
        return 0;
    }
    if(input[1] + input[2] != 155) {
        return 0;
    }
    printf("success!\n");
    return 0;
}