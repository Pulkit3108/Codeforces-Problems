#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define sc1(a) scanf("%d",&a)
#define sc2(a,b) scanf("%d %d",&a,&b)
#define pf1(a) printf("%d\n",a)
#define pf2(a,b) printf("%d %d\n",a,b)
#define vsort(v) sort(v.begin(), v.end())
#define forn(i,n) for(ll i=0; i<n; i++)
#define pb push_back
int main(){
    ll n,a,b;
    cin>>n;
    ll c=1;
    while(n>=c){
        c=c*10;
    }
    c/=10;
    c--;
    a=c;
    b=n-c;
    ll s=0;
    while(a){
        s+=a%10;
        a/=10;
    }
    while(b){
        s+=b%10;
        b/=10;
    }
    printf("%d\n",s);
    return 0;
}
