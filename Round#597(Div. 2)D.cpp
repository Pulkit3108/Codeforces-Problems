#include <bits/stdc++.h>
using namespace std;
#define ll long long int 
const ll N=2e3+10;
const ll inf=1e9+10;
ll p[N];
ll s[N];
multiset<ll> mst;
void make(ll v){
    p[v]=v;
    s[v]=1;
    mst.insert(1);
}
int find(ll v){
    if(v==p[v]){
        return v;
    }
    else{
        return p[v]=find(p[v]);
    }
}
void union_set(ll a,ll b){
    a=find(a);
    b=find(b);
    if(a!=b){
        if(s[a]<s[b]){
            swap(a,b);
        }
        p[b]=a;
        s[a]+=s[b];
    }
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    //cin>>T;
    while(T--){
        ll n;
        cin>>n;
        vector<pair<ll,ll>> co(n+1);
        for(ll i=1;i<n+1;i++){
            cin>>co[i].first>>co[i].second;
        }
        vector<ll> c(n+1);
        vector<ll> k(n+1);
        for(ll i=1;i<n+1;i++){
            cin>>c[i];
        }
        for(ll i=1;i<n+1;i++){
            cin>>k[i];
        }
        vector<pair<ll,pair<ll,ll>>> g;
        for(ll i=1;i<n+1;i++){
            g.push_back({c[i],{0,i}});
        }
        for(ll i=1;i<n+1;i++){
            for(ll j=1;j<n+1;j++){
                ll d=abs(co[i].first-co[j].first)+abs(co[i].second-co[j].second);
                ll c=d*(k[i]+k[j]);
                g.push_back({c,{i,j}});
            }
        }
        sort(g.begin(),g.end());
        for(ll i=0;i<n+1;i++){
            make(i);
        }
        ll t=0;
        vector<ll> p;
        vector<pair<ll,ll>> w;
        for(auto &it:g){
            ll wt=it.first;
            ll u=it.second.first;
            ll v=it.second.second;
            if(find(u)==find(v)){
                continue;
            }
            else{
                union_set(u,v);
                t+=wt;
                if(u==0 || v==0){
                    p.push_back(max(u,v));
                }
                else{
                    w.push_back({u,v});
                }
            }
        }
        cout<<t<<endl;
        cout<<p.size()<<endl;
        for(int i=0;i<p.size();i++){
            cout<<p[i]<<" ";
        }
        cout<<endl;
        cout<<w.size()<<endl;
        for(auto &it:w){
            cout<<it.first<<" "<<it.second<<endl;
        }
    }
    return 0;
}

