#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll n,k,ans=0;
    cin>>n>>k;
    ll r,g,b,c;
    r=2*n;
    g=5*n;
    b=8*n;
    if(r%k==0){
        ans+=r/k;
    }
    else{
        ans+=r/k+1;
    }
    if(g%k==0){
        ans+=g/k;
    }
    else{
        ans+=g/k+1;
    }
    if(b%k==0){
        ans+=b/k;
    }
    else{
        ans+=b/k+1;
    }
    cout<<ans<<endl;



    return 0;
}
