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
        int N;
        cin>>N;
        int i;
        ll a,b=0;
        vector<ll> A(N);
        for(i=1;i<N+1;i++){
            A[i-1]=pow(2,i);
        }
        a=A[N-1];
        for(i=0;i<N/2-1;i++){
            a+=A[i];
        }
        for(i=N/2-1;i<N-1;i++){
            b+=A[i];
        }
        cout<<abs(a-b)<<endl;
    
    }
    return 0;
}
