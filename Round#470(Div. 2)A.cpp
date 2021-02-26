#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll T=1;
    //cin>>T;
    while(T--){
        int n,m;
        cin>>n>>m;
        int i,j,c=1,k=1;
        char a[n][m];
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                cin>>a[i][j];
            }
        }
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                if(a[i][j]=='S'){
                    if(j+1<m){
                        if(a[i][j+1]=='W'){
                            k=0;
                            break;
                        }
                        else if(a[i][j+1]=='.'){
                            a[i][j+1]='D';
                        }
                    }
                    if(j-1>-1){
                        if(a[i][j-1]=='W'){
                            k=0;
                            break;
                        }
                        else if(a[i][j-1]=='.'){
                            a[i][j-1]='D';
                        }
                    }
                    if(i+1<n){
                        if(a[i+1][j]=='W'){
                            k=0;
                            break;
                        }
                        else if(a[i+1][j]=='.'){
                            a[i+1][j]='D';
                        }
                    }
                    if(i-1>-1){
                        if(a[i-1][j]=='W'){
                            k=0;
                            break;
                        }
                        else if(a[i-1][j]=='.'){
                            a[i-1][j]='D';
                        }
                    }
                }
            }
            if(k==0){
                c=0;
                break;
            }
        }
        if(c==1){
            cout<<"Yes\n";
            for(i=0;i<n;i++){
                for(j=0;j<m;j++){
                    cout<<a[i][j];
                }
                cout<<"\n";
            }
        }
        else{
            cout<<"No\n";
        }
        
        
    }
    return 0;
}
