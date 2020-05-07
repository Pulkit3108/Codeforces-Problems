#include<bits/stdc++.h>
#include<numeric> 
using namespace std;
#define ll long long int
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin>>T;
    while(T--){
        ll n,ans=0,i;
        cin>>n;
        for(i=2;i<30;i++){
            ll a=pow(2,i)-1;
            if(n%a==0){
                ans=n/a;
                break;
            }
        }
        cout<<ans<<endl;

    }
    
    return 0;
}
