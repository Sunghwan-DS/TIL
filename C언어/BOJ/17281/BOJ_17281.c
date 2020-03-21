#include <stdio.h>
int N, sequence[9], player[50][9], use[9] = { 0 }, ans = 0;

void play(int seq[]) {
	int score = 0, num = 0;
	for (int inning = 0; inning < N; inning++) {
		int out = 0, runner[3] = { 0 };
		do {
			if (player[inning][seq[num]] == 0) {
				out += 1;
			}
			else if (player[inning][seq[num]] == 1) {
				score += runner[2];
				runner[2] = runner[1];
				runner[1] = runner[0];
				runner[0] = 1;
			}
			else if (player[inning][seq[num]] == 2) {
				score = score + runner[2] + runner[1];
				runner[2] = runner[0];
				runner[1] = 1;
				runner[0] = 0;
			}
			else if (player[inning][seq[num]] == 3) {
				score = score + runner[2] + runner[1] + runner[0];
				runner[2] = 1;
				runner[1] = 0;
				runner[0] = 0;
			}
			else if (player[inning][seq[num]] == 4) {
				score = score + runner[2] + runner[1] + runner[0] + 1;
				runner[2] = 0;
				runner[1] = 0;
				runner[0] = 0;
			}
			num = (num + 1) % 9;
		} while (out < 3);
	}

	if (ans < score) {
		ans = score;
	}
}


int make_lst(int idx, int seq[]) {
	if (idx == 9) {
		play(seq);
		return 0;
	}

	if (idx == 3) {
		seq[3] = 0;
		make_lst(idx + 1, seq);
		return 0;
	}

	for (int i = 1; i < 9; i++) {
		if (use[i] == 0) {
			seq[idx] = i;
			use[i] = 1;
			make_lst(idx + 1, seq);
			use[i] = 0;
		}
	}
	return 0;
}


int main(void) {
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < 9; j++) {
			scanf("%d", &player[i][j]);
		}
	}

	make_lst(0, sequence);
	printf("%d", ans);
	return 0;
}