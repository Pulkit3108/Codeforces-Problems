#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll T;
    cin>>T;
    while(T--){
        ll n;
        cin>>n;
        vector<ll> a(n);
        ll i,j;                          
        for(i=0;i<n;i++){
            cin>>a[i];
        }
        vector<bool> v(n,false);
        ll t=0;
        for(i=31;i>=0;i--){
            ll q=0;
            for(j=0;j<n;j++){
                if((1<<i)&(a[j]) && !v[j]){
                    q+=1;
                    v[j]=true;
                }
            }
            t+=(q*(q-1))/2; 
        }
        cout<<t<<"\n";
    }
    return 0;
}
