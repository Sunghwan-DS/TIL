# include <stdio.h>

int main(void) {
	int* pnum; // ������ ���� pnum ����
	int num = 12345; // num�� �ʱ�ȭ
	pnum = &num; // pnum�� num�� �ּҰ��� ����
	printf("������ num�� �� : %d\n", num);
	printf("������ pnum�� ����Ű�� ������ �� : %d\n", *pnum);
	printf("������ pnum�� ������ �ּ� �� : %d\n", pnum);

	*pnum = 54321;

	printf("������ num�� �� : %d\n", num);
	printf("������ pnum�� ����Ű�� ������ �� : %d\n", *pnum);
	printf("������ pnum�� ������ �ּ� �� : %d\n", pnum);

	num = 33333;

	printf("������ num�� �� : %d\n", num);
	printf("������ pnum�� ����Ű�� ������ �� : %d\n", *pnum);
	printf("������ pnum�� ������ �ּ� �� : %d\n", pnum);

	int ppnum;
	ppnum = &num;
	printf("ppnum: %d", ppnum);

	return 0;
}