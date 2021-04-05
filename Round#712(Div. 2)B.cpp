#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T;
    cin>>T;
    while(T--){
        ll n;
        cin>>n;
        string a,b;
        cin>>a>>b;
        int o=0,z=0;
        vector<pair<int,int>> x;
        int i,j=0;
        for(i=0;i<n;i++){
            if(a[i]=='1'){
                o+=1;
            }
            else{
                z+=1;
            }
            if(o==z){
                x.push_back({j,i});
                j=i+1;
            }
        }
        for(auto k : x){
            int s=k.first;
            int e=k.second;
            if(a[s]==b[s]){
                continue;
            }
            else{
                for(i=s;i<e+1;i++){
                    if(a[i]=='0'){
                        a[i]='1';
                    }
                    else{
                        a[i]='0';
                    }
                }
            }
        }
        int flag=1;
        for(i=0;i<n;i++){
            if(a[i]!=b[i]){
                flag=0;
                break;
            }
        }
        if(flag){
            cout<<"YES"<<endl;
        }
        else{
            cout<<"NO"<<endl;
        }
    }
    return 0;
}
