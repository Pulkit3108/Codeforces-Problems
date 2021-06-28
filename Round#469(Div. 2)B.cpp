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
        int n,m;
        cin>>n>>m;
        vector<int> x(n);
        vector<int> y(m);
        int i;
        for(i=0;i<n;i++){
            cin>>x[i];
        }
        for(i=0;i<m;i++){
            cin>>y[i];
        }
        int s1=0,s2=0,c=0;
        map<int,int> mp;
        for(i=0;i<n;i++){
            s1+=x[i];
            mp[s1]+=1;
        }
        for(i=0;i<m;i++){
            s2+=y[i];
            if(mp[s2]==1){
                c+=1;
            }
        }
      cout<<c<<endl;
    }
    return 0;
}
