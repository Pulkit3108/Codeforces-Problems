#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
    while(t--){
        int n,i,j,m;
        cin>>n>>m;
        int a[n][m],b[n][m];
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                cin>>a[i][j];
            }
        }
        for(i=0;i<m;i++){
            for(j=0;j<n;j++){
                cin>>a[i][j];
            }
        }
    }
    return 0;
}
