#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define sc1(a) scanf("%lld",&a)
#define sc2(a,b) scanf("%lld %lld",&a,&b)
#define pf1(a) printf("%lld\n",a)
#define pf2(a,b) printf("%lld %lld\n",a,b)
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll T;
    sc1(T);
    while(T--){
            ll n;
            sc1(n);
            vector<ll> a(n);
            ll i;
            for(i=0;i<n;i++){
                sc1(a[i]);
            }
            ll k = 0;
            while(k<n && a[k]==1){
                k+=1;
            }
            if(k==n && k%2==0){
                printf("Second\n");
                continue;
            }
            if(k==n && k%2!=0){
                printf("First\n");
                continue;
            }
            if(k%2==0){
                printf("First\n");
            }
            else{
                printf("Second\n");
            }
        }  
    return 0;
}
