#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define ld long double
ll mod=1e9+7;
ll binexp(ll a,ll b){
    if(b==0){
        return 1;
    }
    ll x=binexp(a,b/2);
    x=(x*x)%mod;
    if(b%2){
        x=(x*a)%mod;
    }
    return x;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T;
    cin>>T;
    while(T--){
        ll n,k;
        cin>>n>>k;
        if(k==0){
            cout<<1<<endl;
            continue;
        }
        vector<ll> dp(k+1,0);
        for(ll i=0;i<k;i++){
            if(i==0){
                ll c=0;
                if(n%2==0){
                    c=(binexp(2,n-1))%mod;
                }
                else{
                    c=(1+binexp(2,n-1))%mod;
                }
                dp[i]=c;
                continue;
            }
            ll c=0;
            if(n%2==0){
                c+=binexp(2,((i*n)));
                ll t=(((binexp(2,n-1)-1+mod)%mod)*dp[i-1])%mod;
                c=(c+t)%mod;
            }
            else{
                c+=dp[i-1];
                ll t=(binexp(2,n-1)*dp[i-1])%mod;
                c=(c+t)%mod;
            }
            dp[i]=c;
        }
        cout<<dp[k-1]<<endl;
    }
    return 0;
}
