#include <bits/stdc++.h>
using namespace std;
#define ll long long int 
const ll N=1e5+10;
const ll inf=1e9+10;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    cin>>T;
    while(T--){
        ll n;
        cin>>n;
        ll e=0;
        ll o=-1;
        bool flag=true;
        for(ll i=0;i<n;i++){
            ll x;
            cin>>x;
            if(x&1 && x>=o){
                o=x;
            }
            else if(x%2==0 && x>=e){
                e=x;
            }
            else{
                flag=false;
            }
        }
        if(flag){
            cout<<"Yes"<<endl;
        }
        else{
            cout<<"No"<<endl;
        }
    }
    return 0;
}

