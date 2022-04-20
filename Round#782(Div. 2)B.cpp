#include <bits/stdc++.h>
using namespace std;
#define ll long long int 
const ll N=1e5+10;
const ll inf=1e9+10;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T;
    cin>>T;
    while(T--){
        ll n,k;
        cin>>n>>k;
        string b;
        cin>>b;
        vector<ll> f(n,0);
        ll t=k;
        for(ll i=0;i<n && t>0;i++){
            if(k%2==b[i]-'0'){
                f[i]=1;
                --t;
            }
        }
        f[n-1]+=t;
        for(ll i=0;i<n;i++){
            if((k-f[i])&1){   
                b[i]='1'-(b[i]-'0');
            }
        }
        cout<<b<<endl;
        for(auto &it:f){  
            cout<<it<<" ";
        }
        cout<<endl;
    }
    return 0;
}

