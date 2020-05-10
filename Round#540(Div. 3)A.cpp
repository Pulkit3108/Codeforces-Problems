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
        ll n,a,b,ans;
        cin>>n>>a>>b;
        if(n%2==0){
            if(2*a<b){
                ans=n*a;
            }
            else{
                ans=(n/2)*b;
            }
        }
        else{
            if(2*a<b){
                ans=n*a;
            }
            else{
                ans=((n-1)/2)*b+a;
            }
        }
        cout<<ans<<endl;
    }
    
    return 0;
}
