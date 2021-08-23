#include<bits/stdc++.h>
using namespace std;
#define ll long long int
const ll mod=1e9+7;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    //cin>>T;
    while(T--){
        ll n,k;
        cin>>n>>k;
        vector<int> a(n);
        ll m=0;
        for(ll i=0;i<n;i++){
            cin>>a[i];
            m=max((int)m,(int)a[i]);
        }
        stack<ll> st;
        ll c=0;
        st.push(a[0]);
        ll i=1;
        while(c<k){
            if(st.top()==m){
                break;
            }
            if(st.top()<a[i]){
                st.pop();
                c=1;
                st.push(a[i]);
            }
            else{
                c+=1;
            }
            i+=1;
            i=i%n;
        }
        cout<<st.top()<<endl;
    }
    return 0;
}
