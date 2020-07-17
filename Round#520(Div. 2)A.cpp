#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){   
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T=1;
    //scanf("%d",&T);
    while(T--){
        int i,n;
        scanf("%d",&n);
        vector<int> A(n);   
        for(i=0;i<n;++i){
            scanf("%d",&A[i]);
        }
        int c1=0;
        for(i=0;i<n-1;++i){
            if(A[i]+1==A[i+1]){
                c1+=1;
            }
            else{
                break;
            }
        }
        int c2=0;
        for(i=n-1;i>0;--i){
            if(A[i]-1==A[i-1]){
                c2+=1;
            }
            else{
                break;
            }
        }
        int m=0;
        int x=0;
        for(i=0;i<n-1;++i){
            if(A[i]+1==A[i+1]){
                x+=1;
            }
            else{
                x=0;
            }
            m=max(x,m);
        }
        if((c1==m and A[0]==1) or (c2==m and A[n-1]==1000) or m==0){
            printf("%d\n",m);
        }
        else{
            printf("%d\n",m-1);
        }
    }
    return 0;
}
