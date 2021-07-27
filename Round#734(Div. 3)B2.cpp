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
    ll T;
    cin>>T;
    while(T--){
        ll n,k;
        cin>>n>>k;
        map<ll,vector<ll>> mp;
        ll a[n];
        mp.clear();
        memset(a,0,sizeof(a));
        for(ll i=0;i<n;i++){
            int x;
            cin>>x;
            if(mp[x].size()<k){
                mp[x].push_back(i);
            }
        }
        int m=0;
        for(auto it:mp){ 
            m+=it.second.size();
        }
        m-=m%k;
        int co=0;
        for(auto it:mp){
            for(auto i:it.second){
                co+=1;
                a[i]=co;
                co%=k;
                m-=1;
                if(m==0){
                    break;
                }
            }
            if(m==0){
                break;
            }
        }
        for(ll i=0;i<n;i++){
            cout<<a[i]<<' ';
        }
        cout<<'\n';
    }
    return 0;
}
