#include<bits/stdc++.h>
using namespace std;
#define ll long long int 
pair<ll,ll> duplicate(vector<ll> &v,ll n){
    vector<ll> f(n+10,-1);
    for(ll i=0;i<n;i++){
        if(f[v[i]]!=-1){ 
            return make_pair(f[v[i]],i);
        }
        else{ 
            f[v[i]]=i;
        }
    }
    return make_pair(-1,-1);
}
void fix(vector<ll> &v,ll p,ll n){
    vector<bool> f(n+10,false);
    for(ll i=0;i<n;i++){ 
        if(i!=p){ 
            f[v[i]]=true;
        }
    }
    for(ll i=1;i<=n;i++){
        if(!f[i]){ 
            v[p]=i; 
        }
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
        vector<ll> a(n),b(n);
        for(ll i=0;i<n;i++){
            cin>>a[i];
        }
        for(ll i=0;i<n;i++){
            cin>>b[i];
        }
        pair<ll,ll> da,db;
        da=duplicate(a,n);
        db=duplicate(b,n);
        if(da==db){
            a[da.first]=b[db.first];
        }
        else if(da.first==db.first || da.first==db.second){
            a[da.second]=b[da.second];
            fix(a,da.first,n);
        } 
        else if(da.second==db.first || da.second==db.second){
            a[da.first]=b[da.first];
            fix(a,da.second,n);
        } 
        else{
            a[da.first]=b[da.first];
            a[da.second]=b[da.second];
        }
        for(ll i=0;i<n;i++){ 
            cout<<a[i]<<" ";
        }
        cout<<endl;
    }
    return 0;
}

