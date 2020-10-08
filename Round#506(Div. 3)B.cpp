#include<cstdio>
#include<iostream>
using namespace std;
int main(){
    int n;
    scanf("%d",&n);
    int a[n];
    int i,j,c=0;
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    for(i=0;i<n;i++){
        j=i;
        while(j+1<n and a[j+1]<=2*a[j]){
            j+=1;
        }
        c=max(c,j-i+1);
        i=j;
    }
    printf("%d\n",c);
    return 0;
}
