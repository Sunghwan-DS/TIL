#include <stdio.h>

int arr[50][50], new_arr[50][50], dy[4], dx[4];

int main(void) {
	int R, C, T, m1, m2, ni, nj, remain, val;
	int ans = 0;

	dy[0] = -1, dy[1] = 0, dy[2] = 1, dy[3] = 0, dx[0] = 0, dx[1] = 1, dx[2] = 0, dx[3] = -1;
	scanf("%d %d %d", &R, &C, &T);
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			scanf("%d", &arr[i][j]);
			new_arr[i][j] = 0;
		}
	}

	for (int i = 2; i < R - 2; i++) {
		if (arr[i][0] == -1) {
			m1 = i;
			m2 = i + 1;
			arr[m1][0] = 0;
			arr[m2][0] = 0;

			break;
		}
	}


	for (int t = 0; t < T; t++) {

		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				remain = arr[i][j];
				val = arr[i][j] / 5;
				for (int d = 0; d < 4; d++) {
					ni = i + dy[d];
					nj = j + dx[d];
					if (0 <= ni && ni < R && 0 <= nj && nj < C) {
						if (nj != 0 || (ni != m1 && ni != m2)) {
							new_arr[ni][nj] += val;
							remain -= val;
						}
					}
				}
				new_arr[i][j] += remain;
			}
		}

		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				arr[i][j] = new_arr[i][j];
				new_arr[i][j] = 0;
			}
		}

		for (int i = m1 - 2; i >= 0; i--) {
			arr[i + 1][0] = arr[i][0];
		}

		for (int j = 1; j < C; j++) {
			arr[0][j - 1] = arr[0][j];
		}

		for (int i = 1; i < m1 + 1; i++) {
			arr[i - 1][C - 1] = arr[i][C - 1];
		}

		for (int j = C - 2; j >= 0; j--) {
			arr[m1][j + 1] = arr[m1][j];
		}

		for (int i = m2 + 2; i < R; i++) {
			arr[i - 1][0] = arr[i][0];
		}

		for (int j = 1; j < C; j++) {
			arr[R - 1][j - 1] = arr[R - 1][j];
		}

		for (int i = R - 2; i >= m2; i--) {
			arr[i + 1][C - 1] = arr[i][C - 1];
		}

		for (int j = C - 2; j >= 0; j--) {
			arr[m2][j + 1] = arr[m2][j];
		}
	}

	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			ans += arr[i][j];
		}
	}

	printf("%d", ans);
}