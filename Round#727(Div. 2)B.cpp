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
        // code  
        int n,q;
        cin>>n>>q;
        string s;
        cin>>s;
        int k=0;
        vector<int> f(s.size()+1,0);
        for(int i=1;i<s.size()+1;i++){
            k+=s[i-1]-'a'+1;
            f[i]=k;
        }
        while(q--){
            int l,r;
            cin>>l>>r;
            cout<<f[r]-f[l-1]<<endl;
            
        }
    }
    return 0;
}
