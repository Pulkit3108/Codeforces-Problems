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
    ll T=1;
    //sc1(T);
    while(T--){
        ll n,k;
        sc2(n,k);
        vector<ll> A(5001);
        vector<pair<ll, ll> > v;
        ll c=0;
        ll i=0;
        for(i=0;i<n;i++){
            ll a;
            sc1(a);
            A[a]++;
            v.push_back(make_pair(a,i));
            if(A[a]>k){
                c=1;
            } 
        }
        if(c==1){
            printf("NO\n");
            return 0;
        }
        printf("YES\n");
        sort(v.begin(),v.end());
        vector<ll> B(n);
        ll cc=0;
        for(i=0;i<n;i++){
            ll ind=v[i].second;
            B[ind]=cc%k+1;
            cc++;
        }
        for(i=0;i<n;i++){
            printf("%lld ",B[i]);
        }
        printf("\n");
    }  
    return 0;
}
