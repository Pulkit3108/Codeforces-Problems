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
        int n;
        cin>>n;
        int a[n];
        unordered_map<int,int> mp;
        for(int i=0;i<n;i++){
            cin>>a[i];
            mp[a[i]]=i;
        }
        int m;
        int x=n;
        for(auto it:mp){
            if(x>it.second){
                x=it.second;
                m=it.first;
            }
        }
        cout<<m<<endl;
    }
    return 0;
}
