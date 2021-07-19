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
        ll h,w;
        cin>>h>>w;
        ll i,j;
        ll t[h][w];
        for(i=0;i<h;i++){
            for(j=0;j<w;j++){
                t[i][j]=0;
            }
        }
        for(i=0;i<h;i+=2){
            t[i][0]=1;
            t[i][w-1]=1;
        }
        for(j=2;j<w-2;j+=2){
            t[0][j]=1;
            t[h-1][j]=1;
        }
        for(i=0;i<h;i++){
            for(j=0;j<w;j++){
                cout<<t[i][j];
            }
            cout<<endl;
        }
        cout<<endl;
    }
    return 0;
}
