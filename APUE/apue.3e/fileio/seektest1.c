#include "apue.h"

int
main(void)
{
	if (lseek(STDIN_FILENO, 0, SEEK_CUR) < 0){
		printf("%d\n",STDIN_FILENO);
		printf("cannot seek\n");
	}
	else{
		printf("%d\n",STDIO_FILENO);
		printf("seek OK\n");
	}
	exit(0);
}
