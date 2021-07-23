#include<bits/stdc++.h>
using namespace std;
#define ll long long int
const int mod=1e9+7;
const ll N=1e7+10;
ll f[N];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    //cin>>T;
    while(T--){
        string s;
        cin>>s;
        ll m,i;
        cin>>m;
        for(i=0;i<m;++i){
            int x;
            cin>>x;
            f[x]+=1;
            f[s.size()-x+2]-=1;
        }
        for(i=1;i<=s.size()/2;++i){
            f[i]+=f[i-1];
            if(f[i]%2!=0){
                swap(s[i-1],s[(s.size()-i+1)-1]);
            }
        }
        cout<<s<<endl;
    }
    return 0;
}
