#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int n;
vector<int> B(1007,0);
bool ok(int d){
    int i;
    for(i=0;i+d<n;++i)
        if(B[i+1]-B[i]!=B[i+d+1]-B[i+d]){
            return(false);
        }
    return(true);
}
int main(){   
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T=1;
    //scanf("%d",&T);
    while(T--){
        int i;   
        scanf("%d",&n);
        for(i=1;i<=n;++i){
            scanf("%d",&B[i]);
        }
        vector<int> A;
        for(i=1;i<=n;++i){
            if(ok(i)){
                A.push_back(i);
            }
        } 
        printf("%d\n",A.size());
        for(int a: A)
            printf("%d ",a);
        
    }
    return 0;
}
