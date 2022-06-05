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
        ll n;
        cin>>n;
        vector<ll> a(n);
        for(auto &it:a){
            cin>>it;
            it=__builtin_ffsll(it)-1;
        }
        ll op=max(*min_element(a.begin(),a.end())-1,0LL);
        for(auto &it:a)
            op+=(it>0);
        cout<<op<<endl;
    }
    return 0;
}
