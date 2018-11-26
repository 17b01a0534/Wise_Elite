//Hacker Rank
/*Find the Point*/

#include <stdio.h>
int main() {
int n, px, py, qx, qy, rx, ry;
scanf("%d", &n);
for(int i = 0; i < n; i++) {
scanf("%d%d%d%d", &px, &py, &qx, &qy);
printf("%d %d\n", 2 * qx - px, 2 * qy - py);
}
}



