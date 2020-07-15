#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){   
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T=1;
    //scanf("%d",&T);
    while(T--){   
        ll n;
        scanf("%lld",&n);
        ll c=0,i; 
        for(i=1;i<=sqrt(n);i++){ 
            if(n%i==0){ 
                if(n/i==i){
                    c+=1;
                }
                else{
                    c+=2;
                } 
            } 
        }
        printf("%lld\n",c); 
        
    }
    return 0;
}
