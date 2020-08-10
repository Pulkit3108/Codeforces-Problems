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
mt19937 rng((int) std::chrono::steady_clock::now().time_since_epoch().count());
int main(){
    int t;
    sc1(t);
    while(t--){
        int n;
        sc1(n);
        vector<int> A;
        int i;
        for(i=1;i<n+1;i++){
            A.pb(i);
        }
        shuffle(A.begin(),A.end(),rng);
        for(i=0;i<n;i++){
            cout<<A[i]<< " ";
        }
        cout<<endl;
    }
    return 0;
}
