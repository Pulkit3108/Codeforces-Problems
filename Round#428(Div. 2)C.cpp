#include<bits/stdc++.h>
using namespace std;
#define ll long long int 
#define ld long double
const ll mod=1e9+7;
ld dfs(vector<int> g[],int v=0,int p=-1){
    ld s=0;
    for(auto u:g[v]){
        if(u!=p){
            s+=dfs(g,u,v)+1;
        }
    }
    return s ? s/(g[v].size()-(p!=-1)):0;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    //cin>>T;
    while(T--){
        int n;
        cin>>n;
        vector<int> g[n];
        for(int i=1;i<n;i++){
            int u,v;
            cin>>u>>v;
            v-=1;
            u-=1;
            g[v].push_back(u);
            g[u].push_back(v);
        }
        cout<<fixed<<setprecision(7)<<dfs(g)<<endl;
    }
    return 0;
}

