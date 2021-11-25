#include<bits/stdc++.h>
using namespace std;
#define ll long long int 
const int N=200010;
int t[N];
int c[N];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    //cin>>T;
    while(T--){
        ll n,k,q;
        cin>>n>>k>>q;
        for(ll i=0;i<n;i++){
            ll l,r;
            cin>>l>>r;
            t[l]+=1;
            t[r+1]-=1;
        }
        for(ll i=1;i<N;i++){
            t[i]+=t[i-1];
            c[i]=c[i-1]+(t[i]>=k);
        }
        for(ll i=0;i<q;i++){
            ll a,b;
            cin>>a>>b;
            cout<<c[b]-c[a-1]<<endl;
        }
    }
    return 0;
}

