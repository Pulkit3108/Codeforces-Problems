#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll T;
    scanf("%lld",&T);
    while(T--){
        ll c=0;
        ll n,r,l=1;
        scanf("%lld%lld",&n,&r);
        if(n<=l){
            printf("1\n");
            continue;
        }
        if(n<=r){
            r=n-1;
            c=1;
        }
        ll x=c+((l+r)*(r-l+1))/2;
        printf("%lld\n",x);
        
    }
    
    return 0;
}
