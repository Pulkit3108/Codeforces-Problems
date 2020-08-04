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
    int t;
    string s;
    sc1(t);
    while(t--){
        int n;
        sc1(n);
        cin>>s;
        int k=-1;
        int c=0,i;
        for(i=0;i<n;i++){
            if(s[i]=='P' && k>-1){
                c=max(c,i-k);
            }
            else if(s[i]=='A'){
                k = i;
            }
        }
        pf1(c);
    }
    return 0;
}
