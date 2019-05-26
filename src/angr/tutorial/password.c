#include <stdio.h>
#include <string.h>

static char password[] = "passw0rd";
int main(void) {
 char buf[20];
 printf("Enter the password: ");
 scanf("%s", buf);
 int match = strcmp(buf, password);
 if (match) {
 printf("Access denied.\n");
return 0;
 }
 else {
 printf("Access granted!\n");
 return 1;
}
 return 0;
}