#include <bits/stdc++.h>
using namespace std;
#define ll long long int 
const ll N=1e5+10;
const ll inf=1e9+10;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T;
    cin>>T;
    while(T--){
        int n;
        cin>>n;
        map<int,int> mp;
        for(int i=0;i<n;i++){
            int a;
            cin>>a;
            mp[a]+=1;
        }
        int k=0;
        for(auto &it:mp){
            k=max(k,it.second);
        }
        int o=0;
        while(k<n){
            int j=min(k,n-k);
            o+=(j+1);
            k+=j;
        }
        cout<<o<<endl;
    }
    return 0;
}

