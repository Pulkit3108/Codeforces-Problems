#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    //cin>>T;
    while(T--){ 
        ll n,k;
        cin>>n>>k;
        vector<ll> p(n);
        vector<pair<ll,ll>> c;
        priority_queue<ll,vector<ll>,greater<ll>> pq;
        map<ll,ll> dp;
        ll s=0;
        ll i,j;
        for(i=0;i<n;i++){ 
            cin>>p[i];
        }
        for(i=0;i<n;i++){
            ll x;
            cin>>x;
            c.push_back(make_pair(p[i],x));
        }
        sort(c.begin(),c.end());
        for(i=0;i<n;i++){
            s+=c[i].second;
            if(i<=k){
                 dp[c[i].first]=s;
                 pq.push(c[i].second);
            }
            else{
                ll t=pq.top();
                pq.pop();
                s-=t;
                dp[c[i].first]=s;
                pq.push(c[i].second);
            }
        }
        for(auto it : p){
            cout<<dp[it]<<" ";
        }
        cout<<endl;
    }
    return 0;
}
