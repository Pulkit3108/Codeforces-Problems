#include <bits/stdc++.h>
using namespace std;
#define ll long long int 
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T;
    cin>>T;
    while (T--){
        int n;
        cin>>n;
        vector<int> a(n);
        vector<int> b(n);
        unordered_map<int,int> mp;
        for(int i=0;i<n;i++){
            cin>>a[i];
            mp[a[i]]=i;
        }
        for(int i=0;i<n;i++){
            cin>>b[i];
            mp[b[i]]=i;
        }
        int m=INT_MAX;
        vector<int> v;
        for(int i=2*n;i>=0;i-=2){
            m=min(m,mp[i]);
            v.push_back(m);
        }
        int j=0;
        m=INT_MAX;
        for(int i=2*n-1;i>=1;i-=2){
            m=min(m,mp[i]+v[j]);
            j+=1;
        }
        cout<<m<<endl;
    }
    return 0;
}

