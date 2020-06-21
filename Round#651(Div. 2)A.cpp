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
        int n;
        scanf("%d",&n);
        
        printf("%d\n",n/2);
    }
    return 0;
}
