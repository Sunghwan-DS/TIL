#include <stdio.h>

struct point {
	int xpos;
	int ypos;
}pos1;


int main(void) {
	pos1.xpos = 1;
	pos1.ypos = 3;
	printf("pos1ÀÇ xÁÂÇ¥ : %d, yÁÂÇ¥ : %d\n", pos1.xpos, pos1.ypos);

	struct point pos2 = { 4, 6 };
	printf("pos2ÀÇ xÁÂÇ¥ : %d, yÁÂÇ¥ : %d\n", pos2.xpos, pos2.ypos);

	return 0;
}