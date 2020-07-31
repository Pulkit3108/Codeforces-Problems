#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin>>t;
    while(t--){
        int n,i; 
        cin>>n;
        int x=(n+3)/4;
        for(i=0;i<n-x;++i){
            cout<<9;
        }
        for(i=0;i<x;++i){
            cout<<8;
        }
        cout<<endl;
    }
    return 0;
}
