#include <stdio.h>

struct node {
	int data;
	int * next;
};

struct linkedlist {
	int current;
	struct node now = { current };
	struct node head = { -1000, now.next };

};

int main(void) {
	struct node node1 = { 5 };
	printf("%d", node1.current);

	return 0;
}