#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin>>n;
    ll M[n][n];
    ll i,j;
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            cin>>M[i][j];
        }
    }
    ll d=sqrt((M[0][1]*M[0][2])/M[1][2]);
    cout<<d<<" ";
    for(i=1;i<n;++i) {
        cout<<M[0][i]/d<<" ";
    }
    return 0; 
} 
