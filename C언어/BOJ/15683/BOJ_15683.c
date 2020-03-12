#include <stdio.h>

int N, M, ans = 64, num_camera = 0, cctv[64][3], dy[4] = { -1, 0, 1, 0 }, dx[4] = { 0, 1, 0, -1 };

int go(int idx, int now[8][8]) {
	if (idx == num_camera) {
		int res = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (now[i][j] == 0) {
					res += 1;
				}
			}
		}
		if (ans > res)
			ans = res;
		return 0;
	}
	
	int y, x, k;
	y = cctv[idx][0];
	x = cctv[idx][1];
	k = cctv[idx][2];

	if (k == 1) {
		for (int dir = 0; dir < 4; dir++) {
			int new[8][8] = { 0 };
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < M; j++) {
					new[i][j] = now[i][j];
				}
			}
			
			show(new, y, x, dir);
			go(idx + 1, new);
		}
	}

	else if (k == 2) {
		for (int dir = 0; dir < 2; dir++) {
			int new[8][8] = { 0 };
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < M; j++) {
					new[i][j] = now[i][j];
				}
			}

			show(new, y, x, dir);
			show(new, y, x, dir + 2);
			go(idx + 1, new);
		}
	}

	else if (k == 3) {
		for (int dir = 0; dir < 4; dir++) {
			int new[8][8] = { 0 };
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < M; j++) {
					new[i][j] = now[i][j];
				}
			}

			show(new, y, x, dir);
			show(new, y, x, (dir + 1) % 4);
			go(idx + 1, new);
		}
	}

	else if (k == 4) {
		for (int dir = 0; dir < 4; dir++) {
			int new[8][8] = { 0 };
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < M; j++) {
					new[i][j] = now[i][j];
				}
			}

			show(new, y, x, dir);
			show(new, y, x, (dir + 1) % 4);
			show(new, y, x, (dir + 2) % 4);
			go(idx + 1, new);
		}
	}

	else if (k == 4) {
		
		int new[8][8] = { 0 };
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				new[i][j] = now[i][j];
			}
		}

		show(new, y, x, 0);
		show(new, y, x, 1);
		show(new, y, x, 2);
		show(new, y, x, 3);
		go(idx + 1, new);
		
	}

	return 0;
}

void show(int new[8][8], int y, int x, int dir) {
	int ny, nx;
	ny = y + dy[dir];
	nx = x + dx[dir];

	while (0 <= ny && ny <= N - 1 && 0 <= nx && nx <= M - 1 && new[ny][nx] != 6) {
		if (new[ny][nx] = 0) {
			new[ny][nx] = 9;
		}
	}
}


int main(void) {
	int arr[8][8];

	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++) {
		for (int j = 0; i < M; j++) {
			scanf("%d", &arr[i][j]);
			if (arr[i][j] != 0 && arr[i][j] != 6) {
				cctv[num_camera][0] = i;
				cctv[num_camera][1] = j;
				cctv[num_camera][2] = arr[i][j];
				num_camera += 1;
			}
		}
	}

	go(0, arr);
	printf("%d", ans);
	return 0;
}