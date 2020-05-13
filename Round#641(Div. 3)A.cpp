#include<bits/stdc++.h>
using namespace std;
#define ll long long int
ll SD(ll n){   
    if(n%2==0) 
        return 2; 
    for(ll i=3;i*i<=n;i+=2){ 
        if(n%i==0) 
            return i; 
    } 
    return n; 
} 
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll t;
    cin>>t;
    while(t--){
        ll n,k;
        cin>>n>>k;
        ll ans,i,x=1;
        if(n%2==0){
            ans=n+2*k;
        }
        else{
            ans=n+2*(k-1)+SD(n);
        }
        cout<<ans<<endl;
    }

    return 0;
}
