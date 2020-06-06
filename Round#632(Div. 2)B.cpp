#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin>>T;
    while(T--){
        ll n; 
        cin>>n;
        vector<ll> A(n);
        vector<ll> B(n);
        ll i;
        for(i=0;i<n;++i){
            cin>>A[i];
        }
        for(i=0;i<n;++i){
            cin>>B[i];
        }
        ll x=0,y=0;
        ll c=1;
        for(i=0;i<n;++i){
            if(A[i]>B[i] && x==0){
                c=0;
                break;
            } 
            else if(A[i]<B[i] && y==0){
                c=0;
                break;
            }
            if(A[i]==-1){
                x=1;
            }
            if(A[i]==1){
                y=1;
            }
        }
        if(c==1){
            cout<<"YES"<<endl;
        }
        else{
            cout<<"NO"<<endl;
        }
    }
    return 0;
}
