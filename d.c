#include <stdio.h>

int main() {
    int money = 0;
    printf("주유에 필요한 금액을 입력하세요 : ");
    scanf("%d", &money);
    printf("%d로 주유할 수 있는 휘발유는 %.2f입니다.", money, money / 1995);
    return 0;
}