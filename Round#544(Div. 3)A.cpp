#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int h1,h2,m1,m2,h3,m3;
    scanf("%d:%d",&h1,&m1);
    scanf("%d:%d",&h2,&m2);
    int x1,x2,y1,y2;
    x1=h1*60+m1;
    x2=60*h2+m2;
    y1=(x2-x1)/2;
    y2=x1+y1;
    h3=y2/60;
    m3=y2%60;
    printf("%02d:%02d",h3,m3);
    return 0;
}
