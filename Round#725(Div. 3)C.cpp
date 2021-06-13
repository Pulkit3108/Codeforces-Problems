#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    cin>>T;
    while(T--){
        ll n,l,r;       
        cin>>n>>l>>r;
        vector<ll> a(n);
        ll i,c=0;
        for(i=0;i<n;i++){
            cin>>a[i];
        }
        sort(a.begin(),a.end());
        for(i=0;i<n-1;i++){
            auto c1=lower_bound(a.begin()+i+1,a.end(),l-a[i]);
            auto c2=upper_bound(a.begin()+i+1,a.end(),r-a[i]);
            c+=c2-c1;
        }
        cout<<c<<endl;
    }
    return 0;
}
