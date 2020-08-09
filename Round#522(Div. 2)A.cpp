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
    int n,m;
    scanf("%d%d",&n,&m);
    int M=0,i;
    int a[10000];
    for(i=0;i<n;i++){
        int t; 
        scanf("%d",&t);
        a[t]++;
        M=max(M,a[t]);
    }
    int c=0;
    for(i=1;i<=100;i++){
        c+=(a[i]!=0);
    }
    while(M%m!=0){
        M++;
        }
    printf("%d\n",c*M-n);
    return 0;
}
