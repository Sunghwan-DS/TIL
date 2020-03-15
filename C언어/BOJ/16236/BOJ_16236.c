#include <stdio.h>
int N, arr[20][20];
int dy[4] = { -1, 0, 1, 0 }, dx[4] = { 0, 1, 0, -1 };
int eat_y = 21, eat_x = 21;
int y, x;


int main(void) {
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			scanf("%d", &arr[i][j]);
			if (arr[i][j] == 9) {
				y = i;
				x = j;
				arr[i][j] = 0;
			}
		}
	}

	int size = 2, ans = 0, q[400][2], visited[20][20] = { 0 };
	int eat = 0;

	q[0][0] = y;
	q[0][1] = x;
	int front = 0, rare = 1, cnt = 0;

	while (front < rare) {
		int last_rare = rare;
		for (; front < last_rare; front++) {
			y = q[front][0];
			x = q[front][1];
			for (int dir = 0; dir < 4; dir++) {
				int ny, nx;
				ny = y + dy[dir];
				nx = x + dx[dir];
				if (0 <= ny && ny <= N - 1 && 0 <= nx && nx <= N - 1 && visited[ny][nx] == 0 && arr[ny][nx] <= size) {
					visited[ny][nx] = 1;
					if (0 < arr[ny][nx] && arr[ny][nx] < size) {
						if (eat_y > ny) {
							eat_y = ny;
							eat_x = nx;
						}
						else if (eat_y == ny) {
							if (eat_x > nx) {
								eat_x = nx;
							}
						}
					}
					else {
						q[rare][0] = ny;
						q[rare][1] = nx;
						rare += 1;
					}
				}
			}
		}
		cnt += 1;

		if (eat_y < 21) {
			eat += 1;
			if (eat == size) {
				size += 1;
				eat = 0;
			}

			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					visited[i][j] = 0;
				}
			}
			front = 0;
			rare = 1;
			q[0][0] = eat_y;
			q[0][1] = eat_x;
			arr[eat_y][eat_x] = 0;
			ans += cnt;
			cnt = 0;
			eat_y = 21;
			eat_x = 21;
		}
	}

	printf("%d", ans);

	return 0;
}