#include<bits/stdc++.h>
using namespace std;
#define ll long long int
bool compare(pair<ll,ll> &a, pair<ll,ll> &b){
    return(a.second<b.second);
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
        vector<pair<ll,ll>> w;
        ll i,j,k=0;
        for(i=0; i<n; i++){
            int t;
            cin>>t;
            w.push_back(make_pair(i,t));
        }
        sort(w.begin(), w.end(), compare);
        string s;
        cin>>s;
        ll a[n],b[n];
        stack<long long> st;
        for(i=0;i<(2*n);i++){
            if(s[i]=='0'){
            st.push(w[k].first);
            cout<<(w[k].first+1)<<" ";
            k+=1;
            }
            else{
                cout<<(st.top()+1)<<" ";
                st.pop();
            }
        }
    }
    return 0;
}
