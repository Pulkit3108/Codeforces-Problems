#include<bits/stdc++.h>
#include <cstdio>
#include <vector>
using namespace std;
#define ll long long int
int g(int a,int b){
    if(b==0){
        return(a);
    }
    return(g(b,a%b));
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    scanf("%d",&T);
    while(T--){
        ll a,b;
        scanf("%lld%lld",&a,&b);
        ll c;
        if(a%b==0){
            c=0;
        }
        else{
            c=b-(a%b);
        }
        printf("%lld\n",c);
        


    }
    return 0;
}
