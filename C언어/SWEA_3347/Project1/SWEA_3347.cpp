#include <stdio.h>

int main(void) {
	int T, N, M, A[1000] = { 0 }, B[1000] = { 0 };
	scanf("%d", &T);
	
	for (int tc = 1; tc <= T; tc++) {
		scanf("%d %d", &N, &M);
		for (int i = 0; i < N; i++) {
			scanf("%d", &A[i]);
		}
		for (int i = 0; i < M; i++) {
			scanf("%d", &B[i]);
		}

		int ans = 0, max_times = 0;
		
		for (int i = 0; i < N; i++) {
			int times = 0;
			for (int j = 0; j < M; j++) {
				if (A[i] <= B[j]) {
					times += 1;
					B[j] = 0;
				}
			}
			if (max_times < times) {
				ans = i + 1;
				max_times = times;
			}
		}
		printf("#%d %d\n", tc, ans);
	}

	return 0;
}