#include <stdio.h>

int visited[9];

void make_seq(int idx, int lst) {
	if (idx == 9) {
		cal(lst);
	}
	else {
		for (int i = 0; i < 9; i++) {
			if (visited[i] == 0) {
				lst[idx] = i;
				visited[i] = 1;
				make_seq(idx + 1, lst);
				visited[i] = 0;
			}
		}
	}
}


int main() {
	int N=0;
	scanf("%d", &N);
	int arr[N][9];

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < 9; j++) {
			scanf("%d", &arr[i][j]);
		}
	}

	int lst[9];
	make_seq(0, lst)




	return 0;
}