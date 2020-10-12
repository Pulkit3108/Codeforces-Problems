#include<bits/stdc++.h>
using namespace std;
int n;
int p[1005],vis[1005];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T=1;
    while(T--){
        cin>>n;
        int i;
        for(i=1;i<=n;i++){
            cin>>p[i];
        }
        for(i=1;i<=n;i++){
            memset(vis,0,sizeof(vis));
            int t=i;
            while(1){
                vis[t]++;
                if(vis[t]==2){
                    cout<<t<<" ";
                    break;
                }
                t=p[t];
            }
        }
        cout<<endl;
    }
    return 0;
}



        
