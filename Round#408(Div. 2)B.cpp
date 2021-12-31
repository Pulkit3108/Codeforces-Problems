#include<bits/stdc++.h>
using namespace std;
#define ll long long int 
const int inf=1e9+10;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    //cin>>T;
    while(T--){
        int n,m,k;
        cin>>n>>m>>k;
        unordered_set<int> hole;
        for(int i=0;i<m;i++){
            int h;
            cin>>h;
            hole.insert(h);
        }
        int p=1;
        for(int i=0;i<k;i++){
            int u,v;
            cin>>u>>v;
            if(u==p && hole.find(u)==hole.end()){ 
                p=v;
            }
            else if(v==p && hole.find(v)==hole.end()){ 
                p=u;
            }
        }
        cout<<p<<endl;
    }
    return 0;
}

