#include<bits/stdc++.h>
using namespace std;
#define ll long long int
const int m1=1e3+7;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
    while(t--){
        int n,m;
        cin>>n>>m;
        int a[m1][m1],b[m1];
        int i,j,k,l;
        for(i=1;i<=n;i++){
            for(j=1;j<=m;j++){
                cin>>a[i][j];
            }
        }
        for(i=1;i<=m;i++){
            for(j=1;j<=n;j++){
                int t;
                cin>>t;
                if(i==1){
                    b[j]=t;
                }
            }
        }
        for(i=1;i<=n;i++){
            for(j=1;j<=n;j++){
                for(k=1;k<=m;k++){
                    if(b[i]==a[j][k]){
                        for(l=1;l<=m;l++){
                            cout<<a[j][l]<<' ';
                        }
                        cout<<endl;
                    }
                }
            }
        }                 
    }
    return 0;
}
