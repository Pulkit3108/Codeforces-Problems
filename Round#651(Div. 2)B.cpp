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
        vector<int> a(2*n);
        vector<int> o;
        vector<int> e;
        int i;
        for(i=0;i<2*n;i++){
            scanf("%d",&a[i]);
            if(a[i]%2==0){
                e.push_back(i+1);
            }
            else{
                o.push_back(i+1);
            }
        }
        vector<pair<int,int>> r;
        for(i=0;i+1<o.size();i+=2){
            r.push_back({o[i],o[i+1]});
        }   
        for(i=0;i+1<e.size();i+=2){
            r.push_back({e[i],e[i+1]});
        } 
        for(i=0;i<n-1;i++){
            printf("%d %d\n",r[i].first,r[i].second);
        }


    }
    return 0;
}
