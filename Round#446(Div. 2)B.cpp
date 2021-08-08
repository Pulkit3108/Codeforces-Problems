#include<bits/stdc++.h>
using namespace std;
#define ll long long int
// const int mod=1e9+7;
// const ll N=1e7+10;
// ll f[N];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    //cin>>T;
    while(T--){
        ll n;
        cin>>n;
        stack<ll> st;
        for(ll i=0;i<n;i++){
            ll x;
            cin>>x;
            while(!st.empty() and st.top()>=i-x){
                st.pop();
            }
            st.push(i);
        }
        cout<<st.size()<<endl;

    }
    return 0;
}
