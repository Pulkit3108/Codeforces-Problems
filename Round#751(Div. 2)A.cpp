#include<bits/stdc++.h>
using namespace std;
#define ll long long int 
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T;
    cin>>T;
    while(T--){
        ll n;
        cin>>n;
        vector<ll> a(n,0);
        unordered_map<ll,ll> mp;
        for(ll i=0;i<n;i++){
            cin>>a[i];
            mp[a[i]]+=1;
        }
        vector<ll> p(a);
        vector<ll> c(n,0);
        for(ll i=0;i<n;i++){
            c[i]=mp[p[i]];
        }
        vector<vector<ll>> f;
        f.push_back(p);
        ll t=0;
        while(c!=p){
            mp.clear();
            f.push_back(c);
            t+=1;
            p=c;
            for(ll i=0;i<n;i++){ 
                mp[p[i]]+=1;
            }
            for(ll i=0;i<n;i++){ 
                c[i]=mp[p[i]];
            }
        }
        ll q;
        cin>>q;
        while(q--){
            ll x,k;
            cin>>x>>k;
            if(k>=t){ 
                cout<<f[t][x-1]<<endl;
            }
            else{ 
                cout<<f[k][x-1]<<endl;
            }
        }
    }
    return 0;
}

