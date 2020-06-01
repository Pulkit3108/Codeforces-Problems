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
        ll l,r;
        cin>>l>>r;
        ll a,b;
        a=l*pow(-1,l);
        b=r*pow(-1,r);
        ll ans=0;
        if(a==b){
            ans=a;
        }
        else if(a<0 and b<0){
            ll c=(r-l)/2;
            ans=a-c;

        }
        else if(a>0 and b>0){
            ll c=(r-l)/2;
            ans=a+c;
        }
        else if(a>0 and b<0){
            ll c=(r-l-1)/2;
            ans=a+c+b;
        }
        else if(a<0 and b>0){
            ll c=(r-l+1)/2;
            ans=a-c+(b+1);
        }
        cout<<ans<<endl; 
    }

    return 0;
}
