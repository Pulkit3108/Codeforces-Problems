#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll t;
    scanf("%lld",&t);
    while(t--){
        ll n;
        scanf("%lld",&n);
        ll c=0,i;
        for(i=0;i<n;++i){
            ll x;
            scanf("%lld",&x);
            c=max(0LL,c+x);
        }
        cout<<c<<"\n";
    }
    return 0; 
} 
