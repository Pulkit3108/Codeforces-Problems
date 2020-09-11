#include<bits/stdc++.h>
using namespace std;
#define ll long long int
ll calc(ll n){
    ll x;
    if(n==0){
        return 1;
    }
    if(n<10){
        return n;
    }
    x=max(n%10*calc(n/10),9*calc(n/10-1));
    return x;
}
int main(){
    ll n;
    cin>>n;
    cout<<calc(n)<<endl;
    return 0;
}

