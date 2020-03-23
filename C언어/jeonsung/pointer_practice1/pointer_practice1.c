# include <stdio.h>

int main(void) {
	int* pnum; // 포인터 변수 pnum 선언
	int num = 12345; // num값 초기화
	pnum = &num; // pnum에 num의 주소값을 저장
	printf("변경전 num의 값 : %d\n", num);
	printf("변경전 pnum이 가리키는 변수의 값 : %d\n", *pnum);
	printf("변경전 pnum이 저장한 주소 값 : %d\n", pnum);

	*pnum = 54321;

	printf("변경후 num의 값 : %d\n", num);
	printf("변경후 pnum이 가리키는 변수의 값 : %d\n", *pnum);
	printf("변경후 pnum이 저장한 주소 값 : %d\n", pnum);

	num = 33333;

	printf("변경후 num의 값 : %d\n", num);
	printf("변경후 pnum이 가리키는 변수의 값 : %d\n", *pnum);
	printf("변경후 pnum이 저장한 주소 값 : %d\n", pnum);

	int ppnum;
	ppnum = &num;
	printf("ppnum: %d", ppnum);

	return 0;
}