#include <stdio.h>

int main(void) {
	int T, N, s, e;

	scanf("%d", &T);

	for (int tc = 1; tc <= T; tc++) {
		int arr[200] = { 0 }, ans = 0;
		scanf("%d", &N);

		for (int i = 0; i < N; i++) {
			scanf("%d %d", &s, &e);
			s -= 1;
			s /= 2;
			e -= 1;
			e /= 2;

			for (int j = s; j <= e; j++) {
				arr[j] += 1;
			}
		}

		for (int i = 0; i < 200; i++) {
			if (ans < arr[i])
				ans = arr[i];
		}

		printf("#%d %d\n", tc, ans);
	}

	return 0;
}