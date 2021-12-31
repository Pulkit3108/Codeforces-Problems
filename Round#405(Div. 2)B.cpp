#include<bits/stdc++.h>
using namespace std;
#define ll long long int 
const int inf=1e9+10;
void dfs(int i,int &cv,int &ce,vector<int> &v,vector<int> g[]) {
    assert(!v[i]);
    v[i]=true;
    cv+=1;
    ce+=g[i].size();
    for(auto &it:g[i]){
        if(!v[it]){
            dfs(it,cv,ce,v,g);
        }
    }
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    //cin>>T;
    while(T--){
        int n,m;
        cin>>n>>m;
        vector<int> g[n+10];
        vector<int> v(n+10);
        bool flag=true;
        for(int i=0;i<m;i++){
            int u,v;
            cin>>u>>v;
            g[u].push_back(v);
            g[v].push_back(u);
        }
        for(int i=1;i<n+1;++i){
            if(!v[i]){
                int cv=0,ce=0;
                dfs(i,cv,ce,v,g);
                if(ce!=(ll)cv*(cv-1)){
                    flag=false;
                    break;
                }
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

