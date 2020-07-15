#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){   
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T=1;
    //scanf("%d",&T);
    while(T--){   
        ll N,M,K,L;
        scanf("%lld%lld%lld%lld",&N,&M,&K,&L);
        ll X;
        if((L+K)%M==0){
            X=(L+K)/M;
        }
        else{
            X=(L+K)/M+1;
        }
        if(X*M>N){
            printf("%d",-1);
        }
        else{
            printf("%lld\n",X);
        }
    }
    return 0;
}
