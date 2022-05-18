#include <bits/stdc++.h>
using namespace std;
#define ll long long int 
const ll N=1e5+10;
const ll inf=1e9+10;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T;
    cin>>T;
    while(T--){
        ll n,k;
        cin>>n>>k;
        vector<ll> a(n);
        for(auto &it:a){ 
            cin>>it;
        }
        map<ll,ll> mp;
        ll m=0;
        for(auto &it:a){
            if(it%k==0){ 
                continue;
            }
            ++mp[k-it%k];
            m=max(m,mp[k-it%k]);
        }
        ll mv=0;
        for(auto &it:mp){
            if(it.second==m){
                mv=k*(it.second-1)+it.first+1;
            }
        }
        cout<<mv<<endl;
    }
    return 0;
}

