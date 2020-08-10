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
    sc1(t);
    while(t--){
        int n,m;
        sc2(n,m);
        char A[n][m];
        int i,j,c=0;
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                cin>>A[i][j];
                if(A[i][j] == 'C'){
                    continue;
                }
                if(i==n-1 and A[i][j]=='D'){
                    c+=1;
                }
                if(j==m-1 and A[i][j]=='R'){
                    c+=1;
                }
            }
        }
        pf1(c);   
    }
    return 0;
}
