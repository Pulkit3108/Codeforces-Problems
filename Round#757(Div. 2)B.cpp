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
        vector<pair<ll,ll>> a(n);
        for(ll i=0;i<n;i++){
            ll x;
            cin>>x;
            a[i].first=x;
            a[i].second=i;
        }
        sort(a.rbegin(),a.rend());
        vector<ll> d(n);
        ll h=(n+2)/2;
        ll l=h-1;
        ll r=h+1;
        ll f=0;
        ll c=0;
        bool flag=true;
        for(int i=0;i<n;i++){
            ll t=a[i].first;
            ll id=a[i].second;
            if(flag){
                d[id]=l;
                f=2*(h-l);
                l-=1;
            }
            else{
                d[id]=r;
                f=2*(r-h); 
                r+=1;
            }
            c+=t*f;
            flag=!flag;
        }
        cout<<c<<endl;
        cout<<h<<" ";
        for(auto &it:d){
            cout<<it<<" ";
        }
        cout<<endl;
    }
    return 0;
}

