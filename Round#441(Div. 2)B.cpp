#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int T=1;
    //cin>>T;
    while(T--){
        int n,k,m;
        cin>>n>>k>>m;
        int a[n];
        for(int i=0;i<n;i++){
            cin>>a[i];
        }
        map<int,vector<ll>> mp;
        for(int i=0;i<n;i++){
            mp[a[i]%m].push_back(a[i]);
        }
        bool flag=true;
        for(auto it:mp){
            if(it.second.size()>=k){
                cout<<"Yes"<<endl;
                for(int i=0;i<k;i++){
                    cout<<it.second[i]<<" ";
                }
                cout<<endl;
                flag=false;
                break;
            }
        }
        if(flag){
            cout<<"No"<<endl;
        }
    }
    return 0;
}
