#include<bits/stdc++.h>
using namespace std;
#define ll long long int 
const int inf=1e9+10;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T;
    cin>>T;
    while(T--){
        ll n;
        cin>>n;
        vector<pair<ll,ll>> v;
        ll l[n+1]={0};
        ll r;
        for(ll i=0;i<n;i++){
           ll a,b;
           cin>>a>>b;
           v.push_back({a,b});
       }
       sort(v.rbegin(),v.rend());
       for(ll i=0;i<n;i++){
            if(v[i].first==v[i].second){
            cout<<v[i].first<<" "<<v[i].second<<" "<<v[i].first<<endl;
            l[v[i].first]=1;
            }
            else{
                for(ll j=v[i].first;j<=v[i].second;j++){
                    if(l[j]==0){
                        r=j;
                    }
                }
                cout<<v[i].first<<" "<<v[i].second<<" "<<r<<endl;
                l[r]=1;
            }
       }
       cout<<endl;
    }
    return 0;
}

