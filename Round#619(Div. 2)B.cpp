#include<bits/stdc++.h>
#include <climits>
#include <cmath>
using namespace std;
#define ll long long int
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll T;
    cin>>T;
    while(T--){
        ll N;
        cin>>N;
        vector<ll> A(N+2);
        for(ll i=1;i<=N;i++){
            cin>>A[i];
        }
        A[0]=-1,A[N+1]=-1;
        ll c=0;
        ll f=-1;
        ll l=1e9+1;
        ll r=0;
        for(ll i=1;i<=N;i++){
            if(A[i]!=-1){
                f=A[i];
                if(A[i+1]!=-1){
                    c=max(abs(A[i+1]-A[i]),c);
                }
                if(A[i-1]!=-1){
                    c=max(abs(A[i]-A[i-1]),c);
                }     
            }
            else{
                if(A[i-1]!=-1){
                    l=min(A[i-1],l);
                    r=max(A[i-1],r);
                }
                if(A[i+1]!=-1){
                    l=min(A[i+1],l);
                    r=max(A[i+1],r);
                }
            }
        }
        ll ans=(l+r+1)/2;
        c=max(abs(r-ans),c);
        c=max(abs(ans-l),c);
        if(f==-1){
            cout<<0<<" "<<42<<endl;
            continue;
        }
        cout<<c<<" "<<ans<<endl;
    }
    return 0;
}
