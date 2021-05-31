#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int T;
    cin>>T;
    while(T--){
        int n,m;
        cin>>n>>m;
        multiset<pair<int,int>> mt;
        int a[n][m];
        int i,j;
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                a[i][j]=-1;
                int x;
                cin>>x;
                mt.insert({x,i});
            }
        }
        for(i=0;i<m;i++){
            auto itr=mt.begin();
            a[itr->second][i]=itr->first;
            mt.erase(itr);
        }
        while(!mt.empty()){
            auto itr=mt.begin();
            int k=0;
            while(a[itr->second][k]!=-1){
                k+=1;
            }
            a[itr->second][k]=itr->first;
            mt.erase(itr);
        }
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                cout<<a[i][j]<<" ";
            }
            cout<<"\n";
        }
        
    }
    return 0;
}
