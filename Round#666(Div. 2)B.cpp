#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll T=1;
    //cin>>T;
    while(T--){
        ll n;
        cin>>n;
        vector<ll> a(n);
        ll i;
        for(i=0;i<n;i++){
            cin>>a[i];
        }
        sort(a.begin(),a.end());
        ll b=1e15;
        ll f=b;
        ll c=1;
        ll k=0;
        while(1){
            ll v=0,p=1;
            for(i=0;i<n;i++,p*=c){
                if(p>=b){
                    v=-1;
                    break;
                }
                v+=abs(p-a[i]);
            }
            if(v==-1){
                break;
            }
            f=min(f,v);
            c+=1;
        }
        cout<<f<<endl;
    }
    return 0;
}
