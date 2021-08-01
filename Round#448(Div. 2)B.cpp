#include<bits/stdc++.h>
using namespace std;
#define ll long long int
// const int mod=1e9+7;
// const ll N=1e7+10;
// ll f[N];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    //cin>>T;
    while(T--){
        ll n,x,k;
        cin>>n>>x>>k;
        ll a[n];
        map<ll,ll> m1;
        for(ll i=0;i<n;i++){
            cin>>a[i];
            m1[a[i]]+=1;
        }
        map<ll,ll> ct;
        ll p=0;
        for(auto it:m1){
            ct[(it.first-1)/x]+=it.second;
            p+=ct[it.first/x-k]*it.second;
        }
        cout<<p<<endl;
    }
    return 0;
}
