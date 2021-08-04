#include<bits/stdc++.h>
using namespace std;
#define ll long long int
// const int mod=1e9+7;
// const ll N=1e7+10;
// ll f[N];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    //cin>>T;
    while(T--){
        int n,m;
        cin>>n>>m;
        int f[n]={0};
        int k=n;
        for(int i=0;i<m;i++){
            int u,v;
            cin>>u>>v;
            if(u>v){
                if(f[v-1]==0){
                    k-=1;
                }
                f[v-1]+=1;
            }
            else if(u<v){
                if(f[u-1]==0){
                    k-=1;
                }
                f[u-1]+=1;
            }
        }
        int q;
        cin>>q;
        while(q--){
            int c;
            cin>>c;
            if(c==1){
                int u,v;
                cin>>u>>v;
                if(u>v){
                    if(f[v-1]==0){
                        k-=1;
                    }
                    f[v-1]+=1;
                }
                else if(u<v){
                    if(f[u-1]==0){
                        k-=1;
                    }
                    f[u-1]+=1;
                } 
            }
            else if(c==2){
                int u,v;
                cin>>u>>v;
                if(u>v){
                    if(f[v-1]==1){
                        k+=1;
                    }
                    f[v-1]-=1;
                }
                else if(u<v){
                    if(f[u-1]==1){
                        k+=1;
                    }
                    f[u-1]-=1;
                }
            }
            else{
                cout<<k<<endl;
            }
        }
    }
    return 0;
}
