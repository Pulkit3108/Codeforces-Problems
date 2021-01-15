#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin>>T;
    while(T--){
        ll n,m;
        cin>>n>>m;
        ll a[2*n][2];
        ll i,j;
        ll k=0;
        for(i=0;i<2*n;i++){
            for(j=0;j<2;j++){
                cin>>a[i][j];
            }
        }
        for(i=0;i<2*n;i+=2){
            if(a[i][1]==a[i+1][0] and a[i][0]!=a[i+1][1]){
                k+=1;
            }
            else if(a[i][1]==a[i+1][0] and a[i][0]==a[i+1][1]){
                k+=2;
            }
        }
        if(m%2==0){
            if(k>0){
                cout<<"YES";
            }
            else{
                cout<<"NO";
            }
        }
        else{
            cout<<"NO";
        }
        cout<<endl;
    }
    return 0;
}
