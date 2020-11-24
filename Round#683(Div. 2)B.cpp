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
        int a[n][m];
        int i,j;
        ll s=0;
        ll mn=10000;
        ll c=0;
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                cin>>a[i][j];
                if(a[i][j]<0){
                    c+=1;
                    a[i][j]=-a[i][j];
                }
                s+=a[i][j];
                if(a[i][j]<mn){
                    mn=a[i][j];
                }
            }
        }
        if(c%2!=0){
            s-=2*mn;
        }
        cout<<s<<"\n";
        
    }
    return 0;
}
