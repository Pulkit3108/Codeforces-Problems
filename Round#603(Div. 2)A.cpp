#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){   
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    scanf("%d",&T);
    while(T--){   
        vector<int> A(3);
        scanf("%d%d%d",&A[0],&A[1],&A[2]);
        sort(A.begin(),A.end());
        if(A[2]<=A[0]+A[1]){
            printf("%d\n",((A[0]+A[1]+A[2])/2));
        }  
        else{
            printf("%d\n",(A[0]+A[1]));
        }            
    }
    return 0;
}
