#include <stdio.h>

struct Node {
	int data;
	struct Node *next;
};



int main(void) {
	struct Node head;
	struct Node node1 = { 5 };
	printf("%d", node1.data);
	printf("%d", head.data);
	

	return 0;
}