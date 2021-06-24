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
        ll n,k1,k2;
        cin>>n>>k1>>k2;
        vector<ll> a(n);
        vector<ll> b(n);
        ll i=0;
        for(i=0;i<n;i++){
            cin>>a[i];
        }
        for(i=0;i<n;i++){
            cin>>b[i];
        }
        priority_queue<ll> p;
        for(i=0;i<n;i++){
            p.push(abs(a[i]-b[i]));
        }
        ll k=k1+k2;
        while(k>0){
            ll r=p.top();
            p.pop();
            r-=1;
            k-=1;
            p.push(abs(r));
        }
        ll t=0;
        while(p.size()!=0){
            ll r=p.top();
            p.pop();
            t+=(r*r);
        }
        cout<<t<<endl;
    }
    return 0;
}
