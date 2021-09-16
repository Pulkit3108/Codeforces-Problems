#include <bits/stdc++.h>
using namespace std;
#define ll long long int 
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T = 1;
    //cin>>T;
    while (T--){
        ll n;
        cin>>n;
        vector<ll> C(n+5,0);
        for(ll i=2;i<n+2;i++){
            if(!C[i]){
                for(ll j=i*i;j<n+2;j+=i){
                    C[j]=1;
                }
            }
        }
        if(n>2){
            cout<<2<<endl;
        }
        else{
            cout<<1<<endl;
        }
        for(ll i=2;i<n+2;i++){
            if(!C[i]){
                cout<<1<<" ";
            }
            else{
                cout<<2<<" ";
            } 
        }
        cout<<endl;
    }
    return 0;
}
