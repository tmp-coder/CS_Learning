#include "apue.h"

int
main(void)
{
	if (lseek(STDIN_FILENO, 0, SEEK_CUR) < 0)
		printf("cannot seek\n");
	else
		printf("seek OK\n");
	exit(0);
}
