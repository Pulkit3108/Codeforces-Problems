#include<bits/stdc++.h>
using namespace std;
#define ll long long int 
#define ld long double
const ll mod=1e9+7;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    //cin>>T;
    while(T--){
        int n,m;
        cin>>n>>m;
        vector<vector<char>> a(n,vector<char>(m,'.'));
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                cin>>a[i][j];
            }
        }
        vector<int> f(m+1,0);
        for(int i=1;i<n;i++){
            for(int j=1;j<m;j++){
                if(a[i][j-1]=='X' && a[i-1][j]=='X'){
                    f[j+1]=1;
                }
            }
        }
        for(int i=1;i<m+1;i++){
            f[i]+=f[i-1];
        }
        int q;
        cin>>q;
        while(q--){
            int x,y;
            cin>>x>>y;
            cout<<((f[y]-f[x]==0)?"YES":"NO")<<endl;
        }
    }
    return 0;
}

