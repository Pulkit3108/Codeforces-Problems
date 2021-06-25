#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    //cin>>T;
    while(T--){ 
        int n,k,m;
        cin>>n>>k>>m;
        map<string,int> mp;
        string s[100005];
        int i,j;
        for(i=1;i<n+1;i++){
            cin>>s[i];
        }
        for(i=1;i<n+1;i++){
            int x;
            cin>>x;
            mp[s[i]]=x;
        }
        for(i=1;i<k+1;i++){
            int y;
            cin>>y;
            int a[y+1];
            int m=INT_MAX;
            for(j=0;j<y;j++){
                cin>>a[j];
                m=min(m,mp[s[a[j]]]);
            }
            for(j=0;j<y;j++){
                mp[s[a[j]]]=m;
            }
        }
        ll r=0;
        for(i=1;i<m+1;i++){
            string t;
            cin>>t;
            r+=mp[t];
        }
        cout<<r<<endl;
    }
    return 0;
}
