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
        int n,m;
        cin>>n>>m;
        int i,j,k;
        char mp[n][m];
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                cin>>mp[i][j];
            }
        }   
        const int x[]={0,0,-1,-1,-1,1,1,1};
        const int y[]={-1,1,0,-1,1,-1,0,1};
        bool flag = true;
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                if(mp[i][j]=='*'){ 
                    continue;
                }
                int c=mp[i][j]-'0';
                int t=0;
                for(k=0;k<8;k++){
                    int a=i+x[k];
                    int b=j+y[k];
                    if(a<0 || a>=n || b<0 || b>=m){ 
                        continue;
                    }
                    if(mp[a][b]=='.' || ('1'<=mp[a][b] && mp[a][b]<='8')){ 
                        continue;
                    }
                    t+=1;
                }   
                if(mp[i][j]== '.' && t==0){
                    continue;
                }
                if(t!=c){
                    flag=false;
                    break;
                }
            }
            if(!flag){ 
                break;
            }
        }
        if(flag){
            cout<<"YES"<<endl;
        } 
        else{
            cout<<"NO"<<endl;
        }
    }
    return 0;
}
