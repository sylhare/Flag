#include <stdio.h>

int main(int argc, char** argv) {
    if (argc <= 1) {
	printf("usage: %s <password>\n", argv[0]);
	return(-1);
    }
    char* pass = argv[1];
    if (
        (pass[0] == 'P') &&
        (pass[1] == 'A') &&
        (pass[2] == 'S') &&
        (pass[3] == 'S') &&
        (pass[4] == 'W') &&
        (pass[5] == 'O') &&
        (pass[6] == 'R') &&
        (pass[7] == 'D')
        )
        {
        puts("WIN");
        }

    else {
        puts("FAIL");
    }

}
