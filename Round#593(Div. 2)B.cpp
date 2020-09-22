#include<bits/stdc++.h>
typedef long long ll;
using namespace std;
const int mod=1e9+7;
ll n,m;
ll calc(ll a,ll b){
    ll k=1;
    while(b>0){
        if(b&1){
            k=(k*a)%mod;
        }
        b>>=1;
        a=(a*a)%mod;
    }
    return(k%mod);
}
int main(){
    scanf("%lld%lld",&n,&m);
    ll c=calc(2,m)-1;
    ll a=calc(c,n);
    printf("%lld\n",a);
    return 0;
}
