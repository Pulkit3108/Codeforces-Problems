#include<bits/stdc++.h>
using namespace std;
int main(){
    int n,k;
    scanf("%d%d",&n,&k);
    int A[n],i;
    vector<int> B(k,0);
    for(i=0;i<n;i++){
        scanf("%d",&A[i]);
        B[A[i]-1]+=1;
    }
    int c=0,a=0;
    for(i=0;i<k;i++){
        c+=B[i]%2;
        a+=(B[i]/2)*2;
    }
    a+=(c+1)/2;
    printf("%d\n",a);
    return 0;
}
