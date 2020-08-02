#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll n,i;
    cin>>n;
    ll a[n];
    for(i=0;i<n;i++){
        cin>>a[i];
    }
    ll c=INT_MAX;
    ll k=0;
    for(i=n-1;i>=0;i--){
        if((c-1)<a[i]){
            c=c-1;
        }
        else{
            c=a[i];
        }
        if(c<0){
            c=0;
        }
        k+=c;
    }
    cout<<k<<endl;
    return 0;
}
