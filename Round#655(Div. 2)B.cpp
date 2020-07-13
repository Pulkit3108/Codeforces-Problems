#include<bits/stdc++.h>
using namespace std;
#define ll long long int
ll maxF(ll n){
    ll i;
    ll m=1;
    for(i=2;i<=sqrt(n);i++){ 
        if(n%i==0){ 
            if(i==(n/i)){
                m=max(m,i); 
            }     
            else{
                ll c=n/i;
                m=max(m,c); 
            }          
        } 
    } 
    return(m); 
} 
int main(){   
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    scanf("%d",&T);
    while(T--){   
        ll n;
        scanf("%lld",&n);
        //printf("%lld",maxF(n));
        if(n%2==0){
            printf("%lld %lld\n",n/2,n/2);
        }
        else if((n-3)!=0){
            printf("%lld %lld\n",maxF(n),n-maxF(n));
        }
        else{
            printf("%d %d\n",1,2);
        }
    }
    return 0;
}
