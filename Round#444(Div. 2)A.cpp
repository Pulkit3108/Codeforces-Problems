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
        string s;
        cin>>s;
        int c=0;
        bool flag=false;
        for(int i=0;i<s.size();i++){
            if(flag and s[i]=='0'){
                c+=1;
            }
            if(s[i]=='1'){
                flag=true;
            }
        }
        if(c>5){
            cout<<"yes"<<endl;
        }
        else{
            cout<<"no"<<endl;
        }
    }
    return 0;
}
