#include<bits/stdc++.h>
typedef long long ll;
using namespace std;
int main(){
    ll t;
    scanf("%lld",&t);
    while(t--){
        ll n,m,i,ep=0,op=0,eq=0,oq=0,c=0;
        scanf("%lld",&n);
        for(i=0;i<n;i++){
            ll x;
            scanf("%lld",&x);
            if(x%2==0){
                ep+=1;
            }
            else{
                op+=1;
            }
        }
        scanf("%lld",&m);
        for(i=0;i<m;i++){
            ll x;
            scanf("%lld",&x);
            if(x%2==0){
                eq+=1;
            }
            else{
                oq+=1;
            }
        }
        c=ep*eq + op*oq;
        printf("%lld\n",c);
    }
    return 0;
}
