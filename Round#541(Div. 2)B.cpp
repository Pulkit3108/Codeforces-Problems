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
    int n,i;
    cin>>n;
    int a[n+1],b[n+1];
    a[0]=0;
    b[0]=0;
    for(i=1;i<=n;i++){
        scanf("%d%d",&a[i],&b[i]);
    }
    int c=0;
    for(i=1;i<=n;i++){
        c+=max(0,min(a[i],b[i])-max(a[i-1],b[i-1])+1);
        if(a[i]==b[i]){
            a[i]++; 
        }
    }
    cout<<c<<endl;
    return 0;
}
