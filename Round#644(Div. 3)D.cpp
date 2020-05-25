#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll T;
    cin>>T;
    while(T--){
        ll n,k;
        cin>>n>>k;
        ll i;
        ll a=n;
        for(i=1;i*i<=n;i++){
            if(n%i==0){
                if(i<=k){
                    a=min(a,n/i);
                }
                if(n/i<=k){
                    a=min(a,i);
                }
            }
        }
        cout<<a<<endl;
        
    }

    return 0;
}
