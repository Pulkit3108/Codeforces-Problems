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
    int n,k;
    sc2(n,k);
    int i;
    for(i=k-1;i>0;i--){
        if(n%i==0){
            pf1(((n/i)*(k))+i);
            break;
        }
    }
    return 0;
}
