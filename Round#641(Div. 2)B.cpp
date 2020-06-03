#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll t;
    cin>>t;
    while(t--){
        ll n,i,j;
        cin>>n;
        vector<int> A(n+1);
        vector<int> F(n+1);
        for(i=1;i<=n;i++){
            cin>>A[i];
        }
        for(i=1;i<=n;i++){
            F[i]=1;
        }
        for(i=1;i<=n;i++){
            for(j=i*2;j<=n;j+=i){
                if(A[i]<A[j]){
                    F[j]=std::max(F[j],F[i]+1);
                }
            }
        } 
        ll ans = 0;
        for(i=1;i<=n;i++){
            if(ans<F[i]){
                ans=F[i];
            }
        }
        cout<<ans<<endl;
    }
    return 0;
}
