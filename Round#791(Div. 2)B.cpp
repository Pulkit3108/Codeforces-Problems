#include<bits/stdc++.h>
using namespace std;
#define ll long long int 
const ll inf=1e9+10;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    //cin>>T;
    while(T--){
        ll n,q;
        cin>>n>>q;
        vector<ll> a(n);
        vector<pair<ll,ll>> p;
        ll s=0;
        for(ll i=0;i<n;++i){
            cin>>a[i];
            p.push_back({a[i],0});
            s+=a[i];
        }
        pair<ll,ll> l={0,-1};
        for(ll j=0;j<q;++j){
            ll t;
            cin>>t;
            if(t==1){
                ll i,x;
                cin>>i>>x;
                if(l.second<p[i-1].second){
                    s-=p[i-1].first; 
                } 
                else{
                    s-=l.first;
                }
                s+=x;
                p[i-1]={x,j};
            }
            else{
                ll x;
                cin>>x;
                l={x,j};
                s=n*x;
            }
            cout<<s<<endl;
        }
    }
    return 0;
}

