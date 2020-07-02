#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll T;
    scanf("%lld",&T);
    while(T--){
        ll n;
        scanf("%lld",&n);
        ll x=(n*(n+1))/2;
        printf("%lld\n",x/n);
    }
    
    return 0;
}
