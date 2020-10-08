#include<bits/stdc++.h>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T=1;
    while(T--){
        int n,k,i;
        cin>>n>>k;
        string t;
        cin>>t;
        vector<int> p(n);
        for(i=1;i<t.size();++i){
            int j=p[i-1];
            while(j>0 && t[j]!=t[i]){
                j=p[j-1];
            }
            if(t[i]==t[j]){
                j+=1;
            }
            p[i]=j;
        }
        int l=t.size()-p[n-1];
        for(i=0;i<k-1;++i){
            cout<<t.substr(0,l);
        }
        cout<<t<<endl;
    }
    return 0;
}
