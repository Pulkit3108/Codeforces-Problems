#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    int w[n],h[n];
    int i;
    for(i=0;i<n;i++){
        cin>>w[i]>>h[i];
    }
    int m=max(w[0],h[0]);
    for(i=1;i<n;i++){
        if(max(w[i],h[i])<=m){
            m=max(w[i],h[i]);
        }
        else if(min(w[i],h[i])<=m){
            m=min(w[i],h[i]);
        }
        else{
            cout<<"NO\n";
            return 0;
        }
    }
    cout<<"YES\n";
    return 0;
}
    
