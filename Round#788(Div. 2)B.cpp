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
        ll n;
        cin>>n;
        string s;
        cin>>s;
        ll sp;
        cin>>sp;
        vector<bool> f(26,false);
        for(ll i=0;i<sp;++i){
            char c;
            cin>>c;
            f[c-'a']=true;
        }
        ll ct=0,d=0;
        for(auto &it:s){
            if(f[it-'a']){
                d=max(d,ct);
                ct=1;
            }
            else{
                ++ct;
            }
        }
        cout<<d<<endl;
    }
    return 0;
}

