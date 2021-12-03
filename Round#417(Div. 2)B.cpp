#include<bits/stdc++.h>
using namespace std;
#define ll long long int 
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    //cin>>T;
    while(T--){
        ll n,m; 
        cin>>n>>m;
        ll c=n*m*2;
        ll dp[n+1][2];
        dp[n][0]=-1;
        dp[n][1]=c;
        ll v[n][2];
        ll l=n-1;
        for(ll i=0;i<n;i++){
            string s; 
            cin>>s;
            v[i][0]=m+1;
            v[i][1]=0;
            for(ll j=1;j<=m;j++){
                if(s[j]== '1'){
                    l=min(l,i);
                    v[i][0]=min(v[i][0],j);
                    v[i][1]=max(v[i][1],j);
                }
            }
        }
        for(int i=n-1;i>l;i--){
            dp[i][0]=min(dp[i+1][0]+1+2*v[i][1],dp[i+1][1]+1+m+1);
            dp[i][1]=min(dp[i+1][0]+1+m+1,dp[i+1][1]+1+2*(m+1-v[i][0]));
        }
        int t=min(dp[l+1][0]+1+v[l][1],dp[l+1][1]+1+m+1-v[l][0]);
        cout<<t<<endl;
    }
    return 0;
}

