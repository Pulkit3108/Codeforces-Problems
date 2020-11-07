#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int a,b,i;
        cin>>a>>b;
        string s;
        cin>>s;
        int f=-1;
        int l=-1;
        for(i=0;i<s.size();i++){
            if(s[i]=='1'){
                f=i;
                break;
            }
        }
        for(i = s.size()-1;i>=0;i--){
            if(s[i]=='1'){
                l=i;
                break;
            }
        }
        if(f==l && f==-1){
            cout<<0<<"\n";
            continue;
        }
        int r=a;
        int k=INT_MAX;
        for(i=f;i<=l;i++){
            int c=0;
            while(s[i]=='0'){
                c+=1;
                i+=1;
            }
            r+=min(a,b*c);
        }
        cout<<r<<"\n";
    }
}
    
