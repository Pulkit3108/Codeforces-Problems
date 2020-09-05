#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll t;
    cin>>t;
    while(t--){
        ll a,b,x,y,n,i;
        cin>>a>>b>>x>>y>>n;
        ll p1,p2;
        ll c1,c2;
        c1=min(n,a-x);
        c2=min(n-c1,b-y);
        p1=(a-c1)*(b-c2);
        c1=min(n,b-y);
        c2=min(n-c1,a-x);
        p2=(b-c1)*(a-c2);
        cout<<min(p1,p2)<<endl;
    }
    return 0; 
} 
