#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll T;
    cin>>T;
    while(T--){
        ll n,t;
        cin>>n>>t;
        ll i;
        vector<ll> a(n);
        vector<ll> x(n,0);
        map<ll,ll> c;
        map<ll,ll> d;
        for(i=0;i<n;i++){
            cin>>a[i];
        }
        for(i=0;i<n;i++){
            ll q=t-a[i];
            if(d[q]<c[q]){
                d[a[i]]+=1;
                x[i]=1;
            }
            else{
                c[a[i]]+=1;
                x[i]=0;
            }
        }
        for(i=0;i<n;i++){
            cout<<x[i]<<" ";
        }
        cout<<endl;
    }
    return 0;
}
