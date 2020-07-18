#include<bits/stdc++.h>
using namespace std;
#define ll long long int 
int main(){   
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll T;
    scanf("%lld",&T);
    while(T--){
        vector<ll> A(3);
        ll i;
        for(i=0;i<3;i++){
            scanf("%lld",&A[i]);
        } 
        sort(A.begin(), A.end());
        if(A[1]!=A[2]){
            printf("NO\n");
        } 
        else{
            printf("YES\n");
            printf("%lld %lld %lld\n",A[0],A[0],A[1]);
        }

    }    
    return 0;
}
