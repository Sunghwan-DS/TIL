#include <stdio.h>

int main(void) {
	int T;

	scanf("%d", &T);

	for (int tc = 1; tc <= T; tc++) {
		int W, H, N, x, y, nx, ny, dx, dy, ans = 0;
		scanf("%d %d %d", &W, &H, &N);
		scanf("%d %d", &x, &y);

		for (int i = 1; i < N; i++) {
			scanf("%d %d", &nx, &ny);
			dx = nx - x;
			dy = ny - y;

			if (dx * dy >= 0) {
				if (abs(dx) >= abs(dy)) {
					ans += abs(dx);
				}
				else {
					ans += abs(dy);
				}
			}
			else {
				ans += abs(dx) + abs(dy);
			}

			x = nx;
			y = ny;

		}
		printf("#%d %d\n", tc, ans);
	}
	return 0;
}