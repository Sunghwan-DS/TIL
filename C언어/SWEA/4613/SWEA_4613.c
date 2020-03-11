#include <stdio.h>

int main(void) {
	int T, N, M, data[50][3];
	char arr[50][50];

	scanf("%d", &T);

	for (int tc = 1; tc <= T; tc++) {
		scanf("%d %d", &N, &M);

		for (int i = 0; i < N; i++) {
			int W = 0, B = 0, R = 0;
			scanf("%s", arr[i]);
			for (int j = 0; j < M; j++) {
				if (arr[i][j] == 'W')
					W += 1;
				else if (arr[i][j] == 'B')
					B += 1;
				else
					R += 1;
			}
			data[i][0] = W;
			data[i][1] = B;
			data[i][2] = R;
		}

		int max_res = 0;
		for (int white = 0; white < N - 2; white++) {
			for (int blue = white + 1; blue < N - 1; blue++) {
				int res = 0;
				for (int i = 0; i <= white; i++) {
					res += data[i][0];
				}
				for (int i = white + 1; i <= blue; i++) {
					res += data[i][1];
				}
				for (int i = blue + 1; i < N; i++) {
					res += data[i][2];
				}

				if (max_res < res)
					max_res = res;
			}
		}
		printf("#%d %d\n", tc, N * M - max_res);
	}
	return 0;
}