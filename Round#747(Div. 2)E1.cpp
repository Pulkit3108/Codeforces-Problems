#include <bits/stdc++.h>
using namespace std;
#define ll long long int 
const ll mod=1e9+7;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    //cin>>T;
    while(T--){
        ll k;
        cin>>k;
        ll p=(1LL<<k)-2;
        ll f=1;
        ll a=4;
        while(p){
            if(p&1){
                f=(f*a)%mod;
            }
            a=(a*a)%mod;
            p>>=1;
        }
        ll r=(f*6)%mod;
        cout<<r<<endl;
    }
    return 0;
}

