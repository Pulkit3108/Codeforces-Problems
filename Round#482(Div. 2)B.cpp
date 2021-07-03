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
        ll n;
        cin>>n;
        string s[3];
        int i,j;
        for(i=0;i<3;i++){
            cin>>s[i];
        }
        string t[]={"Kuro", "Shiro" , "Katie"};
        int flag[]={1,1,1};
        pair<int,int> p[3];
        map<char,int> mp[3];
        for(i=0;i<3;i++){
            for(auto c:s[i]){
                mp[i][c]++;
            }
            p[i]={0,i};
            for(auto k:mp[i]){
                p[i].first=max(p[i].first,k.second);
            }
        }
        for(i=0;i<min(1000000LL,n);i++){
            for(j=0;j<3;j++){
                if(p[j].first<s[j].size()){
                    p[j].first++;
                }
                else if(p[j].first==s[j].size() and flag[j]){
                    p[j].first--;
                }
                flag[j]=0;
            }
        }
        sort(p,p+3);
        if(p[1].first==p[2].first){
            cout<<"Draw"<<endl;
        }
        else{ 
            cout<<t[p[2].second]<<endl;
        }
    }
    return 0;
}
