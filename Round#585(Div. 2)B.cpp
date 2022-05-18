#include<bits/stdc++.h>
using namespace std;
#define ll long long int 
const int inf=1e9+10;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    //cin>>T;
    while(T--){
        ll n ;
        cin>>n;
        vector<ll> a(n);
        for(auto &it:a){
            cin>>it;
        }
        ll dp[2][n];
        if(a[0]>0){
            dp[1][0]=1;
            dp[0][0]=0;
        }   
        else{
            dp[1][0]=0;
            dp[0][0]=1;     
        }
        for(int i=1;i<n;++i){
            if(a[i]>0){
                dp[1][i]=1+dp[1][i-1];
                dp[0][i]=dp[0][i-1];
            }
            else{
                dp[1][i]=dp[0][i-1];
                dp[0][i]=1+dp[1][i-1];
            }
        }
        ll c1=0,c2=0;
        for(int i=0;i<n;++i){
           c1+=dp[0][i];
           c2+=dp[1][i];   
        }
        cout<<c1<<" "<<c2<<endl;
    }
    return 0;
}
