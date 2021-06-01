#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin>>T;
    while(T--){
        int n,m;
        cin>>n>>m;
        char a[n][m];
        vector<vector<int>> dp(n+1,vector<int>(m+1));
        int i,j;
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                cin>>a[i][j];
                if(a[i][j]=='*'){
                    dp[i][j]=1;
                }
            }
        }
        int ans=0;
        for(i=n-1;i>=0;i--){
            for(int j=m-2;j>=1;j--){
                if(dp[i][j]==1){
                    dp[i][j]=1+min({dp[i+1][j-1],dp[i+1][j],dp[i+1][j+1]});
                }
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++)
                ans+=dp[i][j];
        }
        cout<<ans<<"\n";
    }
    return 0;
}
