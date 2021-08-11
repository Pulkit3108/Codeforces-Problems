#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define ld long double
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T;
    cin>>T;
    while(T--){
        ll n;
        cin>>n;
        vector<ll> a(n);
        for(ll i=0;i<n;i++){
            cin>>a[i];
        }
        ll m=a[0];
        ll s=0;
        for(ll i=0;i<n;i++){
            if(a[i]>m){
                m=a[i];
            }
            s+=a[i];
        }
        cout<<fixed<<setprecision(10)<<(1.0)*(s-m)/(n-1)+m<<endl;
    }
    return 0;
}
