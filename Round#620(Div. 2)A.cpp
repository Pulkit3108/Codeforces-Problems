#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int gcd(int a,int b){ 
    if(b==0){
        return a; 
    } 
    return gcd(b,a%b);     
} 
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin>>T;
    while(T--){
        ll x,y,a,b;
        cin>>x>>y>>a>>b;
        ll ans=y-x;
        ll n=a+b;
        if(ans%n==0){
            cout<<ans/n<<endl;
        }
        else{
            cout<<"-1"<<endl;
        }
    }
    return 0;
}
