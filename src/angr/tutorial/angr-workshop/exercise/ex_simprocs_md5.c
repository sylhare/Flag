#include<stdio.h>
#include<string.h>
#include<openssl/md5.h>

int md5 = 0;
unsigned char result[MD5_DIGEST_LENGTH];
char* string = "asdfasdf";

int main(int argc, char** argv) {
	MD5(string, strlen(string), result);

	for(md5 = 0; md5 < MD5_DIGEST_LENGTH; md5++) {
		printf("%02x", result[md5]);
	}
	printf("\n");
}
