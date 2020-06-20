#include<bits/stdc++.h>
#include <vector>
using namespace std;
#define ll long long int
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    scanf("%d",&T);
    while(T--){
        ll n;
        scanf("%lld",&n);
        vector<ll> a(n);
        vector<ll> b(n);
        ll i,k=0;
        for(i=0;i<n;++i){
            scanf("%lld",&a[i]);
        }
        sort(a.begin(),a.end());
        if(n%2==0){
            for(i=n/2;i<n;++i){
                b[k]=a[i];
                b[k+1]=a[n-1-i];
                k+=2;
            }
        }
        else{
            b[k]=a[n/2];
            k+=1;
            for(i=(n/2)+1;i<n;++i){
                b[k]=a[i];
                b[k+1]=a[n-1-i];
                k+=2;
            }
        }
        for(i=0;i<n;++i){
            printf("%lld ",b[i]);
        }
        printf("\n");



    }
    return 0;
}
