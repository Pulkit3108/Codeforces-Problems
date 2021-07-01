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
        char s[n][m];
        int i,j,k,c=1;
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                cin>>s[i][j];
            }
        }
        for(i=0;i<n;i++){
            for(j=i+1;j<n;j++){
                bool f1=true;
                bool f2=true;
                for(k=0;k<m;k++){
                    if(s[i][k]==s[j][k] && s[i][k]=='#'){
                        f1=false;
                    }
                    if(s[i][k]!=s[j][k]){
                        f2=false;
                    }
                }
                if(!f1 && !f2){
                    c=0;
                    break;
                }
            }
        }
        if(c){
            cout<<"Yes"<<endl;
        }
        else{
            cout<<"No"<<endl;
        }
    }
    return 0;
}
