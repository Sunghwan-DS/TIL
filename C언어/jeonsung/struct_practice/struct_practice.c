#include <stdio.h>

struct point {
	int xpos;
	int ypos;
}pos1;


int main(void) {
	pos1.xpos = 1;
	pos1.ypos = 3;
	printf("pos1�� x��ǥ : %d, y��ǥ : %d\n", pos1.xpos, pos1.ypos);

	struct point pos2 = { 4, 6 };
	printf("pos2�� x��ǥ : %d, y��ǥ : %d\n", pos2.xpos, pos2.ypos);

	return 0;
}